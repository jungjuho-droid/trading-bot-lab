---
title: "[개발일지] UP.V907 — 듀얼 엔진 분리"
description: "UP.V907 · Dual Engine Splitting"
date: 2026-06-22T21:10:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "듀얼 엔진 분리. 단일파일 진화기 112/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V907 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-22 21:10. 이 시리즈에 보존된 120개 버전 가운데 112번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v907_bot.py — 1,794줄</em></div>
<pre><code><span class="r">- # 1. 통계 관리자 (V906)</span>
<span class="r">- self.filename = "upbit_v906_trade_stats.json"</span>
<span class="c">+ # 1. 통계 관리자 (V907)</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V907)</span>
<span class="c">+ # 🔥 [V907 UI 개조] 좌측 가격 정보, 우측 엔진 상태 및 수익률 분리</span>
<span class="c">+ # 좌측 4줄 유지</span>
<span class="g">+ self.filename = "upbit_v907_trade_stats.json"</span>
<span class="g">+ self.engine_type = saved_state.get("engine_type", "STANDBY")  # V907 듀얼 엔진 타입 저장</span>
<span class="g">+ self.last_ui_states = {"cp": "", "avg": "", "invest": "", "eval": "", "mb": "", "ms": "...</span></code></pre>
</div>

## 무엇을 바꿨나

'Dual Engine Splitting & Tactical AI'. V590에서 동거시킨 두 엔진을 이번엔 구조적으로 분리했다 — 판단 경로와 상태를 엔진별로 갈라 간섭을 끊었다. 1,794줄. 단일 파일 안에서 할 수 있는 관심사 분리의 한계선까지 간 버전이다.

## 소회

한 파일 안의 분리는 결국 미봉이었다. 이 답답함이 몇 주 뒤 모듈 분리(vv141)의 연료가 된다.

> 짐 로저스는 아무것도 하지 않는 것도 포지션이라고 했다. 진입하지 않게 만드는 코드가 진입 코드보다 늘 길었다.

Developer: JH JEONG
