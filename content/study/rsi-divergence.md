---
title: "RSI 다이버전스, 파인스크립트 한 장으로 봇을 만들다 (RSI Divergence Oscillator: Building a Bot From a Single Pine Script)"
description: "RSI DIVERGENCE · From One Pine Script to a Working Trading Bot"
date: 2026-08-14T19:00:00+09:00
draft: false
tags: ["지표스터디", "기술적지표", "자동매매", "백테스트"]
markets: ["crypto"]
summary: "빠른 RSI(5)에서 느린 RSI(14)를 뺀 오실레이터. 트레이딩뷰 지표 한 장을 받아서, 신호 설계 → 파이썬 이식 → 게이트 → 집행 → 검증까지 — 봇 한 대가 되기까지의 전 공정을 기록한다."
---

## 이름이 내용을 배신하는 지표 하나

트레이딩뷰에서 지표 하나를 받아놓고 며칠을 들여다봤다. 이름은 RSI Divergence. 이름값을 하는 물건인지 아직 확신이 안 서는데, 일단 코드부터 그대로 올려놓고 시작하는 게 낫겠다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>TradingView — RSI Divergence (Pine Script 원문)</em></div>
<pre><code><span class="c">study(title="RSI Divergence", shorttitle="RSI Divergence")</span>
<span class="g">src_fast = close, len_fast = input(5,  minval=1, title="Length Fast RSI")</span>
<span class="g">src_slow = close, len_slow = input(14, minval=1, title="Length Slow RSI")</span>
<span class="w">up_fast   = rma(max(change(src_fast), 0), len_fast)</span>
<span class="w">down_fast = rma(-min(change(src_fast), 0), len_fast)</span>
<span class="w">rsi_fast  = down_fast == 0 ? 100 : up_fast == 0 ? 0 : 100 - (100 / (1 + up_fast / down_fast))</span>
<span class="w">up_slow   = rma(max(change(src_slow), 0), len_slow)</span>
<span class="w">down_slow = rma(-min(change(src_slow), 0), len_slow)</span>
<span class="w">rsi_slow  = down_slow == 0 ? 100 : up_slow == 0 ? 0 : 100 - (100 / (1 + up_slow / down_slow))</span>
<span class="y">divergence = rsi_fast - rsi_slow</span>
<span class="y">plotdiv = plot(divergence, color = divergence > 0 ? lime : red, linewidth = 2)</span>
<span class="c">band = hline(0)</span></code></pre>
</div>

구조 자체는 간결하다. 기간 5짜리 빠른 RSI와 기간 14짜리 느린 RSI를 각각 와일더 방식(rma)으로 구하고, 빠른 쪽에서 느린 쪽을 뺀 차이를 0선 위아래 히스토그램으로 그린다. 0 위면 라임색, 아래면 빨강. 여기서 걸린다. 이름은 다이버전스인데, 교과서가 말하는 '가격 고점과 지표 고점의 엇갈림'을 자동으로 잡아주는 물건은 아니다. 실제로 그리는 건 두 RSI의 스프레드, 그러니까 모멘텀의 가속도 쪽이다. 지표를 봇에 넣을 거면 이름 말고 수식이 하는 일을 봐야 한다.

## 지표의 뼈대: 빠른 놈에서 느린 놈을 뺀다

