---
title: "[개발일지] UP.V321 — 자동 시작 체계"
description: "UP.V321 · Absolute Compact & Autostart"
date: 2026-06-12T16:48:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "자동 시작 체계. 단일파일 진화기 56/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V321 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-12 16:48. 이 시리즈에 보존된 120개 버전 가운데 56번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v321_bot.py — 1,714줄</em></div>
<pre><code><span class="r">- # 1. 통계 관리자 (V320 일일/월간 금액 추적)</span>
<span class="r">- self.filename = "upbit_v320_trade_stats.json"</span>
<span class="c">+ # 1. 통계 관리자 (V321 일일/월간 금액 추적)</span>
<span class="c">+ # [V321 핵심 복구] 4개 슬롯의 엔진 Start / Stop 버튼 사이즈 및 패딩 최적화 부활</span>
<span class="c">+ # [V321 수정] 파라미터 저장 시 곧바로 START 절차(락업 승인) 진행</span>
<span class="c">+ # 버튼 명칭 변경 (저장 및 START)</span>
<span class="g">+ self.filename = "upbit_v321_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v320_trade_stats.json", "upbit_v310_trade_stats.json", "upbit_v307_tr...</span>
<span class="g">+ e_seed.insert(0, self.vars["seed"].get())</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1714줄. 직전 버전 대비 +114/-106줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **자동 시작 체계**이다. 당시 주석이 의도를 증언한다 — "1. 통계 관리자 (V321 일일/월간 금액 추적)" / "[V321 핵심 복구] 4개 슬롯의 엔진 Start / Stop 버튼 사이즈 및 패딩 최적화 부활"

## 소회

파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 짐 로저스는 아무것도 하지 않는 것도 포지션이라고 했다. 진입하지 않게 만드는 코드가 진입 코드보다 늘 길었다.

Developer: JH JEONG
