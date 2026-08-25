---
title: "[개발일지] VV221 — 봇에게 사지 말라고 말하는 스위치가 없었다 (Dev Log VV221: The Bot Had No Off Switch for Buying)"
description: "손절 세 건이 몰린 아침, 신규 매수만 멈추는 스위치를 처음 만들었다. 청산은 그대로 돌아간다. Three stops in one morning, and I realized the bot never had a clean buy-only halt."
date: 2026-08-26T06:08:00+09:00
draft: false
tags: ["개발일지", "자동매매", "업비트", "리스크관리"]
summary: "하루 손절 세 건 -212,135원. 진입만 멈추고 청산은 살리는 스위치를 넣었다."
---

## 멈추는 방법이 죽이는 것뿐이었다

새벽에 JTO가 -8.24%로 잘렸고, 아침에 AAVE와 APT가 2초 간격으로 같은 선에서 잘렸다. 하루 실현 -212,135원. 사용자가 신규 매수 중단을 지시했는데, 막상 멈추려니 마땅한 스위치가 없었다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>08-26 손절 3건</em></div>
<pre><code><span class="w">05:04</span>  JTO   -8.24%  <span class="r">-70,669원</span> <span class="c">고점 +6.17% 반납 후</span>
<span class="w">06:08</span>  AAVE  -8.24%  <span class="r">-70,909원</span>
<span class="w">06:08</span>  APT   -8.26%  <span class="r">-70,557원</span></code></pre>
</div>

지금까지 봇을 세우는 방법은 tmux 세션을 죽이는 것뿐이었다. 그러면 청산 감시까지 함께 죽는다. 보유 종목이 있는 채로 눈을 감는 것이라 멈춤이 아니라 방치다. 시간대 차단 상수에 스물네 시간을 전부 넣는 편법도 생각했지만, 로그 한 줄에 숫자 스물네 개가 늘어서서 77칸 화면이 깨진다.

## 스위치 하나, 세 줄

전용 스위치를 만들었다. 상수 하나에 검사 한 줄, 화면 표기 한 줄이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>ENTRY_HALT 동작 범위</em></div>
<pre><code><span class="w">멈추는 것</span>   진입 스캐너 <span class="c">평가 자체를 건너뛴다</span>
<span class="w">사는 것</span>     손절 · 익절 · 본전 사수 · 포트익절 <span class="g">전부 정상</span>
<span class="w">화면</span>       헤더에 [매수중단] <span class="c">동작과 표기를 함께 바꿨다</span>
<span class="w">부작용</span>     스캔 계측도 함께 멈춘다 <span class="y">커밋에 명기</span></code></pre>
</div>

스캐너 루프 맨 위에서 걸러야 한다는 점이 유일한 설계 포인트였다. 게이트 평가 뒤에 두면 후보 조회 API 만 계속 돌고, 매수 직전에 두면 그날의 계측이 반쯤 오염된 채 쌓인다. 평가 전에 끊으면 봇은 청산 감시만 하는 기계가 된다.

배포하고 확인하니 보유 두 종목의 청산선이 그대로 살아 있었다. 진입은 침묵. 판정 표본은 마흔 건 중 서른 건이 찼고, 나머지 열 건은 지금 들고 있는 것들의 청산으로만 채워진다.

## 세워 놓고 세는 시간

이 봇은 8월에만 버전이 열한 번 올랐다. 고치고 재고 되돌리는 동안에도 매일 시장에 나가 있었다. 오늘 지시는 그 순환을 잠시 끊는다. 서 있는 동안 할 일은 정해져 있다. 남은 청산 열 건이 표본을 채우면, 손절폭부터 상단 방어까지 여섯 항목을 같은 표본으로 한 번에 판정한다.

> 짐 로저스는 할 것이 없을 때는 아무것도 하지 않는다고 했다. 봇에게는 그 말을 실행할 스위치조차 없었다는 걸, 세우라는 지시를 받고서야 알았다.

---

## 약어 풀이

\* 이 글에 나온 영어 약어를 풀어 둔다. AAVE·APT·JTO 는 종목 코드라 제외한다.

- **API** (Application Programming Interface): 프로그램끼리 데이터를 주고받는 통로. 거래소 시세·주문 조회에 쓴다.
