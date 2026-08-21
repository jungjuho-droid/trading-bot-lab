---
title: "[개발일지] VV216 — 상승장을 26만 번 판정하고 한 번도 상승장이라 하지 않았다 (Dev Log VV216: The EMA That Was Never an EMA)"
description: "봉을 정확히 200개만 받아 EMA200이 단순평균으로 축퇴했다. 상승 판정 0건, 하락 판정 과다. 같은 조사에서 나온 게이트 완화안은 스윕이 기각했다. Feeding exactly 200 candles into a 200-period EMA collapsed it into a flat average."
date: 2026-08-20T23:55:00+09:00
draft: false
tags: ["개발일지", "자동매매", "업비트", "장애복기"]
summary: "레짐 판정 262,185회 중 상승장은 0건이었다. EMA200이 평활을 한 번도 돌지 않고 있었다."
---

## 26만 번 중 0건

레짐별 매매를 갈라 봤다. 하락장 진입 35건 -76,763원, 횡보장 48건 +137,507원. 차단 규칙은 옳았다. 그런데 상승장 칸이 비어 있었다. 진입이 없는 게 아니라 판정 자체가 없었다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>레짐 판정 분포 (누적 262,185회)</em></div>
<pre><code><span class="w">ranging</span>    166,392회
<span class="w">downtrend</span>   95,793회 <span class="y">전체의 36.5%</span>
<span class="w">uptrend</span>          <span class="r">0회</span> <span class="c">BTC 24h +4% 구간에도 '횡보'</span></code></pre>
</div>

상승 판정은 현재가가 EMA50 위, EMA50이 EMA200 위일 때 나온다. 뒷조건이 참인 적이 없었다.

## EMA가 EMA가 아니었다

EMA 함수는 앞의 n개로 시드를 만들고 남은 값을 평활한다. 그런데 4시간봉을 **정확히 200개** 받아 200기간 EMA에 넣고 있었다. 남은 값이 없으니 평활이 한 번도 돌지 않았고, 나온 숫자는 33일치 단순평균이었다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>실측 재현과 수정 후 (2026-08-20)</em></div>
<pre><code><span class="w">현재가</span>    98,456,000
<span class="w">EMA50</span>     91,580,744
<span class="w">구 EMA200</span> 92,149,045 <span class="r">평활 0회 = 200봉 전체 평균</span>
<span class="w">신 EMA200</span> 91,833,613 <span class="g">평활 200회 (봉 400개로 확장)</span>
<span class="c">--------------------------------------------------</span>
<span class="w">간격</span>      ema50-ema200 <span class="r">-567,626</span> <span class="c">→</span> <span class="g">-248,479</span> <span class="c">상승 판정 도달 가능</span></code></pre>
</div>

업비트는 1콜 200개가 상한이라 페이징으로 400개를 받게 고쳤다. 레짐 로그에 봉 개수도 찍어 재발을 눈으로 잡는다.

## 고치려던 것을 못 고쳤다

병목이 하나 더 나왔다. 상승장 탈락의 95.3%가 저점근접 게이트였다. 24시간 저점 대비 3% 이내를 요구하는데 상승장에선 모두가 그 위에 있다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>저점근접 단독탈락 104건 · 구간별 4시간 수익률</em></div>
<pre><code><span class="w">3~5%</span>   <span class="r">-0.90%</span> <span class="c">상승장 -0.44 / 그 이전 -1.11 (양쪽 다 음수)</span>
<span class="w">5~8%</span>   <span class="g">+1.52%</span>
<span class="w">8%↑</span>   <span class="y">-0.38%</span></code></pre>
</div>

임계를 올리면 좋은 구간만 취할 수 없다. 3%를 8%로 올리면 가장 나쁜 3~5% 구간이 함께 들어온다. 단일 임계로는 답이 안 나온다.

## 두 번 다 계기판이었다

어제는 서킷브레이커가 고점을 잊었고, 오늘은 EMA가 EMA가 아니었다. 둘 다 매매를 멈추지 않았고 에러도 남기지 않았다. 고장은 소리를 내지만 오차는 내지 않는다.

## 하루 뒤에 붙이는 정정

다음 날 수치를 다시 셌다. 결함은 실재했지만 **그 크기를 부풀려 썼다.**
BTC 4시간봉으로 같은 기간을 구/신 양쪽 돌려보니 판정이 거의 같았다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>같은 기간 재계산 (8/2~8/21, 4시간봉 120개)</em></div>
<pre><code><span class="w">구(200봉)</span>  하락 83 · 횡보 32 · <span class="y">상승 5</span>
<span class="w">신(400봉)</span>  하락 83 · 횡보 31 · <span class="y">상승 6</span>
<span class="c">--------------------------------------------------</span>
<span class="w">차이</span>      <span class="r">횡보→상승 1봉 (0.8%)</span> <span class="c">그게 전부였다</span></code></pre>
</div>

구 방식으로도 상승 판정은 나온다. 로그에 0건이던 건 그 기간 시장이 상승추세가
아니었기 때문이다. 고친 다음 날 상승 판정이 뜬 것 역시 시장이 바뀐 결과다.
고친 뒤에 좋아 보이는 현상을 수정의 효과로 적었다. 검산이 늦었다.

평활이 0회 도는 함수를 EMA라 부르던 것은 여전히 결함이고 수정도 유효하다.
틀린 건 효과 크기 서술이다.

> 에드워드 소프는 우위를 재는 도구가 정확한지부터 확인하라고 했다. 나는 게이트 임계를 만지기 전에 그 게이트가 참조하는 시장 판정이 맞는지를 물었어야 했다. 순서가 뒤집혀 있었다.

---

## 약어 풀이

\* 이 글에 나온 영어 약어를 풀어 둔다.

- **EMA** (Exponential Moving Average): 지수이동평균. 최근 값에 더 큰 가중치를 주는 이동평균으로, 앞부분 평균을 시드로 잡고 남은 값을 하나씩 평활해 구한다.
- **BTC** (Bitcoin): 비트코인. 이 봇은 BTC 4시간봉 추세로 시장 레짐을 판정한다.
- **MACD** (Moving Average Convergence Divergence): 이동평균수렴확산. 단기와 장기 EMA의 차이로 추세 전환을 보는 지표.
