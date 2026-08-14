---
title: "[개발일지] UP.V200 — MA·MACD 지표 결합"
description: "UP.V200 · Quantum MA/MACD Fully Integrated"
date: 2026-06-09T20:18:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "MA·MACD 지표 결합. 단일파일 진화기 41/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V200 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-09 20:18. 이 시리즈에 보존된 120개 버전 가운데 41번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v200_bot.py — 1,470줄</em></div>
<pre><code><span class="r">- import pandas as pd # [V150 신규 도입] MACD 및 다중 이평선 계산용 (pip install pandas 필수)</span>
<span class="r">- # 1. 통계 관리자 (V150 마이그레이션)</span>
<span class="c">+ # 1. 통계 관리자 (V200 마이그레이션)</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V200 - V129/V150 무삭제 통합)</span>
<span class="c">+ # V129 옵션 변수</span>
<span class="c">+ # V150 옵션 변수</span>
<span class="g">+ import pandas as pd # [V150/V200 도입] MACD 및 다중 이평선 계산용</span>
<span class="g">+ self.filename = "upbit_v200_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v150_trade_stats.json", "upbit_v129_trade_stats.json"]:</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1470줄. 직전 버전 대비 +198/-52줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **MA·MACD 지표 결합**이다. 당시 주석이 의도를 증언한다 — "1. 통계 관리자 (V200 마이그레이션)" / "3. 개별 코인 슬롯 (V200 - V129/V150 무삭제 통합)"

## 소회

버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 마크 더글러스는 시장이 아니라 자신의 규칙과 거래하라고 했다. 봇을 만든다는 건 그 규칙을 물리적으로 만드는 일이다.

Developer: JH JEONG
