---
title: "[개발일지] UP.V203 — 손익 집계 정비"
description: "UP.V203 · PnL Accounting"
date: 2026-06-10T21:53:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "손익 집계 정비. 단일파일 진화기 42/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V203 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-10 21:53. 이 시리즈에 보존된 120개 버전 가운데 42번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v203_bot.py — 1,598줄</em></div>
<pre><code><span class="r">- import pandas as pd # [V150/V200 도입] MACD 및 다중 이평선 계산용</span>
<span class="r">- # 1. 통계 관리자 (V200 마이그레이션)</span>
<span class="c">+ # 1. 통계 관리자 (V201/V202 일일/월간 금액 추적 연동)</span>
<span class="g">+ import pandas as pd</span>
<span class="g">+ self.filename = "upbit_v202_trade_stats.json"</span>
<span class="g">+ self.stats = {</span>
<span class="g">+ "daily": {"win": 0, "loss": 0, "profit": 0.0, "date": ""},</span>
<span class="g">+ "weekly": {"win": 0, "loss": 0, "profit": 0.0, "week": ""},</span>
<span class="g">+ "monthly": {"win": 0, "loss": 0, "profit": 0.0, "month": ""}</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1598줄. 직전 버전 대비 +192/-64줄 — 대수술이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **손익 집계 정비**이다. 당시 주석이 의도를 증언한다 — "1. 통계 관리자 (V201/V202 일일/월간 금액 추적 연동)"

## 소회

이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 짐 로저스는 아무것도 하지 않는 것도 포지션이라고 했다. 진입하지 않게 만드는 코드가 진입 코드보다 늘 길었다.

Developer: JH JEONG
