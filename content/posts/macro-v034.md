---
title: "[개발일지] MACRO.V034 — RSI 게이트 조정"
description: "MACRO.V034 · RSI Gate Tuning"
date: 2026-07-10T23:32:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "RSI", "Trading Bot Lab"]
summary: "RSI 게이트 조정. 병렬 실험기 69/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V034 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 22번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO034.py — 671줄</em></div>
<pre><code><span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO033.py</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO034.py</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [V34 핵심 픽스] API 지연 대비 이중 방어망 (수동 블랙리스트 복구)</span>
<span class="c">+ # [ DATA PIPELINE ] 스캐너 (API 지연 대비 이중 방어 탑재)</span>
<span class="g">+ VERSION = "MACRO034.py"</span>
<span class="g">+ STATE_FILE = "MACRO034_STATE.json"</span>
<span class="g">+ BLACKLIST_COINS = ['KRW-AERGO']</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 671줄. 직전 버전 대비 +13/-14줄 — 미세 조정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **RSI 게이트 조정**이다. 당시 주석이 의도를 증언한다 — "[ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO034.py" / "=============================================================================="

## 소회

시장 전체를 읽고 들어가겠다는 야심이었다. 절반은 과욕이었고, 절반은 지금의 레짐 차단으로 살아남았다. 매크로 지표는 느리고 코인은 빠르다. 이 속도 차이를 극복하지 못한 것이 이 계열의 사인(死因)이다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 제시 리버모어는 시장은 결코 틀리지 않고 의견만 틀린다고 했다. 봇의 의견을 고치는 일, 그게 버전업이다.

Developer: JH JEONG
