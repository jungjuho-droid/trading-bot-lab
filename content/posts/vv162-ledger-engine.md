---
title: "[개발일지] VV162 — 258,020원이 장부에서 사라져 있었다 (Dev Log VV162: 258,020 Won Had Quietly Vanished From the Books)"
description: "봇의 계산을 손익의 정답으로 삼는 구조 자체가 문제였다. Treating the bot's own arithmetic as the source of truth was the bug, not any single line of code."
date: 2026-07-29T21:58:00+09:00
draft: false
tags: ["개발일지", "자동매매", "업비트", "손익계산"]
summary: "거래소 실제 손익 -336,658원, 봇 장부 -78,637원. 차이는 개별 버그가 아니라 구조였다."
---

## 전수 대조에서 나온 숫자

거래소 주문내역과 봇 장부를 종목별로 맞춰봤다. 차이가 컸다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>2026-07-29 · 전수 대조</em></div>
<pre><code><span class="w">거래소 실제</span> <span class="r">-336,658원</span>
<span class="w">봇 장부</span> <span class="y">-78,637원</span>
<span class="c">--------------------------------------------------</span>
<span class="r">누락 258,020원</span>
<span class="c"> </span>
<span class="r">·</span> 봇 밖 수동 매도가 장부에 안 잡힘 <span class="c">RE -135,971원 등 19종목</span>
<span class="r">·</span> 구버전이 트리거 가격으로 손익 추정 <span class="c">XLM 16,084원 오차</span>
<span class="r">·</span> 먼지 슬롯 해제가 팔지도 않은 코인을 계상
<span class="c"> </span><span class="c">PROS 7.33개는 지금도 보유 중인데 +554원이 실현으로 기록</span></code></pre>
</div>

세 갈래인데 뿌리는 하나다. **봇 내부 계산을 손익의 정답으로 삼고 있었다.** 그러니 봇이 모르는 일은 장부에도 없다.

## 정답을 밖으로 옮겼다

`vv_ledger.py` 를 새로 만들었다. 종목별 체결내역을 시간순으로 놓고 선입선출로 대응시킨다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>FIFO 원장 · 계산 방식</em></div>
<pre><code><span class="w">매수</span> 재고 적재 <span class="c">단가 = (체결대금 + 수수료) / 수량</span>
<span class="w">매도</span> 오래된 재고부터 소진
<span class="g"> </span> <span class="g">실현손익 = 실수령 - 소진원가</span>
<span class="c">--------------------------------------------------</span>
<span class="g">검증</span> 37종목 독립 대조 <span class="g">오차 0원</span>
<span class="g"> </span> 합계 -336,658원 일치
<span class="w">기동 시 자동 정정</span> -78,637 → -336,658 <span class="c">(-258,020)</span></code></pre>
</div>

분할매수든 분할매도든 수동매도든 먼지 잔량이든 전부 자동으로 맞는다. 특수 케이스마다 예외를 다는 대신 원장 하나로 수렴시켰다.

그리고 5분마다 대조 루프를 돌린다. 내부 증분 계산은 빠른 추정치로만 쓰고 원장 값으로 덮어쓴다. 보정액이 5,000원을 넘으면 경고를 띄운다. 258,020원 오차가 사흘 동안 조용히 굴러다니던 일을 막기 위한 장치다.

## 자기 기억을 안 믿기로 했다

소프트웨어 입장에서는 굴욕이다. 자기가 계산한 값을 못 믿겠다고 선언한 셈이니까.

그런데 회계로 보면 당연한 얘기다. 손익은 내가 얼마를 벌었다고 생각하는지가 아니라 계좌에 얼마가 들어왔는지다. **틀린 장부로 하는 성적 분석은 전부 틀린다.** 파라미터를 아무리 정교하게 튜닝해도 그 위에 세운 거라면 소용없다.

> 피터 린치는 자기가 무엇을 갖고 있는지 모르면서 투자하지 말라고 했다. 나는 무엇을 잃었는지도 모르고 있었다.

---

## 약어 풀이

\* 이 글에 나온 영어 약어를 풀어 둔다.

- **FIFO** (First In First Out): 선입선출. 먼저 산 물량부터 먼저 팔린 것으로 대응시켜 원가와 실현손익을 계산하는 방식.
