---
title: "[개발일지] BASE.V013 — 106줄짜리 조각"
description: "BASE.V013 · A 106-Line Fragment"
date: 2026-07-07T22:38:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "알림", "Trading Bot Lab"]
summary: "106줄짜리 조각. 병렬 실험기 45/108."
---

## 배경

이 글은 BASE 실험기의 한 페이지, BASE.V013 의 기록이다. 바닥권 지지선 진입(Bottom Area Support Entry)이라는 단일 아이디어를 파고든 계열이다. 이 시리즈에 보존된 11개 버전 가운데 9번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실). 이 보존본은 전체 파일이 아니라 당시 바꾼 부분만 남긴 스니펫이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>BASE013.py — 106줄</em></div>
<pre><code><span class="r">- import websockets</span>
<span class="r">- import aiohttp</span>
<span class="c">+ # UPBIT HYBRID ENGINE - BASE013</span>
<span class="c">+ # ------------------------------------------------------------------------------</span>
<span class="c">+ # [CORE DESCRIPTION]</span>
<span class="c">+ # - 스마트 완화 로직 이식 (BASE012 튜닝값 -&gt; BASE013 확정 릴리즈)</span>
<span class="g">+ import datetime</span>
<span class="g">+ BASE_PUMP_MIN = 0.011       # 1.1% 소폭 펌핑부터 추적 대상 포함 (완화)</span>
<span class="g">+ BASE_VOL_SURGE = 2.2        # 평소 대비 거래량 2.2배 유입 시 인정 (완화)</span></code></pre>
</div>

## 무엇을 바꿨나

이 보존본은 106줄 스니펫이다. 텔레그램 리포트 포맷 구간만 떼어 저장한 것으로 추정한다 — 남은 조각의 대부분이 리포트 문자열 f-string이다.

## 소회

전략 시리즈에서도 결국 손이 자주 간 건 보고서였다. 사람이 읽는 부분이 늘 마지막까지 다듬어진다.

> 폴 튜더 존스는 어제의 가격이 아니라 오늘의 리스크를 보라고 했다. 패치는 언제나 오늘의 리스크가 시켰다.

Developer: JH JEONG
