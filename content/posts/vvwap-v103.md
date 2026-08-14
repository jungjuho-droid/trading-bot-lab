---
title: "[개발일지] VVWAP.V103 — 하드컷 -3%와 BTC 낙폭 리밋"
description: "VVWAP.V103 · Hard-Cut −3% and the BTC Drop Limit"
date: 2026-07-16T16:48:00+09:00
draft: false
series: ["VVWAP기"]
tags: ["개발일지", "VVWAP기", "자동매매", "업비트", "VWAP", "Trading Bot Lab"]
summary: "하드컷 -3%와 BTC 낙폭 리밋. VVWAP기 2/27."
---

## 배경

이 글은 VVWAP기 — VV의 기원의 한 페이지, VVWAP.V103 의 기록이다. 앵커드 VWAP 기반으로 재설계한 시기로, 현행 VV 넘버링이 여기서 시작된다. 이 시리즈에 보존된 27개 버전 가운데 3번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>VV103.py — 769줄</em></div>
<pre><code><span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE VV101 (VWAP + Alt B + Momentum Out)</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE VV103 (VWAP + Alt B + Momentum Out)</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [VV103 전용 파라미터]</span>
<span class="c">+ # [ ACCOUNT CACHE ] 실계좌 동기화 및 예산 관리 (VV103 Full Sync 패치)</span>
<span class="g">+ VERSION = "VV103"</span>
<span class="g">+ STATE_FILE = "UPBIT_ENGINE_VV103_STATE.json"</span>
<span class="g">+ VOL_SURGE_MULTIPLIER = 1.5</span></code></pre>
</div>

## 무엇을 바꿨나

엔진 선언이 또렷해졌다 — 'VWAP + Alt B + Momentum Out'. 그리고 두 개의 방어선: `HARD_CUT_PCT = -0.03`(하드컷 -3.00%)과 **`BTC_DROP_LIMIT = -0.02`** — BTC가 -2.00% 급락하면 알트 진입을 막는다. 시장 전체의 상태로 개별 진입을 차단하는 이 발상이, 현행 'BTC 4시간봉 하락장 레짐 차단'의 직계 조상이다. `VOL_SURGE_MULTIPLIER = 1.5`로 거래량 급증 판정도 들어왔다.

## 소회

개별 종목이 아니라 시장의 안색을 먼저 살핀다 — 이 한 줄의 파라미터가 훗날 7주 연속 손실을 끊는 레짐 차단으로 자란다.

> 윌리엄 오닐은 손절은 보험료라고 했다. 보험료 계산식을 고치는 날이 제일 많았다.

Developer: JH JEONG