RSI(14)는 최근 14봉의 방향성 요약이고, RSI(5)는 최근 5봉의 방향성 요약이다. 둘의 차이가 양수면 단기 모멘텀이 중기 모멘텀보다 강하다는 얘기가 된다. 하락하던 종목이 바닥을 다지고 돌기 시작하면 느린 RSI가 아직 누워 있는 동안 빠른 RSI가 먼저 고개를 든다. 느린 쪽이 여전히 과매도 언저리에 머무는 동안 빠른 쪽만 먼저 방향을 틀기 때문에, 그 시차가 그대로 스프레드가 되어 오실레이터를 0선 위로 밀어 올린다. 반대로 상승이 지치면 빠른 쪽이 먼저 꺾여 0선 아래로 내려간다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>divergence = rsi(5) - rsi(14) — 반등 초입의 형태</em></div>
<pre><code><span class="c">   값                                          해석</span>
<span class="g"> +6 │                    ██                  단기가 중기를 크게 추월</span>
<span class="g"> +4 │                  ████                  (반등 가속 구간)</span>
<span class="g"> +2 │                ██████</span>
<span class="w">  0 ┼────────▁▁▁▁──────────────  ◀ 진입 후보: 0선 상향 돌파</span>
<span class="r"> -2 │      ████</span>
<span class="r"> -4 │    ██████                              단기가 중기보다 약함</span>
<span class="r"> -6 │  ████████                              (하락 진행 구간)</span>
<span class="c">    └──── 과거 ────────────── 현재 ────▶</span>
<span class="y">  핵심: 느린 RSI 가 바닥에 있는 동안 빠른 RSI 가 먼저 돈다</span></code></pre>
</div>

이 그림을 보고 좀 설렜다. 내 봇 철학과 같은 동네에 사는 지표라서. 현행 전략은 과매도 눌림목 반등이다. 빠진 걸 사되 빠지는 중인 놈은 피하고 돌기 시작한 놈을 산다. 문제는 '돌기 시작했다'를 어떻게 수치로 못 박느냐인데, 이 오실레이터의 0선 상향 돌파가 그 정의 후보로 딱 들어맞는다. 느린 RSI가 과매도라는 맥락을 깔고, 빠른 RSI와의 스프레드가 타이밍을 잡는 이중 구조.

## 공식을 코드로 옮기면서

봇은 파이썬으로 돈다. 그러니 첫 공정은 이식이다. 여기서 초보 시절의 나를 몇 번이나 넘어뜨린 함정이 나온다. rma는 그냥 이동평균이 아니다. 와일더의 rma는 지수평활의 일종이고, pandas로는 `ewm(alpha=1/len)`이 맞다. `rolling(len).mean()`으로 옮기면 트레이딩뷰와 값이 몇 포인트씩 어긋난다. 그 차이가 0선 근처에서 신호의 유무를 갈라 버린다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>python — pine 의 rma 를 그대로 재현하는 이식</em></div>
<pre><code><span class="c"># rma(x, n) == Wilder smoothing == EMA(alpha=1/n), TV는 첫 값을 SMA로 시드</span>
<span class="g">def rma(s, n):</span>
<span class="g">    return s.ewm(alpha=1/n, min_periods=n, adjust=False).mean()</span>
<span class="c"># change(close) == close.diff()</span>
<span class="g">def rsi_wilder(close, n):</span>
<span class="g">    d    = close.diff()</span>
<span class="g">    up   = rma(d.clip(lower=0), n)</span>
<span class="g">    down = rma(-d.clip(upper=0), n)</span>
<span class="g">    return 100 - 100 / (1 + up / down)      <span class="c"># down==0 이면 inf→100 으로 수렴</span></span>
<span class="y">rsi_fast   = rsi_wilder(close, 5)</span>
<span class="y">rsi_slow   = rsi_wilder(close, 14)</span>
<span class="y">divergence = rsi_fast - rsi_slow</span>
<span class="r"># 주의 1: 마지막 봉이 진행 중이면 계산에서 제외한다 (완성봉 원칙)</span>
<span class="r"># 주의 2: 워밍업 — 최소 len_slow*5 봉을 채우기 전의 값은 버린다</span></code></pre>
</div>

주석에 달린 두 줄은 장식이 아니다. 흉터다. 진행 중인 봉을 계산에 넣으면 오실레이터가 초 단위로 0선을 들락거리고, 봇은 같은 자리에서 사고팔기를 반복한다. 내 봇이 완성봉만 쓰는 건 그 꼴을 본 뒤부터다. 워밍업도 같은 얘기다. 지수평활은 초기 구간에 시드의 흔적이 남아서, 데이터 로딩 직후의 값으로 판정하면 재시작할 때마다 다른 신호를 내는 봇이 된다. 같은 입력에 어제와 다른 답을 내놓는 봇은 성적이 좋든 나쁘든 그 성적을 자기 것이라고 주장할 수 없다.

