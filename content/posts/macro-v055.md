---
title: "[개발일지] MACRO.V055 — 텔레그램 리포트 정비"
description: "MACRO.V055 · Telegram Reporting"
date: 2026-07-13T15:19:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "알림", "Trading Bot Lab"]
summary: "텔레그램 리포트 정비. 병렬 실험기 90/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V055 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 43번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO055.py — 891줄</em></div>
<pre><code><span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO053 (Shadow 1.8% Edition)</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO055 (V55 Final Edition)</span>
<span class="c">+ # ==============================================================================</span>
<span class="g">+ import urllib.request</span>
<span class="g">+ VERSION = "MACRO055"</span>
<span class="g">+ def send_telegram_sync(msg):</span>
<span class="g">+ """엔진 강제 종료 시 알람을 쏘기 위한 동기화 통신 모듈"""</span>
<span class="g">+ url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 891줄. 직전 버전 대비 +86/-29줄 — 중간 수정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **텔레그램 리포트 정비**이다. 당시 주석이 의도를 증언한다 — "[ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO055 (V55 Final Edition)" / "=============================================================================="

## 소회

시장 전체를 읽고 들어가겠다는 야심이었다. 절반은 과욕이었고, 절반은 지금의 레짐 차단으로 살아남았다. 매크로 지표는 느리고 코인은 빠르다. 이 속도 차이를 극복하지 못한 것이 이 계열의 사인(死因)이다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 짐 로저스는 아무것도 하지 않는 것도 포지션이라고 했다. 진입하지 않게 만드는 코드가 진입 코드보다 늘 길었다.

Developer: JH JEONG
