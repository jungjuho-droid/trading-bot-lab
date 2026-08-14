---
title: "[개발일지] UP.V150 — MA와 MACD의 합류"
description: "UP.V150 · MA Meets MACD"
date: 2026-06-09T20:00:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "MA와 MACD의 합류. 단일파일 진화기 40/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V150 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-09 20:00. 이 시리즈에 보존된 120개 버전 가운데 40번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v150_bot.py — 1,324줄</em></div>
<pre><code><span class="r">- # 1. 통계 관리자 (V129 마이그레이션)</span>
<span class="r">- self.filename = "upbit_v129_trade_stats.json"</span>
<span class="c">+ # 1. 통계 관리자 (V150 마이그레이션)</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V150 - 정배열/MACD UI 적용)</span>
<span class="c">+ # [V150] 분할 레이아웃 적용 (좌측: 정보 / 우측: 지표 리스트)</span>
<span class="g">+ import pandas as pd # [V150 신규 도입] MACD 및 다중 이평선 계산용 (pip install pandas 필수)</span>
<span class="g">+ self.filename = "upbit_v150_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v129_trade_stats.json", "upbit_v128_trade_stats.json"]:</span>
<span class="g">+ "tf": tk.StringVar(value=self.active_params.get("tf", self.def_data["tf"])),</span></code></pre>
</div>

## 무엇을 바꿨나

'Quantum MA/MACD Dynamic Edition' — 이동평균에 MACD가 합류했다. MA봇 시절의 크로스 판정 위에 모멘텀 지표를 겹쳐, 추세의 방향과 힘을 함께 보기 시작했다. 게이트가 하나 늘어난다는 것: 진입은 줄고 정확도는 오른다는 데 베팅한 것이다.

## 소회

지표를 더할 때마다 매매 횟수가 줄었다. 처음엔 답답했는데, 계좌는 조용해질수록 건강해졌다.

> 에드 세이코타는 규칙을 지키는 것보다 지킬 수 있는 규칙을 만드는 게 먼저라고 했다. 파라미터 손질은 그 '지킬 수 있는'을 찾는 과정이었다.

Developer: JH JEONG