## 신호 설계: 오실레이터를 매매 규칙으로 바꾸기

이식이 끝났다고 신호가 생긴 건 아니다. "0선을 상향 돌파하면 산다"는 문장은 그럴듯한데, 그대로 코드에 넣으면 첫날부터 0선 근처의 톱니를 만난다. 스프레드가 0 언저리에서 잘게 떨면 돌파가 하루에도 수십 번 찍힌다. 그래서 설계 단계에서 최소 세 가지를 정해야 한다.

첫째, 히스테리시스. 0선 하나로 끝내지 않고 진입선과 이탈선을 나눈다. "-2 아래를 찍은 뒤 +2를 상향 돌파할 때만 트리거" 같은 식이면, 한 번 발동한 신호가 다시 무장되려면 오실레이터가 충분히 내려갔다 와야 한다. 둘째, 맥락 조건. 스프레드의 0선 돌파는 상승 중간의 잔출렁임에서도 나온다. 내가 잡고 싶은 건 과매도에서의 반등이니, 느린 RSI가 낮다는 조건을 같이 건다. 셋째, 확인 봉 수. 돌파 봉에서 바로 들어갈지, 한 봉 유지되는지 보고 들어갈지. 빠르면 휩쏘를 먹고 늦으면 이익의 앞부분을 버린다. 이건 아직도 어느 쪽이 나은지 모르겠다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>signal design — 문장을 판정식으로 바꾸는 과정</em></div>
<pre><code><span class="c"># "반등 초입을 산다" 를 3개의 결정으로 분해</span>
<span class="w">[1] 트리거   divergence 가 arm선(-B) 아래 무장 후 fire선(+B) 상향 돌파</span>
<span class="w">[2] 맥락     rsi_slow <= OS  (과매도 국면에서만 트리거 유효)</span>
<span class="w">[3] 확인     돌파 후 confirm_bars 봉 유지 시 진입 (0 = 즉시)</span>
<span class="y">파라미터 후보:  B ∈ {0, 1, 2, 3}   OS ∈ {35, 40, 45, 50}   confirm ∈ {0, 1}</span>
<span class="c"># 값을 지금 정하지 않는 이유 — 아래 '검증 계획' 참조.</span>
<span class="g">참고: 내 봇의 과매도 기준 RSI 45 는 8.9일 매매기록 전수 스윕의 결과값이다 (VV201)</span>
<span class="g">      교과서의 30 이 아니라 45 가 된 과정은 지난 RSI 편에서 다뤘다</span></code></pre>
</div>

눈여겨볼 대목은 파라미터 후보에 값을 아직 안 박아놨다는 점이다. B=2가 좋아 보이고 OS=45가 손에 익었지만, '좋아 보인다'는 이 스터디의 금지어다. 후보군만 깔아두고 채택은 측정에 맡긴다. 설계자가 할 일은 정답을 찍는 쪽이 아니다. 실험이 가능한 형태로 질문을 좁히는 쪽이다.

## 봇의 골격: 지표는 부품이고, 봇은 공정이다

