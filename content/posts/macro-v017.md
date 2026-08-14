---
title: "[개발일지] MACRO.V017 — 텔레그램 리포트 정비"
description: "MACRO.V017 · Telegram Reporting"
date: 2026-07-09T11:05:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "알림", "Trading Bot Lab"]
summary: "텔레그램 리포트 정비. 병렬 실험기 57/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V017 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 10번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO017.py — 580줄</em></div>
<pre><code><span class="r">- # [ 설정 구역 ] API 키 및 텔레그램 설정 (환경 변수 자동 로드 복원)</span>
<span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO016.py</span>
<span class="c">+ # [ 설정 구역 ] API 키 및 텔레그램 설정 (환경 변수 자동 로드)</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO017.py</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # 🚨 이전 버전(MACRO016) SyntaxError 해결: 콜론 및 as resp 추가 완료</span>
<span class="g">+ VERSION = "MACRO017.py"</span>
<span class="g">+ STATE_FILE = "MACRO017_STATE.json"</span>
<span class="g">+ async with http_session.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": msg, "pars...</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 580줄. 직전 버전 대비 +13/-11줄 — 미세 조정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **텔레그램 리포트 정비**이다. 당시 주석이 의도를 증언한다 — "[ 설정 구역 ] API 키 및 텔레그램 설정 (환경 변수 자동 로드)" / "[ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO017.py"

## 소회

매크로 지표는 느리고 코인은 빠르다. 이 속도 차이를 극복하지 못한 것이 이 계열의 사인(死因)이다. 시장 전체를 읽고 들어가겠다는 야심이었다. 절반은 과욕이었고, 절반은 지금의 레짐 차단으로 살아남았다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 제시 리버모어는 큰돈은 매매가 아니라 기다림이 벌어준다고 했다. 이 버전의 코드 몇 줄도 결국 기다림을 만드는 장치였다.

Developer: JH JEONG
