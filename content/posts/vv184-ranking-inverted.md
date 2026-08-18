---
title: "[개발일지] VV184 — 후보가 여럿일 때 봇은 더 나쁜 쪽을 먼저 사고 있었다 (Dev Log VV184: When Several Candidates Passed, the Bot Kept Picking the Worse One)"
description: "랭킹 총점과 실제 성과의 상관이 음수였다. 논리는 그럴듯했고 데이터가 반박했다. The ranking score correlated negatively with outcomes; the logic was clean and the data disagreed."
date: 2026-08-01T23:19:00+09:00
draft: false
tags: ["개발일지", "자동매매", "업비트", "백테스트"]
summary: "게이트 통과자 21건 기준 총점과 결과의 상관이 -0.371. 점수가 높을수록 성적이 나빴다."
---

## 스캔로그를 다시 돌려봤다

스캔 기록 3,443건 중 1,116건에 대해 "그 시점에 샀다면" 을 현행 청산엔진으로 시뮬레이션했다. 그리고 실제 청산 56건의 진입 지표와 대조했다.

여기서 예상 못 한 게 나왔다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>랭킹 총점과 결과의 상관 · 게이트 통과자 21건</em></div>
<pre><code><span class="r">총점 - 결과 상관</span> <span class="r">-0.371</span>
<span class="c">--------------------------------------------------</span>
<span class="w">과매도 가점</span> 익절 RSI 37.7 <span class="c">vs</span> 손절 RSI 31.0
<span class="c"> </span> <span class="r">덜 과매도한 쪽이 이겼다</span>
<span class="c"> </span> 통과자 기준 상관 <span class="r">-0.386</span>
<span class="w">압축 가점</span> 전체 -0.069 <span class="c">·</span> 통과자 <span class="r">-0.325</span>
<span class="c"> </span> <span class="r">양쪽 다 음수인 유일한 항목</span></code></pre>
</div>

점수를 매기는 항목 두 개가 반대로 작동하고 있었다. 게이트가 이미 RSI 45 이하를 거르고 난 뒤에는, 더 깊은 과매도가 기회가 아니라 붕괴 신호였다. 둘 다 가중치를 0으로 내렸다.

이 변경은 진입 빈도를 안 건드린다. 통과자 사이의 순서만 바뀐다. 그런데 그동안 후보가 여럿일 때 봇은 계속 나쁜 쪽을 먼저 집고 있었다.

## 중기추세와 시간대

같이 손본 것이 둘 더 있다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>실제 청산 18건 · 14일 고점 대비</em></div>
<pre><code><span class="g">익절 4건</span> 평균 <span class="g">0.000%</span>
<span class="r">손절 14건</span> 평균 <span class="r">-8.605%</span>
<span class="c">--------------------------------------------------</span>
<span class="g">차이 8.605%p</span> <span class="c">· 다른 지표는 사실상 구분 불가</span>
<span class="c">낙폭 +0.044 · 밴드 -0.072 · 반등 -0.138</span></code></pre>
</div>

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>시간대별 · 스캔 1,116건</em></div>
<pre><code><span class="r">19시</span> -0.752% <span class="c">승률 19.4%</span>
<span class="r">20시</span> -0.806% <span class="c">승률 12.1%</span>
<span class="r">21시</span> -0.716% <span class="c">승률 14.6%</span>
<span class="y">22시</span> -0.044%
<span class="r">23시</span> -0.409% <span class="c">승률 23.6%</span>
<span class="c">--------------------------------------------------</span>
<span class="w">19~23시 신규 진입 차단</span></code></pre>
</div>

## 반박해주는 도구

기분 좋은 발견은 아니다. 가중치를 넣을 때 나는 나름의 논리가 있었다. 더 눌린 종목이 더 크게 튄다는 것. 문장으로는 멀쩡하다.

그런데 그 논리가 이미 게이트를 통과한 표본 위에서는 뒤집혔다. 조건을 걸고 나면 남은 분포의 성격이 달라진다는 걸 계산해보기 전에는 몰랐다.

한계도 적어둔다. 최종 조합의 표본이 35~42건이고, 하루 종일 같은 데이터로 파라미터를 골랐다. 과적합이 섞여 있다. 낙폭 상한만 해도 오전 판단과 저녁 판단이 서로 뒤집혔다.

> 소로스는 자기가 언제 틀렸는지 알기 때문에 돈을 벌었다고 했다. 나한테 그걸 알려준 건 감이 아니라 상관계수 하나였다.

---

## 약어 풀이

\* 이 글에 나온 영어 약어를 풀어 둔다.

- **RSI** (Relative Strength Index): 상대강도지수. 일정 기간 평균 상승폭과 평균 하락폭의 비율을 0~100 으로 나타내 과매수·과매도를 재는 모멘텀 오실레이터.
