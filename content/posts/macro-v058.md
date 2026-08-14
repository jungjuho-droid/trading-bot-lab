---
title: "[개발일지] MACRO.V058 — RSI 게이트 조정"
description: "MACRO.V058 · RSI Gate Tuning"
date: 2026-07-14T09:26:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "RSI", "Trading Bot Lab"]
summary: "RSI 게이트 조정. 병렬 실험기 93/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V058 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 46번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO058.py — 927줄</em></div>
<pre><code><span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO057 (Panic Sell Defender)</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO058 (Non-Blocking Velocity Edition)</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # 섀도우 진입 및 투매 방어 파라미터</span>
<span class="c">+ # [복구] 오래된 섀도우 타겟 정리 (12시간 경과 시)</span>
<span class="g">+ VERSION = "MACRO058"</span>
<span class="g">+ SHADOW_DROP_TARGET = -0.018</span>
<span class="g">+ SHADOW_CANCEL_BOUNCE = 0.010</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 927줄. 직전 버전 대비 +43/-19줄 — 중간 수정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **RSI 게이트 조정**이다. 당시 주석이 의도를 증언한다 — "[ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO058 (Non-Blocking Velocity Edition)" / "=============================================================================="

## 소회

시장 전체를 읽고 들어가겠다는 야심이었다. 절반은 과욕이었고, 절반은 지금의 레짐 차단으로 살아남았다. 매크로 지표는 느리고 코인은 빠르다. 이 속도 차이를 극복하지 못한 것이 이 계열의 사인(死因)이다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 마크 미너비니는 손실을 작게 유지하는 것이 공격의 전제라고 했다. 방어 코드가 늘어날수록 진입은 오히려 과감해졌다.

Developer: JH JEONG
