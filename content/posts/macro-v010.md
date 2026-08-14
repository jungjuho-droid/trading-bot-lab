---
title: "[개발일지] MACRO.V010 — 스캐너 조정"
description: "MACRO.V010 · Scanner Pass"
date: 2026-07-08T22:56:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "스캐너", "Trading Bot Lab"]
summary: "스캐너 조정. 병렬 실험기 53/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V010 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 6번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO010.py — 547줄</em></div>
<pre><code><span class="r">- # [ MACRO009 1H BREAKOUT SWING ENGINE (ULTIMATE EDITION) ]</span>
<span class="r">- STATE_FILE = "MACRO009_STATE.json"</span>
<span class="c">+ # [ UPBIT HYBRID ENGINE MACRO010.py (ULTIMATE EDITION) ]</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # - 100% 잔고 동기화 (수동 매수 자동 슬롯 삽입 / 수동 매도 고아 슬롯 삭제)</span>
<span class="c">+ # - 1H 거래량 버그 픽스 및 정밀 스캔 엔진 / API Rate Limit 단일화</span>
<span class="g">+ STATE_FILE = "MACRO010_STATE.json"</span>
<span class="g">+ global global_state, active_slots</span>
<span class="g">+ krw_balance = 0.0</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 547줄. 직전 버전 대비 +74/-25줄 — 중간 수정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **스캐너 조정**이다. 당시 주석이 의도를 증언한다 — "[ UPBIT HYBRID ENGINE MACRO010.py (ULTIMATE EDITION) ]" / "=============================================================================="

## 소회

시장 전체를 읽고 들어가겠다는 야심이었다. 절반은 과욕이었고, 절반은 지금의 레짐 차단으로 살아남았다. 매크로 지표는 느리고 코인은 빠르다. 이 속도 차이를 극복하지 못한 것이 이 계열의 사인(死因)이다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 니콜라스 다바스는 시장에 있는 시간보다 기록을 들여다본 시간이 자신을 만들었다고 했다. 아카이브를 정리하는 지금이 꼭 그렇다.

Developer: JH JEONG
