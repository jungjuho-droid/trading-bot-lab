---
title: "[개발일지] UP.V307 — 레이아웃 재편"
description: "UP.V307 · Quantum Absolute Layout"
date: 2026-06-12T16:09:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "레이아웃 재편. 단일파일 진화기 52/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V307 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-12 16:09. 이 시리즈에 보존된 120개 버전 가운데 52번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v307_bot.py — 1,702줄</em></div>
<pre><code><span class="r">- # 1. 통계 관리자 (V306 일일/월간 금액 추적)</span>
<span class="r">- self.filename = "upbit_v306_trade_stats.json"</span>
<span class="c">+ # 1. 통계 관리자 (V307 일일/월간 금액 추적)</span>
<span class="c">+ # 개별 슬롯 버튼 높이를 2로 유지하여 빗썸 봇과 동일한 크기와 대칭 확보</span>
<span class="c">+ # 4. 메인 윈도우 (UPBIT V307 Absolute Precision Layout Edition)</span>
<span class="g">+ self.filename = "upbit_v307_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v306_trade_stats.json", "upbit_v305_trade_stats.json", "upbit_v303_tr...</span>
<span class="g">+ if mode == "Bull": p_wr = "-6.0 / 2.0"; p_bd = "-2.0 / -3.5"; p_lr = "-7.0 / 24.0"</span>
<span class="g">+ elif mode == "Bear": p_wr = "-15.0 / 5.0"; p_bd = "-5.0 / -8.0"; p_lr = "-11.0 / 24.0"</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1702줄. 직전 버전 대비 +69/-70줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **레이아웃 재편**이다. 당시 주석이 의도를 증언한다 — "1. 통계 관리자 (V307 일일/월간 금액 추적)" / "개별 슬롯 버튼 높이를 2로 유지하여 빗썸 봇과 동일한 크기와 대칭 확보"

## 소회

이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 알렉산더 엘더는 훌륭한 매매 기록이 훌륭한 트레이더를 만든다고 했다. 버전 파일 하나하나가 나에겐 그 기록이었다.

Developer: JH JEONG
