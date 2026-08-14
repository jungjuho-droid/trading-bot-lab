---
title: "[개발일지] VVWAP.V115 — rich 대시보드 — 현행 터미널 UI의 조상"
description: "VVWAP.V115 · The rich Dashboard: Ancestor of Today's UI"
date: 2026-07-20T14:30:00+09:00
draft: false
series: ["VVWAP기"]
tags: ["개발일지", "VVWAP기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "rich 대시보드 — 현행 터미널 UI의 조상. VVWAP기 14/27."
---

## 배경

이 글은 VVWAP기 — VV의 기원의 한 페이지, VVWAP.V115 의 기록이다. 앵커드 VWAP 기반으로 재설계한 시기로, 현행 VV 넘버링이 여기서 시작된다. 이 시리즈에 보존된 27개 버전 가운데 15번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>VV115.py — 874줄</em></div>
<pre><code><span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE VV114 (VWAP + Alt B + Momentum Out)</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [VV115] 터미널 대시보드를 rich 기반으로 교체 (pip install rich 필요)</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE VV115 (VWAP + Alt B + Momentum Out)</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [VV115 전용 파라미터]</span>
<span class="g">+ from rich.console import Console, Group</span>
<span class="g">+ from rich.live import Live</span>
<span class="g">+ from rich.table import Table</span></code></pre>
</div>

## 무엇을 바꿨나

`from rich.console import Console` — 파이썬 rich 라이브러리 기반 터미널 대시보드로 전면 교체됐다. ANSI 수작업(MACRO009)에서 테이블·패널·라이브 갱신을 갖춘 진짜 TUI로. **현행 VV 봇의 터미널 대시보드가 쓰는 바로 그 스택**이 여기서 채택됐다.

## 소회

도구 하나 바꿨을 뿐인데 봇이 달라 보였다. 보기 좋은 장부는 더 자주 들여다보게 되고, 자주 보는 장부는 거짓말을 못 한다.

> 리처드 데니스는 규칙은 가르칠 수 있어도 확신은 가르칠 수 없다고 했다. 확신은 이렇게 버전을 쌓으며 스스로 만든다.

Developer: JH JEONG
