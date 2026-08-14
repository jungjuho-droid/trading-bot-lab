---
title: "[개발일지] UP.V099 — 자동 물타기 평단 계산"
description: "UP.V099 · Absolute Hard-Lock & Auto-Avg"
date: 2026-06-03T20:37:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "자동 물타기 평단 계산. 단일파일 진화기 8/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V099 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-03 20:37. 이 시리즈에 보존된 120개 버전 가운데 8번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v99_bot.py — 1,615줄</em></div>
<pre><code><span class="r">- # 1. 전역 통계 관리자 (업비트 V97 규격)</span>
<span class="r">- self.filename = "upbit_v97_trade_stats.json"</span>
<span class="c">+ # 1. 전역 통계 관리자 (업비트 V99 규격)</span>
<span class="c">+ # 이전 버전 통계 데이터 승계</span>
<span class="c">+ # 2. 업비트 API V1 엔진 (100% Upbit 전용 JWT 인증)</span>
<span class="c">+ # 3. 개별 코인 슬롯 (UPBIT V99 절대 락업 &amp; 자동평단 엔진)</span>
<span class="g">+ self.filename = "upbit_v99_trade_stats.json"</span>
<span class="g">+ fallback_files = ["upbit_v97_trade_stats.json", "upbit_v96_trade_stats.json", "upbit_v9...</span>
<span class="g">+ messagebox.showwarning("보안 경고", "엔진이 가동 중입니다!\n\n코인 변경 시 버그 방지를 위해\n먼저 [STOP] 후 변경하십시오.")</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1615줄. 직전 버전 대비 +46/-43줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **자동 물타기 평단 계산**이다. 당시 주석이 의도를 증언한다 — "1. 전역 통계 관리자 (업비트 V99 규격)" / "이전 버전 통계 데이터 승계"

## 소회

파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 브루스 코브너는 자신이 틀릴 수 있는 지점을 미리 정해두는 것이 포지션의 전부라고 했다. 파라미터 파일이 곧 그 지점들의 목록이다.

Developer: JH JEONG
