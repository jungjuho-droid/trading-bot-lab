---
title: "[개발일지] VV202 — 청산 94건이 전부 하락장 진입이었다 (Dev Log VV202: All 94 Closed Trades Had Been Entered in a Downtrend)"
description: "그동안의 튜닝은 전부 하락장에서 덜 잃는 법이었다. Every parameter I had tuned was really just a way to lose less inside a downtrend."
date: 2026-08-04T13:13:00+09:00
draft: false
tags: ["개발일지", "자동매매", "업비트", "리스크관리"]
summary: "34승 60패, 합계 -346,965원. 승패를 가른 건 지표가 아니라 언제 들어갔느냐였다."
---

## 94건을 한 줄로 세워봤다

시드가 계속 깎이는 이유를 찾으려고 7월 25일 이후 청산이 끝난 거래를 전수로 봤다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>7/25 이후 청산 완결 94건 · 전수</em></div>
<pre><code><span class="r">전부 하락장 진입</span>
<span class="w">합계</span> <span class="r">-346,965원</span> <span class="c">· 34승 60패</span>
<span class="c">--------------------------------------------------</span>
<span class="c">MACD 양·음 가리지 않고 마이너스</span>
<span class="r">대조군이 없다 — 상승장 진입 표본이 0건</span></code></pre>
</div>

한 건도 예외가 없었다는 게 오히려 결론을 명확하게 했다. 진입 조건을 어떻게 다듬어도 표본 전체가 같은 국면 안에 있었다.

## 지금까지 고친 것들의 정체

이 사실을 알고 나서 그동안의 작업을 다시 보게 됐다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>VV193~201 에서 만진 것들</em></div>
<pre><code><span class="w">본전 사수 문턱</span> · <span class="w">중기추세 게이트</span> · <span class="w">RSI 45</span>
<span class="w">저점근접 3.0</span> · <span class="w">재장전 쿨다운</span> · <span class="w">연속 손절 락</span>
<span class="c">--------------------------------------------------</span>
<span class="y">전부 "하락장에서 덜 잃는 법" 이었다</span>
<span class="g">고칠 것은 값이 아니라 들어갈지 말지였다</span></code></pre>
</div>

## 국면이 돌 때까지 쉰다

`DIP_ALLOW_DOWNTREND` 를 껐다. BTC 4시간봉이 횡보나 상승으로 돌 때까지 신규 진입을 하지 않는다.

멈추는 건 진입뿐이다. 보유 종목의 손절, 본전 사수, 트레일링, 익절, 포트폴리오 수확은 전부 그대로 돈다. 터미널에는 `레짐: 하락장 차단` 으로 뜬다.

배포 전 무결성 검사와 게이트21은 통과했다. 총자산 3,246,529원이 거래소 값과 일치했다.

## 안 하는 것도 전략이다

파라미터를 만지는 일은 손에 잡힌다. 값을 바꾸고 시뮬레이션을 돌리면 숫자가 움직이고, 뭔가 한 것 같은 기분이 든다.

봇을 쉬게 하는 건 그런 감각이 없다. 화면에 아무 일도 안 일어난다. 그런데 94건이 알려준 건 그쪽이었다. **기대값이 음수인 국면에서는 거래 횟수를 줄이는 것이 유일하게 확실한 개선이다.** 튜닝으로 얻을 수 있는 건 그 안에서의 순위 조정뿐이다.

> 드러켄밀러는 확신이 없을 때 현금도 하나의 포지션이라고 했다. 봇에게는 그걸 가르치기가 더 쉬웠다. 사람은 쉬는 걸 손해로 느끼는데 코드는 안 그렇다.

---

## 약어 풀이

\* 이 글에 나온 영어 약어를 풀어 둔다.

- **MACD** (Moving Average Convergence Divergence): 이동평균 수렴확산. 장단기 지수이동평균의 차이로 추세의 방향과 힘을 재는 지표.
- **BTC** (Bitcoin): 비트코인. 이 블로그에서는 코인 시장 전체의 방향(레짐)을 재는 기준 자산.
- **RSI** (Relative Strength Index): 상대강도지수. 일정 기간 평균 상승폭과 평균 하락폭의 비율을 0~100 으로 나타내 과매수·과매도를 재는 모멘텀 오실레이터.
