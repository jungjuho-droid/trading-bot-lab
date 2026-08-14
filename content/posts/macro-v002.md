---
title: "[개발일지] MACRO.V002 — 슬롯 운용 조정"
description: "MACRO.V002 · Slot Management"
date: 2026-07-08T10:47:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "슬롯 운용 조정. 병렬 실험기 49/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V002 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 2번째 기록이다. 원본 파일 시각이 소실된 EC2 복원본이라, 게시일은 버전 순서에 따라 시대 구간 안에 배정했다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO002.py — 519줄</em></div>
<pre><code><span class="r">- import datetime</span>
<span class="r">- import pyupbit</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [ MACRO002 1H BREAKOUT SWING ENGINE (COMPOUND INTEREST EDITION) ]</span>
<span class="c">+ # VER: v0.0.2 (MACRO-SWING + Total Equity 1/4 Sizing)</span>
<span class="g">+ import os</span>
<span class="g">+ import sys</span>
<span class="g">+ import uuid</span>
<span class="g">+ import jwt</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 519줄. 직전 버전 대비 +440/-238줄 — 사실상의 재작성이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **슬롯 운용 조정**이다. 당시 주석이 의도를 증언한다 — "==============================================================================" / "[ MACRO002 1H BREAKOUT SWING ENGINE (COMPOUND INTEREST EDITION) ]"

## 소회

매크로 지표는 느리고 코인은 빠르다. 이 속도 차이를 극복하지 못한 것이 이 계열의 사인(死因)이다. 시장 전체를 읽고 들어가겠다는 야심이었다. 절반은 과욕이었고, 절반은 지금의 레짐 차단으로 살아남았다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 레이 달리오는 고통 더하기 반성이 진보라고 했다. 이 버전 번호가 곧 반성의 횟수다.

Developer: JH JEONG
