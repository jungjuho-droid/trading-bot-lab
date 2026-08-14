---
title: "[개발일지] VVWAP.V129 — 강화된 매매 로직 — 게이트 축적기"
description: "VVWAP.V129 · Hardened Logic: The Gate Accumulator"
date: 2026-07-24T09:23:00+09:00
draft: false
series: ["VVWAP기"]
tags: ["개발일지", "VVWAP기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "강화된 매매 로직 — 게이트 축적기. VVWAP기 25/27."
---

## 배경

이 글은 VVWAP기 — VV의 기원의 한 페이지, VVWAP.V129 의 기록이다. 앵커드 VWAP 기반으로 재설계한 시기로, 현행 VV 넘버링이 여기서 시작된다. 이 시리즈에 보존된 27개 버전 가운데 26번째 기록이다. 원본 파일 시각이 소실된 EC2 복원본이라, 게시일은 버전 순서에 따라 시대 구간 안에 배정했다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>VV129.py — 1,226줄</em></div>
<pre><code><span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE VV127 (매수 스캔 버그 수정)</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE VV129 (강화된 매매 로직)</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [VV120 패치] 타임스탑 제거, PA_WICK_MARGIN 유지</span>
<span class="c">+ # [VV117-119] SL/TP 파라미터</span>
<span class="g">+ VERSION = "VV129"</span>
<span class="g">+ MAX_24H_CHANGE_PCT = 0.10</span>
<span class="g">+ MAX_CONSECUTIVE_LOSSES = 3</span></code></pre>
</div>

## 무엇을 바꿨나

1,226줄. 헤더 주석이 패치의 지층을 보여준다 — '[VV117-119] SL/TP 파라미터', '[VV120] 거래 동기화 유예', '[VV121] 필터: MAX_24H_CHANGE_PCT 0.10'. 버전마다 게이트가 한 겹씩 쌓여온 흔적이 주석 번호로 남아 있다. 24시간 상승률 10% 초과 종목 배제 — 과열 추격을 막는 필터도 이때 굳었다.

## 소회

게이트는 한 번에 설계되지 않았다. 상처마다 한 겹씩 — 주석의 버전 번호들이 그 흉터의 연대기다.

> 레이 달리오는 고통 더하기 반성이 진보라고 했다. 이 버전 번호가 곧 반성의 횟수다.

Developer: JH JEONG
