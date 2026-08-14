---
title: "[개발일지] VVWAP.V130 — 파이썬 VVWAP의 마지막"
description: "VVWAP.V130 · The Last Python VVWAP"
date: 2026-07-24T12:11:00+09:00
draft: false
series: ["VVWAP기"]
tags: ["개발일지", "VVWAP기", "자동매매", "업비트", "VWAP", "Trading Bot Lab"]
summary: "파이썬 VVWAP의 마지막. VVWAP기 26/27."
---

## 배경

이 글은 VVWAP기 — VV의 기원의 한 페이지, VVWAP.V130 의 기록이다. 앵커드 VWAP 기반으로 재설계한 시기로, 현행 VV 넘버링이 여기서 시작된다. 이 시리즈에 보존된 27개 버전 가운데 27번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>VV130.py — 1,231줄</em></div>
<pre><code><span class="r">- VERSION = "VV129"</span>
<span class="r">- RANGING_MIN_SCORE = 80          # 박스권 진입 기준 (더 엄격)</span>
<span class="g">+ VERSION = "VV130"</span>
<span class="g">+ RANGING_MIN_SCORE = 75          # 박스권 진입 기준 (더 엄격) [VV130 조정]</span>
<span class="g">+ """MACD (Moving Average Convergence Divergence) 계산 [VV130 수정]"""</span>
<span class="g">+ if len(prices) &lt; slow + signal_period - 1: return None, None, None</span>
<span class="g">+ macd_lines = []</span>
<span class="g">+ for i in range(slow, len(prices)):</span>
<span class="g">+ ema_f = calculate_ema(prices[:i+1], fast)</span></code></pre>
</div>

## 무엇을 바꿨나

vv141 이전, 혼자 짜던 시대의 마지막 보존본이다. 1,231줄. 이 코드가 곧 모듈 분리의 원료가 된다 — 몇 주 뒤 이 파일의 로직들은 vv_state/core/scan/exec 모듈로 해체되고, 커밋 로그에는 처음으로 다른 이름(Claude)이 등장한다. 한 시대가 여기서 접힌다.

## 소회

이 파일을 저장할 때는 몰랐다. 다음 세대부터 개발의 방식 자체가 바뀐다는 걸. 혼자 쓰는 마지막 문장은 늘 평범하다.

> 워런 버핏은 썰물이 되면 누가 벌거벗고 수영했는지 드러난다고 했다. 안전장치는 밀물일 때 만들어야 한다 — 이 버전처럼.

Developer: JH JEONG
