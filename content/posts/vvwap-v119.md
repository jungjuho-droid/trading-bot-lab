---
title: "[개발일지] VVWAP.V119 — RSI 게이트 조정"
description: "VVWAP.V119 · RSI Gate Tuning"
date: 2026-07-21T13:55:00+09:00
draft: false
series: ["VVWAP기"]
tags: ["개발일지", "VVWAP기", "자동매매", "업비트", "RSI", "VWAP", "Trading Bot Lab"]
summary: "RSI 게이트 조정. VVWAP기 17/27."
---

## 배경

이 글은 VVWAP기 — VV의 기원의 한 페이지, VVWAP.V119 의 기록이다. 앵커드 VWAP 기반으로 재설계한 시기로, 현행 VV 넘버링이 여기서 시작된다. 이 시리즈에 보존된 27개 버전 가운데 18번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>VV119.py — 896줄</em></div>
<pre><code><span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE VV118 (VWAP + Alt B + Momentum Out)</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE VV119 (VWAP + Alt B + Momentum Out)</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [VV119 전용 파라미터]</span>
<span class="c">+ # [VV118] 손절/익절 최소폭 설계 (하드컷 -6%, 동적손절 최소 -4%)</span>
<span class="g">+ VERSION = "VV119"</span>
<span class="g">+ STATE_FILE = "UPBIT_ENGINE_VV119_STATE.json"</span>
<span class="g">+ TP1_SIGMA_MULT, TP1_MIN_PCT = 1.5, 0.09</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 896줄. 직전 버전 대비 +20/-15줄 — 미세 조정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **RSI 게이트 조정**이다. 당시 주석이 의도를 증언한다 — "[ 코어 파라미터 ] UPBIT HYBRID ENGINE VV119 (VWAP + Alt B + Momentum Out)" / "=============================================================================="

## 소회

이때부터 '기준선 대비 위치'로 생각하는 습관이 생겼다. 지금의 게이트 사고방식의 뿌리다. VV 라는 이름이 어디서 왔냐고 묻는다면 여기다 — VVWAP. 거래량 가중 평균가를 기준선 삼자는 발상이 그대로 이름이 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 제시 리버모어는 시장은 결코 틀리지 않고 의견만 틀린다고 했다. 봇의 의견을 고치는 일, 그게 버전업이다.

Developer: JH JEONG
