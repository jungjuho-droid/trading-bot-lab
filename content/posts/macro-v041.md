---
title: "[개발일지] MACRO.V041 — RSI 게이트 조정"
description: "MACRO.V041 · RSI Gate Tuning"
date: 2026-07-11T23:50:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "RSI", "Trading Bot Lab"]
summary: "RSI 게이트 조정. 병렬 실험기 77/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V041 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 30번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO041.py — 870줄</em></div>
<pre><code><span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO040.py (Sniper Edition)</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO041.py (Sniper + Accounting Fix)</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [V41 패치] 버전업 시 누적 데이터 증발 방지를 위해 상태 파일명 고정</span>
<span class="c">+ # [V40 패치] 악성 펌핑(설거지) 차단 듀얼 필터</span>
<span class="g">+ VERSION = "MACRO041.py"</span>
<span class="g">+ STATE_FILE = "UPBIT_ENGINE_STATE.json"</span>
<span class="g">+ MAX_IMPULSE_PCT = 0.30</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 870줄. 직전 버전 대비 +82/-15줄 — 중간 수정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **RSI 게이트 조정**이다. 당시 주석이 의도를 증언한다 — "[ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO041.py (Sniper + Accounting Fix)" / "=============================================================================="

## 소회

시장 전체를 읽고 들어가겠다는 야심이었다. 절반은 과욕이었고, 절반은 지금의 레짐 차단으로 살아남았다. 매크로 지표는 느리고 코인은 빠르다. 이 속도 차이를 극복하지 못한 것이 이 계열의 사인(死因)이다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 레이 달리오는 고통 더하기 반성이 진보라고 했다. 이 버전 번호가 곧 반성의 횟수다.

Developer: JH JEONG
