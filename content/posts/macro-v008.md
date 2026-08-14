---
title: "[개발일지] MACRO.V008 — 웹소켓 안정화"
description: "MACRO.V008 · Websocket Hardening"
date: 2026-07-08T16:52:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "웹소켓", "Trading Bot Lab"]
summary: "웹소켓 안정화. 병렬 실험기 51/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V008 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 4번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO008.py — 560줄</em></div>
<pre><code><span class="r">- import jwt</span>
<span class="r">- import uuid</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [ MACRO008 1H BREAKOUT SWING ENGINE (PROFESSIONAL EDITION) ]</span>
<span class="c">+ # - 1H 래리 윌리엄스 (K=0.6) &amp; 정통 전고점 돌파 (Vol 1.5x)</span>
<span class="g">+ import websockets</span>
<span class="g">+ import sys</span>
<span class="g">+ import uuid</span>
<span class="g">+ import jwt</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 560줄. 직전 버전 대비 +505/-264줄 — 사실상의 재작성이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **웹소켓 안정화**이다. 당시 주석이 의도를 증언한다 — "==============================================================================" / "[ MACRO008 1H BREAKOUT SWING ENGINE (PROFESSIONAL EDITION) ]"

## 소회

시장 전체를 읽고 들어가겠다는 야심이었다. 절반은 과욕이었고, 절반은 지금의 레짐 차단으로 살아남았다. 매크로 지표는 느리고 코인은 빠르다. 이 속도 차이를 극복하지 못한 것이 이 계열의 사인(死因)이다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 마크 미너비니는 손실을 작게 유지하는 것이 공격의 전제라고 했다. 방어 코드가 늘어날수록 진입은 오히려 과감해졌다.

Developer: JH JEONG
