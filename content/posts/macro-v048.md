---
title: "[개발일지] MACRO.V048 — RSI 게이트 조정"
description: "MACRO.V048 · RSI Gate Tuning"
date: 2026-07-12T21:06:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "RSI", "Trading Bot Lab"]
summary: "RSI 게이트 조정. 병렬 실험기 84/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V048 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 37번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO048.py — 807줄</em></div>
<pre><code><span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO047.py (Max Profit Swing Edition)</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO048.py (Triple Defense Edition)</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # 거시 스윙 특화 파라미터 (V44~V47 베이스 유지)</span>
<span class="c">+ # [V48 핵심 패치 1] 2단 트레일링 스탑 시스템</span>
<span class="g">+ VERSION = "MACRO048.py"</span>
<span class="g">+ MACRO_TREND_MA = 72             # 72시간(3일선) 거시 추세 안착 확인</span>
<span class="g">+ MIN_IMPULSE_PCT = 0.15          # 일주일 내 최소 15% 이상 상승 파동 발생</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 807줄. 직전 버전 대비 +124/-171줄 — 대수술이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **RSI 게이트 조정**이다. 당시 주석이 의도를 증언한다 — "[ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO048.py (Triple Defense Edition)" / "=============================================================================="

## 소회

매크로 지표는 느리고 코인은 빠르다. 이 속도 차이를 극복하지 못한 것이 이 계열의 사인(死因)이다. 시장 전체를 읽고 들어가겠다는 야심이었다. 절반은 과욕이었고, 절반은 지금의 레짐 차단으로 살아남았다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 브루스 코브너는 자신이 틀릴 수 있는 지점을 미리 정해두는 것이 포지션의 전부라고 했다. 파라미터 파일이 곧 그 지점들의 목록이다.

Developer: JH JEONG
