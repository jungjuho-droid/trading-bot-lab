---
title: "[개발일지] MACRO.V049 — RSI 게이트 조정"
description: "MACRO.V049 · RSI Gate Tuning"
date: 2026-07-13T09:08:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "RSI", "Trading Bot Lab"]
summary: "RSI 게이트 조정. 병렬 실험기 85/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V049 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 38번째 기록이다. 원본 파일 시각이 소실된 EC2 복원본이라, 게시일은 버전 순서에 따라 시대 구간 안에 배정했다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO049.py — 807줄</em></div>
<pre><code><span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO048.py (Triple Defense Edition)</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO049.py (Defensive Quantity Edition)</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [V49 핵심 패치] 방어형 다다익선 스캐너 (매수 기회 극대화)</span>
<span class="c">+ # [V48 계승] 3중 방어 시스템 파라미터</span>
<span class="g">+ VERSION = "MACRO049.py"</span>
<span class="g">+ MACRO_TREND_MA = 50             # 50시간(약 2일선) 거시 추세 적용 (타겟 대폭 확대)</span>
<span class="g">+ MIN_IMPULSE_PCT = 0.08          # 일주일 내 최소 8% 이상 상승 코인 (안전한 짤짤이 펌핑 사냥)</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 807줄. 직전 버전 대비 +15/-15줄 — 미세 조정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **RSI 게이트 조정**이다. 당시 주석이 의도를 증언한다 — "[ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO049.py (Defensive Quantity Edition)" / "=============================================================================="

## 소회

시장 전체를 읽고 들어가겠다는 야심이었다. 절반은 과욕이었고, 절반은 지금의 레짐 차단으로 살아남았다. 매크로 지표는 느리고 코인은 빠르다. 이 속도 차이를 극복하지 못한 것이 이 계열의 사인(死因)이다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 제시 리버모어는 큰돈은 매매가 아니라 기다림이 벌어준다고 했다. 이 버전의 코드 몇 줄도 결국 기다림을 만드는 장치였다.

Developer: JH JEONG
