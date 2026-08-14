---
title: "[개발일지] MACRO.V035 — RSI 게이트 조정"
description: "MACRO.V035 · RSI Gate Tuning"
date: 2026-07-11T09:34:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "RSI", "Trading Bot Lab"]
summary: "RSI 게이트 조정. 병렬 실험기 70/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V035 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 23번째 기록이다. 원본 파일 시각이 소실된 EC2 복원본이라, 게시일은 버전 순서에 따라 시대 구간 안에 배정했다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO035.py — 744줄</em></div>
<pre><code><span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO034.py</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO034.py (Refactored)</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [레이스 컨디션 방지 메모리]</span>
<span class="g">+ VERSION = "MACRO034_REFACTORED.py"</span>
<span class="g">+ protected_slots = {}         # 매수 체결 대기 보호 (ticker -&gt; expire_timestamp)</span>
<span class="g">+ sold_protection_list = {}    # 매도 캐시 잔상 보호 (ticker -&gt; expire_timestamp)</span>
<span class="g">+ def save_state_sync():</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 744줄. 직전 버전 대비 +132/-59줄 — 중간 수정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **RSI 게이트 조정**이다. 당시 주석이 의도를 증언한다 — "[ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO034.py (Refactored)" / "=============================================================================="

## 소회

매크로 지표는 느리고 코인은 빠르다. 이 속도 차이를 극복하지 못한 것이 이 계열의 사인(死因)이다. 시장 전체를 읽고 들어가겠다는 야심이었다. 절반은 과욕이었고, 절반은 지금의 레짐 차단으로 살아남았다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 브루스 코브너는 자신이 틀릴 수 있는 지점을 미리 정해두는 것이 포지션의 전부라고 했다. 파라미터 파일이 곧 그 지점들의 목록이다.

Developer: JH JEONG
