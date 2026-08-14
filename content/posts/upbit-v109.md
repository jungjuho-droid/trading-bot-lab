---
title: "[개발일지] UP.V109 — 슬롯별 독립 반등 판정"
description: "UP.V109 · Independent Rebound"
date: 2026-06-05T12:08:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "슬롯별 독립 반등 판정. 단일파일 진화기 18/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V109 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-05 12:08. 이 시리즈에 보존된 120개 버전 가운데 18번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v109_bot.py — 1,773줄</em></div>
<pre><code><span class="r">- # 1. 전역 통계 관리자 (V108 규격)</span>
<span class="r">- self.filename = "upbit_v108_trade_stats.json"</span>
<span class="c">+ # 1. 전역 통계 관리자 (V109 규격)</span>
<span class="c">+ # 3. 개별 코인 슬롯 (UPBIT V109 UI &amp; 반등 분리 엔진)</span>
<span class="c">+ # [V109 패치] 기존 reb 파라미터 마이그레이션 및 분리 적용</span>
<span class="c">+ # [V109 UI 개편] 시드/수동평단 독립 라인화 및 반등 세분화</span>
<span class="g">+ self.filename = "upbit_v109_trade_stats.json"</span>
<span class="g">+ fallback_files = ["upbit_v108_trade_stats.json", "upbit_v107_trade_stats.json", "upbit_...</span>
<span class="g">+ legacy_reb = self.def_data.get("reb", "2.0")</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1773줄. 직전 버전 대비 +113/-80줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **슬롯별 독립 반등 판정**이다. 당시 주석이 의도를 증언한다 — "1. 전역 통계 관리자 (V109 규격)" / "3. 개별 코인 슬롯 (UPBIT V109 UI & 반등 분리 엔진)"

## 소회

이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 리처드 데니스는 규칙은 가르칠 수 있어도 확신은 가르칠 수 없다고 했다. 확신은 이렇게 버전을 쌓으며 스스로 만든다.

Developer: JH JEONG