여기까지가 지표 얘기고, 지금부터가 봇 얘기다. 461개 버전을 만들며 산 가장 비싼 교훈을 한 줄로 줄이면 이렇다. 지표는 봇의 10%다. 나머지 90%는 데이터의 무결성, 집행의 정확성, 잃지 않는 구조가 나눠 갖는다. 신호가 아무리 예뻐도 체결 확인을 안 하는 봇은 유령 포지션을 만들고(VANA 사건), 원장 대조를 안 하는 봇은 자기 손익을 모른 채 달린다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>bot pipeline — 지표에서 계좌까지, 한 신호의 일생</em></div>
<pre><code><span class="b">  ① 수집     거래소 캔들/호가 수신 (웹소켓 + REST 폴백, 재연결 백오프)</span>
<span class="b">  ② 확정     완성봉만 확정 큐로 — 진행봉은 지표 계산 금지</span>
<span class="y">  ③ 지표     rsi_fast / rsi_slow / divergence 갱신 (워밍업 구간 폐기)</span>
<span class="y">  ④ 게이트   트리거 + 맥락 + 유동성/레짐 게이트 일괄 판정  ◀ 지표는 여기 한 칸</span>
<span class="w">  ⑤ 사이징   슬롯 예산 = 가용 현금의 고정 비중 (몰빵 구조적 차단)</span>
<span class="w">  ⑥ 집행     지정가 → 체결 폴링으로 확인 → 미체결 처리 명시</span>
<span class="g">  ⑦ 청산     손절 / 본전 사수(SAFE) / 포트폴리오 익절 — 진입과 독립된 엔진</span>
<span class="g">  ⑧ 대조     거래소 원장과 손익·잔고 대조, 불일치 시 배포/운용 중단</span>
<span class="c">  지표 교체 = ③④ 만 갈아끼운다. 나머지 공정은 지표와 무관하게 재사용.</span></code></pre>
</div>

이 구조의 요점은 ③④만 오늘의 지표로 갈아끼우면 나머지가 통째로 재사용된다는 데 있다. 내 봇이 돌파 전략에서 눌림목 전략으로 갈아타는 데(VV168) 하루면 됐던 것도 이 분리 덕이다. 지표 하나 바꾸려는데 봇 전체를 새로 짜야 한다면 그건 지표 문제가 아니라 아키텍처 문제다.

그리고 ④의 게이트. 오실레이터 트리거 하나로 진입을 정하는 봇은 오래 못 간다. 게이트를 10개나 두는 건 지표마다 못 보는 사각이 다르기 때문이다. RSI 스프레드는 가격의 모멘텀만 본다. 그 종목의 거래대금이 말라 있는지, 호가 한 칸이 가격의 몇 퍼센트인지, 시장 전체가 하락 레짐인지는 모른다. 실측 예를 들면 저가 코인은 호가 한 칸이 0.2%를 넘어서 청산선이 호가 사이에 끼는 일이 있었고(본전 청산 27건, VV206), 그 뒤 호가단위/가격 비율 게이트(VV208)가 생겼다. 오늘의 오실레이터를 실전에 올린다면 유동성 게이트와 BTC 4시간봉 레짐 차단은 최소한 같이 세워야 한다. 과매도 반등 전략의 최대 리스크는 하락 추세의 중간을 바닥으로 착각하는 것인데, 종목 레벨 지표로는 그게 안 걸러진다.

## 검증 계획: 숫자는 측정한 뒤에 적는다

마지막 공정이고, 이 블로그가 있는 이유이기도 하다. 위에서 설계한 파라미터(B, OS, confirm, len_fast, len_slow)는 전부 후보 상태다. 이걸 채우는 절차는 내 봇의 현행 규율을 그대로 따른다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>validation plan — VV201 방법론을 그대로 적용한 스윕 설계</em></div>
<pre><code><span class="c">  축            후보값                 채택 기준</span>
<span class="w">  len_fast     3 / 5 / 7              ┐</span>
<span class="w">  len_slow     10 / 14 / 21           │  ① 축별 전수 스윕</span>
<span class="w">  밴드 B       0 / 1 / 2 / 3          │  ② 상위 조합 재검증</span>
<span class="w">  과매도 OS    35 / 40 / 45 / 50      │  ③ 기간 반분 안정성 체크</span>
<span class="w">  confirm      0 / 1                  ┘</span>
<span class="y">  목적함수: 평균수익 · 승률 · 손절권 진입률 — 셋 다 개선(파레토 우세)일 때만 채택</span>
<span class="y">  한 축이 좋아도 손절권이 나빠지면 기각 (예: VV201 에서 낙폭 -2.5 기각 사유)</span>
<span class="r">  이 표의 결과 칸이 비어 있는 이유: 아직 측정 전이기 때문이다.</span>
<span class="r">  측정 전의 숫자를 적는 순간, 이 스터디는 광고가 된다.</span></code></pre>
</div>

