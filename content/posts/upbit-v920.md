---
title: "[개발일지] UP.V920 — 택티컬 AI 조건 트리"
description: "UP.V920 · Absolute Tactical AI & Dynamic Engine"
date: 2026-06-22T22:31:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "택티컬 AI 조건 트리. 단일파일 진화기 113/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V920 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-22 22:31. 이 시리즈에 보존된 120개 버전 가운데 113번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v920_bot.py — 1,821줄</em></div>
<pre><code><span class="r">- # 1. 통계 관리자 (V907)</span>
<span class="r">- self.filename = "upbit_v907_trade_stats.json"</span>
<span class="c">+ # ==========================================</span>
<span class="c">+ # [V920] 폰트 및 UI 상수</span>
<span class="c">+ # 1. 통계 관리자 (V920)</span>
<span class="g">+ FONT_MAIN = ("맑은 고딕", 9, "bold")</span>
<span class="g">+ FONT_TITLE = ("맑은 고딕", 11, "bold")</span>
<span class="g">+ self.filename = "upbit_v920_trade_stats.json"</span>
<span class="g">+ self.is_locked = False  # 🔥 [V920] 수동 개입 락업 플래그</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1821줄. 직전 버전 대비 +191/-164줄 — 대수술이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **택티컬 AI 조건 트리**이다. 당시 주석이 의도를 증언한다 — "==========================================" / "[V920] 폰트 및 UI 상수"

## 소회

파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 레이 달리오는 고통 더하기 반성이 진보라고 했다. 이 버전 번호가 곧 반성의 횟수다.

Developer: JH JEONG
