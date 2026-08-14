---
title: "[개발일지] MACRO.V009 — 터미널에 색을 입히다 — ANSI 대시보드"
description: "MACRO.V009 · Painting the Terminal: ANSI Colors"
date: 2026-07-08T19:54:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "터미널에 색을 입히다 — ANSI 대시보드. 병렬 실험기 52/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V009 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 5번째 기록이다. 원본 파일 시각이 소실된 EC2 복원본이라, 게시일은 버전 순서에 따라 시대 구간 안에 배정했다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO009.py — 498줄</em></div>
<pre><code><span class="r">- # [ MACRO008 1H BREAKOUT SWING ENGINE (PROFESSIONAL EDITION) ]</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ MACRO009 1H BREAKOUT SWING ENGINE (ULTIMATE EDITION) ]</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [ UI ANSI Color ]</span>
<span class="c">+ # ---------------------------------------------------------</span>
<span class="g">+ C_CYAN = '\033[96m'</span>
<span class="g">+ C_GREEN = '\033[92m'</span>
<span class="g">+ C_RED = '\033[91m'</span></code></pre>
</div>

## 무엇을 바꿨나

`C_CYAN = '\033[96m'` — ANSI 이스케이프 코드로 터미널에 색이 들어왔다. 수익은 초록, 손실은 빨강, 헤더는 시안. GUI를 버린 지 한 달, 터미널이 드디어 대시보드다워지기 시작했다. 현행 봇의 컬러 터미널 UI가 여기서 첫 붓질을 한다.

## 소회

창을 버렸다고 눈을 버린 건 아니었다. 색 여섯 개로 tkinter 시절보다 명료한 화면이 나왔다.

> 리처드 데니스는 규칙은 가르칠 수 있어도 확신은 가르칠 수 없다고 했다. 확신은 이렇게 버전을 쌓으며 스스로 만든다.

Developer: JH JEONG
