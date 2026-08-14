---
title: "[개발일지] VVWAP.V118 — RSI 게이트 조정"
description: "VVWAP.V118 · RSI Gate Tuning"
date: 2026-07-21T09:06:00+09:00
draft: false
series: ["VVWAP기"]
tags: ["개발일지", "VVWAP기", "자동매매", "업비트", "RSI", "VWAP", "Trading Bot Lab"]
summary: "RSI 게이트 조정. VVWAP기 16/27."
---

## 배경

이 글은 VVWAP기 — VV의 기원의 한 페이지, VVWAP.V118 의 기록이다. 앵커드 VWAP 기반으로 재설계한 시기로, 현행 VV 넘버링이 여기서 시작된다. 이 시리즈에 보존된 27개 버전 가운데 17번째 기록이다. 원본 파일 시각이 소실된 EC2 복원본이라, 게시일은 버전 순서에 따라 시대 구간 안에 배정했다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>VV118.py — 891줄</em></div>
<pre><code><span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE VV116 (VWAP + Alt B + Momentum Out)</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE VV118 (VWAP + Alt B + Momentum Out)</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [VV118 전용 파라미터]</span>
<span class="c">+ # [VV117] 저변동성 구간 잦은 손절 완화용 시그마 배수</span>
<span class="g">+ VERSION = "VV118"</span>
<span class="g">+ STATE_FILE = "UPBIT_ENGINE_VV118_STATE.json"</span>
<span class="g">+ HARD_CUT_PCT = -0.06</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 891줄. 직전 버전 대비 +45/-25줄 — 중간 수정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **RSI 게이트 조정**이다. 당시 주석이 의도를 증언한다 — "[ 코어 파라미터 ] UPBIT HYBRID ENGINE VV118 (VWAP + Alt B + Momentum Out)" / "=============================================================================="

## 소회

이때부터 '기준선 대비 위치'로 생각하는 습관이 생겼다. 지금의 게이트 사고방식의 뿌리다. VV 라는 이름이 어디서 왔냐고 묻는다면 여기다 — VVWAP. 거래량 가중 평균가를 기준선 삼자는 발상이 그대로 이름이 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 윌리엄 오닐은 손절은 보험료라고 했다. 보험료 계산식을 고치는 날이 제일 많았다.

Developer: JH JEONG
