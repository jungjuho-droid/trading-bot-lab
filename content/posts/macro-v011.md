---
title: "[개발일지] MACRO.V011 — 슬롯 운용 조정"
description: "MACRO.V011 · Slot Management"
date: 2026-07-09T09:58:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "슬롯 운용 조정. 병렬 실험기 54/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V011 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 7번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO011.py — 562줄</em></div>
<pre><code><span class="r">- # [ UPBIT HYBRID ENGINE MACRO010.py (ULTIMATE EDITION) ]</span>
<span class="r">- # - 1H 거래량 버그 픽스 및 정밀 스캔 엔진 / API Rate Limit 단일화</span>
<span class="c">+ # [ UPBIT HYBRID ENGINE MACRO011.py (ULTIMATE 2H EDITION) ]</span>
<span class="c">+ # - 2H(120분) 로컬 캔들 합성기 이식 (업비트 정책 위회 정밀 타점)</span>
<span class="c">+ # ⚔️ 진입 파라미터 (2H 합성 스윙)</span>
<span class="c">+ # [GHOST POP] 업비트 잔고엔 없는데 봇 슬롯에 남아있는 고아 슬롯 삭제</span>
<span class="g">+ STATE_FILE = "MACRO011_STATE.json"</span>
<span class="g">+ df = await request_api('GET', 'candles/minutes/60', is_private=False, params={'market':...</span>
<span class="g">+ if not df or len(df) &lt; 40: continue</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 562줄. 직전 버전 대비 +42/-27줄 — 중간 수정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **슬롯 운용 조정**이다. 당시 주석이 의도를 증언한다 — "[ UPBIT HYBRID ENGINE MACRO011.py (ULTIMATE 2H EDITION) ]" / "- 2H(120분) 로컬 캔들 합성기 이식 (업비트 정책 위회 정밀 타점)"

## 소회

시장 전체를 읽고 들어가겠다는 야심이었다. 절반은 과욕이었고, 절반은 지금의 레짐 차단으로 살아남았다. 매크로 지표는 느리고 코인은 빠르다. 이 속도 차이를 극복하지 못한 것이 이 계열의 사인(死因)이다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 윌리엄 오닐은 손절은 보험료라고 했다. 보험료 계산식을 고치는 날이 제일 많았다.

Developer: JH JEONG
