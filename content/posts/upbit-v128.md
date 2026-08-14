---
title: "[개발일지] UP.V128 — Quantum Final"
description: "UP.V128 · Quantum Final"
date: 2026-06-07T20:23:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "Quantum Final. 단일파일 진화기 37/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V128 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-07 20:23. 이 시리즈에 보존된 120개 버전 가운데 37번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v128_bot.py — 1,429줄</em></div>
<pre><code><span class="r">- # 1. 통계 관리자 (V127 마이그레이션 완료)</span>
<span class="r">- self.filename = "upbit_v127_trade_stats.json"</span>
<span class="c">+ # 1. 통계 관리자 (V128 마이그레이션)</span>
<span class="c">+ # [V128 핵심 패치]: 상승 타겟과 하락 타겟을 동시에 보여주는 양방향 추적 레이더 적용</span>
<span class="g">+ self.filename = "upbit_v128_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v127_trade_stats.json", "upbit_v126_trade_stats.json", "upbit_v125_tr...</span>
<span class="g">+ b_drop = self.active_params.get("buy_drops", [-5.0, -7.0])</span>
<span class="g">+ loss_pct = self.active_params.get("loss", -6.0)</span>
<span class="g">+ if self.buy_step == 0:</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1429줄. 직전 버전 대비 +38/-26줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **Quantum Final**이다. 당시 주석이 의도를 증언한다 — "1. 통계 관리자 (V128 마이그레이션)" / "[V128 핵심 패치]: 상승 타겟과 하락 타겟을 동시에 보여주는 양방향 추적 레이더 적용"

## 소회

버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 제시 리버모어는 큰돈은 매매가 아니라 기다림이 벌어준다고 했다. 이 버전의 코드 몇 줄도 결국 기다림을 만드는 장치였다.

Developer: JH JEONG
