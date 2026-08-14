---
title: "[개발일지] MACRO.V047 — RSI 게이트 조정"
description: "MACRO.V047 · RSI Gate Tuning"
date: 2026-07-12T18:03:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "RSI", "Trading Bot Lab"]
summary: "RSI 게이트 조정. 병렬 실험기 83/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V047 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 36번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO047.py — 854줄</em></div>
<pre><code><span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO046.py (Turbo Swing Edition)</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO047.py (Max Profit Swing Edition)</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [V44 유지] 168시간 액티브 스윙 특화 파라미터</span>
<span class="c">+ # [V47 핵심 패치] 차트 기반 수익 극대화 보완 (V44-Max)</span>
<span class="g">+ VERSION = "MACRO047.py"</span>
<span class="g">+ MIN_IMPULSE_PCT = 0.15          # 일주일 내 최소 15% 이상 파동이 발생한 코인 타겟 (매수 기회 증가)</span>
<span class="g">+ TAKE_PROFIT = 0.15              # +15.0% 고정 익절선 (윗꼬리 슈팅 사냥)</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 854줄. 직전 버전 대비 +22/-19줄 — 미세 조정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **RSI 게이트 조정**이다. 당시 주석이 의도를 증언한다 — "[ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO047.py (Max Profit Swing Edition)" / "=============================================================================="

## 소회

매크로 지표는 느리고 코인은 빠르다. 이 속도 차이를 극복하지 못한 것이 이 계열의 사인(死因)이다. 시장 전체를 읽고 들어가겠다는 야심이었다. 절반은 과욕이었고, 절반은 지금의 레짐 차단으로 살아남았다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 제시 리버모어는 시장은 결코 틀리지 않고 의견만 틀린다고 했다. 봇의 의견을 고치는 일, 그게 버전업이다.

Developer: JH JEONG
