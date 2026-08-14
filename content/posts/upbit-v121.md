---
title: "[개발일지] UP.V121 — 파이널 프루프 검증"
description: "UP.V121 · Quantum Final Proof"
date: 2026-06-06T02:34:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "파이널 프루프 검증. 단일파일 진화기 30/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V121 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-06 02:34. 이 시리즈에 보존된 120개 버전 가운데 30번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v121_bot.py — 1,376줄</em></div>
<pre><code><span class="r">- # 1. 통계 관리자 (V120 규격)</span>
<span class="r">- self.filename = "upbit_v120_trade_stats.json"</span>
<span class="c">+ # 1. 통계 관리자 (V121 규격)</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V121 퀀텀 HTS 엔진)</span>
<span class="c">+ # [V121 교정] 수수료 계산의 100% 무결성을 위해 역산 로직 사용</span>
<span class="g">+ self.filename = "upbit_v121_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v120_trade_stats.json", "upbit_v119_trade_stats.json", "upbit_v118_tr...</span>
<span class="g">+ max_buyable = math.floor(krw / 1.0005)</span>
<span class="g">+ if buy_amt &gt; max_buyable: buy_amt = max_buyable</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1376줄. 직전 버전 대비 +50/-23줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **파이널 프루프 검증**이다. 당시 주석이 의도를 증언한다 — "1. 통계 관리자 (V121 규격)" / "3. 개별 코인 슬롯 (V121 퀀텀 HTS 엔진)"

## 소회

이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 워런 버핏은 썰물이 되면 누가 벌거벗고 수영했는지 드러난다고 했다. 안전장치는 밀물일 때 만들어야 한다 — 이 버전처럼.

Developer: JH JEONG
