---
title: "[개발일지] MACRO.V054 — 텔레그램 리포트 정비"
description: "MACRO.V054 · Telegram Reporting"
date: 2026-07-13T12:17:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "알림", "Trading Bot Lab"]
summary: "텔레그램 리포트 정비. 병렬 실험기 89/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V054 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 42번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO054.py — 834줄</em></div>
<pre><code><span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO053.py (Abyss &amp; Quick-Cut Edition)</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO053 (Shadow 1.8% Edition)</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [신규] 섀도우 진입 파라미터</span>
<span class="g">+ VERSION = "MACRO053_SHADOW"</span>
<span class="g">+ SHADOW_DROP_TARGET = -0.018     # 1차 타점 도달 후 1.8% 추가 하락 대기</span>
<span class="g">+ SHADOW_CANCEL_BOUNCE = 0.010    # 대기 중 1.0% 반등 시 타겟 취소</span>
<span class="g">+ shadow_targets = {}     # 1.8% 대기열</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 834줄. 직전 버전 대비 +136/-115줄 — 대수술이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **텔레그램 리포트 정비**이다. 당시 주석이 의도를 증언한다 — "[ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO053 (Shadow 1.8% Edition)" / "=============================================================================="

## 소회

시장 전체를 읽고 들어가겠다는 야심이었다. 절반은 과욕이었고, 절반은 지금의 레짐 차단으로 살아남았다. 매크로 지표는 느리고 코인은 빠르다. 이 속도 차이를 극복하지 못한 것이 이 계열의 사인(死因)이다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 마크 더글러스는 시장이 아니라 자신의 규칙과 거래하라고 했다. 봇을 만든다는 건 그 규칙을 물리적으로 만드는 일이다.

Developer: JH JEONG
