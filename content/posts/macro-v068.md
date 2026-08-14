---
title: "[개발일지] MACRO.V068 — RSI 게이트 조정"
description: "MACRO.V068 · RSI Gate Tuning"
date: 2026-07-15T09:48:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "RSI", "Trading Bot Lab"]
summary: "RSI 게이트 조정. 병렬 실험기 103/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V068 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 56번째 기록이다. 원본 파일 시각이 소실된 EC2 복원본이라, 게시일은 버전 순서에 따라 시대 구간 안에 배정했다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO068.py — 960줄</em></div>
<pre><code><span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO067 (Micro Shadow Edition)</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO068 (Time-out TR Edition)</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [V68 패치] TR 타임스탑(Time-out) 파라미터 (초 단위)</span>
<span class="c">+ # [V68 패치] 동기화 슬롯 진입 시에도 tr_stage_time 초기화 적용</span>
<span class="g">+ VERSION = "MACRO068"</span>
<span class="g">+ TR_STAGE1_TIMEOUT_SEC = 3600    # TR1단계 1시간(3600초) 횡보 시 익절</span>
<span class="g">+ TR_STAGE2_TIMEOUT_SEC = 10800   # TR2단계 3시간(10800초) 횡보 시 익절</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 960줄. 직전 버전 대비 +36/-15줄 — 미세 조정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **RSI 게이트 조정**이다. 당시 주석이 의도를 증언한다 — "[ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO068 (Time-out TR Edition)" / "=============================================================================="

## 소회

시장 전체를 읽고 들어가겠다는 야심이었다. 절반은 과욕이었고, 절반은 지금의 레짐 차단으로 살아남았다. 매크로 지표는 느리고 코인은 빠르다. 이 속도 차이를 극복하지 못한 것이 이 계열의 사인(死因)이다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 마크 더글러스는 시장이 아니라 자신의 규칙과 거래하라고 했다. 봇을 만든다는 건 그 규칙을 물리적으로 만드는 일이다.

Developer: JH JEONG
