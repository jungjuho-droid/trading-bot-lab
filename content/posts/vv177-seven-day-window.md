---
title: "[개발일지] VV177 — 월간손익이 저절로 좋아지고 있었다 (Dev Log VV177: My Monthly P&L Was Improving All by Itself)"
description: "조회 API가 최근 7일만 돌려주자 오래된 손실이 조용히 증발했다. When the orders API silently capped its window at seven days, old losses simply disappeared from the books."
date: 2026-07-31T20:07:00+09:00
draft: false
tags: ["개발일지", "자동매매", "업비트", "손익계산"]
summary: "-311,556원에서 -166,946원으로. 아무것도 안 했는데 숫자가 좋아지면 그건 좋은 소식이 아니다."
---

## 숫자가 혼자 좋아졌다

며칠에 걸쳐 월간손익이 계속 개선됐다. 손절 횟수도 같이 줄었다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>가만히 뒀는데 좋아지는 장부</em></div>
<pre><code><span class="w">월간손익</span> -311,556 → -307,521 → -242,486 → <span class="y">-166,946</span>
<span class="w">손절 횟수</span> 32 → 31 → 30
<span class="c">--------------------------------------------------</span>
<span class="r">손익이 저절로 좋아질 방법은 없다</span></code></pre>
</div>

## 창이 7일에서 잘리고 있었다

주문내역 조회 API 는 기간을 안 주면 최근 7일만 돌려준다. 봇 거래가 7일을 넘어가자 오래된 매수부터 응답에서 빠졌다. 짝을 잃은 매도는 선입선출 대응에서 조용히 건너뛰어졌고, 그만큼 실현손실이 사라졌다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>고아 매도 · 실측</em></div>
<pre><code><span class="w">KRW-XLM</span> 원장 1건 <span class="c">(매도만)</span> → 손익 0
<span class="c"> </span> 봇 기록 <span class="r">-58,046원</span>
<span class="w">KRW-RE</span> 몇 분 사이 <span class="r">-115,120원</span> 이벤트 소멸
<span class="c">--------------------------------------------------</span>
<span class="r">배포 게이트가 못 잡았다</span>
<span class="c">상태파일과 원장을 비교하는데 둘 다 같은 오염원을 본다</span>
<span class="c">그날 세 번 다 "차이 0원" 으로 통과했다</span></code></pre>
</div>

이 마지막 줄이 제일 아팠다. 검증 장치가 있었는데 검증 대상과 기준이 같은 데이터를 보고 있었다. 그러면 항상 통과한다.

## 창을 6일씩 잘라 45일을 훑는다

8일 범위를 한 번에 요청하면 API 가 거부한다. 그래서 6일씩 나눠 페이징하고 45일까지 소급한다. 지난 창은 안 바뀌므로 캐시에 남긴다. 조회 실패는 '없음'과 구별하고, 고아 매도는 세어서 드러낸다. 결과가 불완전하면 장부를 덮어쓰지 않고 경고만 띄운다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>실계좌 재계산 · 상태파일 대비</em></div>
<pre><code><span class="w">일간</span> -20,634 <span class="c">/</span> -20,634 <span class="g">차이 0</span>
<span class="w">주간</span> -91,505 <span class="c">/</span> -91,505 <span class="g">차이 0</span>
<span class="w">월간</span> <span class="r">-562,325</span> <span class="c">/</span> -166,946 <span class="r">차이 -395,379</span>
<span class="w">승패</span> 54승137패 <span class="c">/</span> 27승30패
<span class="c">--------------------------------------------------</span>
<span class="r">07-27 이전 이벤트 178건, 합계 -522,768원이 통째로 빠져 있었다</span>
<span class="g">RE 체결 6건 → 27건 · -115,120원 복구</span></code></pre>
</div>

일간과 주간이 정확했던 게 이 버그를 오래 숨겼다. 7일 창 안이라 원래 맞았던 것이다.

## 검증이 자기를 검증하면

이번 건은 버그보다 검증 설계의 실패다. 게이트를 통과했는데 값이 틀렸다면 게이트가 잘못 서 있는 것이다.

**대조는 서로 다른 출처끼리 해야 뜻이 있다.** 같은 우물에서 두 번 떠서 맞춰보면 언제나 같다.

> 마크 더글러스는 트레이더의 진짜 적은 시장이 아니라 스스로 만든 착각이라고 했다. 나흘 동안 좋아지는 숫자를 보면서 기분이 나쁘지 않았다. 그게 제일 위험한 부분이었다.

---

## 약어 풀이

\* 이 글에 나온 영어 약어를 풀어 둔다.

- **API** (Application Programming Interface): 응용 프로그램 인터페이스. 거래소 서버에 주문·체결 내역을 요청하고 받아오는 규격.
