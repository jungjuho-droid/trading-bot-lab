---
title: "[개발일지] MACRO.V053 — RSI 게이트 조정"
description: "MACRO.V053 · RSI Gate Tuning"
date: 2026-07-13T09:15:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "RSI", "Trading Bot Lab"]
summary: "RSI 게이트 조정. 병렬 실험기 88/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V053 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 41번째 기록이다. 원본 파일 시각이 소실된 EC2 복원본이라, 게시일은 버전 순서에 따라 시대 구간 안에 배정했다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO053.py — 813줄</em></div>
<pre><code><span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO052.py (Deep-Knee Edition)</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO053.py (Abyss &amp; Quick-Cut Edition)</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # 악성 윗꼬리 필터 (깊은 타점을 위해 85% 완화 상태 유지)</span>
<span class="c">+ # [V53 핵심 패치] 손절 폭 2% 칼손절 적용</span>
<span class="g">+ VERSION = "MACRO053.py"</span>
<span class="g">+ MAX_STOP_LOSS = -0.020</span>
<span class="g">+ legacy_files = ["MACRO050_STATE.json", "MACRO051_STATE.json", "MACRO052_STATE.json"]</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 813줄. 직전 버전 대비 +31/-31줄 — 중간 수정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **RSI 게이트 조정**이다. 당시 주석이 의도를 증언한다 — "[ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO053.py (Abyss & Quick-Cut Edition)" / "=============================================================================="

## 소회

시장 전체를 읽고 들어가겠다는 야심이었다. 절반은 과욕이었고, 절반은 지금의 레짐 차단으로 살아남았다. 매크로 지표는 느리고 코인은 빠르다. 이 속도 차이를 극복하지 못한 것이 이 계열의 사인(死因)이다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 에드 세이코타는 규칙을 지키는 것보다 지킬 수 있는 규칙을 만드는 게 먼저라고 했다. 파라미터 손질은 그 '지킬 수 있는'을 찾는 과정이었다.

Developer: JH JEONG