스윕에서 제일 강조하고 싶은 건 목적함수다. 수익률 한 줄만 보고 고르면 반드시 과적합된 값이 뽑힌다. 내 봇의 VV201 스윕이 파레토 우세를, 그러니까 수익과 승률과 손절권 진입률이 동시에 개선되는 값만 채택하는 조건을 걸어둔 것도 그래서다. 기간을 반으로 갈라 앞뒤 양쪽에서 성립하는지 본 것도 같은 이유. 그리고 스윕으로 뽑은 값에도 유효기간이 붙는다. 같은 봇에서 RSI 문턱이 50으로 측정됐다가(VV195) 거래량 게이트 하나가 들어온 뒤 45로 다시 측정된(VV201) 전례가 있다. 게이트 조합이 바뀌면 개별 지표의 최적점도 따라 움직인다. 오늘의 오실레이터를 어느 봇에 얹느냐에 따라 B와 OS의 정답이 달라진다는 얘기다. 그래서 남의 백테스트 결과는, 내 것이 아니다.

## 소회

파인스크립트 열두 줄을 받아서 여기까지 끌고 왔다. 수식 해석, 이식의 함정, 신호 설계의 3분해, 공정 분리, 게이트, 스윕 계획. 지표 하나를 봇으로 만드는 데 필요한 공정이 대충 이만큼이다. 이 공정표 자체가 461개 버전의 수업료로 산 물건이라는 생각이 든다. 예전의 나는 ③에서 곧장 ⑥으로 건너뛰었고, 그 지름길 값을 계좌로 냈다.

빠른 RSI에서 느린 RSI를 뺀다는 발상은 여전히 예쁘다. 과매도의 맥락과 반등의 타이밍을 지표 하나가 같이 들고 있으니까. 그런데 이게 내 봇의 열한 번째 게이트가 될지는 지금 모른다. 모른다고 적어두는 게 이 스터디의 규칙이다. 다음 단계는 정해져 있다. 매매기록 위에서 전수 스윕을 돌리고, 파레토 우세가 나오면 채택하고, 안 나오면 이 글이 그 지표의 부검 보고서가 된다. 어느 쪽이든 기록은 남는다.

> 짐 사이먼스의 르네상스가 지킨 철칙은 '모델이 시키는 대로 하라'였다고 한다. 그 말에는 숨은 전제가 있다. 시키는 대로 해도 될 만큼 모델을 검증해 뒀다는 것. 내가 믿어야 할 대상은 지표 자체보다 그 지표를 검증한 절차 쪽이고, 열두 줄의 파인스크립트와 한 대의 봇 사이에 놓인 거리가 딱 그만큼이다.

---

## 약어 풀이

\* 이 글에 나온 영어 약어를 풀어 둔다.

- **RSI** (Relative Strength Index): 상대강도지수. 일정 기간 평균 상승폭과 평균 하락폭의 비율을 0~100 으로 나타내 과매수·과매도를 재는 모멘텀 오실레이터.
- **SMA** (Simple Moving Average): 단순이동평균. 기간 안의 가격을 같은 가중치로 평균한 값.
- **EMA** (Exponential Moving Average): 지수이동평균. 최근 가격에 더 큰 가중치를 두어 SMA 보다 빠르게 반응하는 이동평균.
- **BTC** (Bitcoin): 비트코인. 이 블로그에서는 코인 시장 전체의 방향(레짐)을 재는 기준 자산.
- **REST** (Representational State Transfer): HTTP 요청·응답으로 자원을 주고받는 API 설계 방식. 거래소 API 대부분이 이 형태다.
- **OS** (Oversold): 과매도. 봇 코드에서는 RSI 과매도 문턱값의 변수명으로 쓴다.
