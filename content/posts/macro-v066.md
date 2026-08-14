---
title: "[개발일지] MACRO.V066 — RSI 게이트 조정"
description: "MACRO.V066 · RSI Gate Tuning"
date: 2026-07-15T09:44:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "RSI", "Trading Bot Lab"]
summary: "RSI 게이트 조정. 병렬 실험기 101/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V066 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 54번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO066.py — 942줄</em></div>
<pre><code><span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO065 (Hyper Agile Shadow Edition)</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO066 (Instant Strike Edition)</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [V66 패치] 섀도우 진입 대기 완전히 제거 (0.0% 즉시 진입)</span>
<span class="c">+ # [대책 1] 절대 윗꼬리 폭격 필터 (Absolute Wick Filter)</span>
<span class="g">+ VERSION = "MACRO066"</span>
<span class="g">+ SHADOW_DROP_TARGET = 0.000</span>
<span class="g">+ "조건2 : 섀도우 대기 제거 (타점 도달 시 즉시 매수)\n"</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 942줄. 직전 버전 대비 +11/-11줄 — 미세 조정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **RSI 게이트 조정**이다. 당시 주석이 의도를 증언한다 — "[ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO066 (Instant Strike Edition)" / "=============================================================================="

## 소회

매크로 지표는 느리고 코인은 빠르다. 이 속도 차이를 극복하지 못한 것이 이 계열의 사인(死因)이다. 시장 전체를 읽고 들어가겠다는 야심이었다. 절반은 과욕이었고, 절반은 지금의 레짐 차단으로 살아남았다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 폴 튜더 존스는 어제의 가격이 아니라 오늘의 리스크를 보라고 했다. 패치는 언제나 오늘의 리스크가 시켰다.

Developer: JH JEONG
