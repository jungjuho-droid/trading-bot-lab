---
title: "[개발일지] UP.V302 — 정밀 표시 조정"
description: "UP.V302 · Quantum UI Precision"
date: 2026-06-12T13:43:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "정밀 표시 조정. 단일파일 진화기 48/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V302 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-12 13:43. 이 시리즈에 보존된 120개 버전 가운데 48번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v302_bot.py — 1,886줄</em></div>
<pre><code><span class="r">- # 1. 통계 관리자 (V300 일일/월간 금액 추적 연동)</span>
<span class="r">- self.filename = "upbit_v300_trade_stats.json"</span>
<span class="c">+ # 1. 통계 관리자 (V301 일일/월간 금액 추적 연동)</span>
<span class="c">+ # 4. 메인 윈도우 (UPBIT V301 Quantum Precision Layout Edition)</span>
<span class="c">+ # [V301 핵심 UI 변경 파트: 좌측 압축 정렬 및 세로 공간 확보]</span>
<span class="c">+ # [V301] 제어 모듈을 가로 화면의 왼쪽 50% 영역에 컴팩트하게 묶음</span>
<span class="g">+ self.filename = "upbit_v301_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v300_trade_stats.json", "upbit_v210_trade_stats.json", "upbit_v208_tr...</span>
<span class="g">+ summary_msg = f"======== [ SLOT {self.slot_id} ({ui_tkr}) V301 매매 계획 ] ========\n\n"</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1886줄. 직전 버전 대비 +48/-51줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **정밀 표시 조정**이다. 당시 주석이 의도를 증언한다 — "1. 통계 관리자 (V301 일일/월간 금액 추적 연동)" / "4. 메인 윈도우 (UPBIT V301 Quantum Precision Layout Edition)"

## 소회

버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 윌리엄 오닐은 손절은 보험료라고 했다. 보험료 계산식을 고치는 날이 제일 많았다.

Developer: JH JEONG
