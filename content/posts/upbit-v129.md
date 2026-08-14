---
title: "[개발일지] UP.V129 — 평가 로직 조정"
description: "UP.V129 · Quantum Dynamic Evaluation"
date: 2026-06-09T19:45:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "평가 로직 조정. 단일파일 진화기 38/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V129 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-09 19:45. 이 시리즈에 보존된 120개 버전 가운데 38번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v129_bot.py — 1,427줄</em></div>
<pre><code><span class="r">- # 1. 통계 관리자 (V128 마이그레이션)</span>
<span class="r">- self.filename = "upbit_v128_trade_stats.json"</span>
<span class="c">+ # 1. 통계 관리자 (V129 마이그레이션)</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V129 - 매수원금/손익 분리 UI 적용)</span>
<span class="c">+ # 3단계 하드코딩 프리셋 자동 매핑 (V126 / V129 표준)</span>
<span class="c">+ # 콤보박스 바인딩</span>
<span class="g">+ self.filename = "upbit_v129_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v128_trade_stats.json", "upbit_v126_trade_stats.json", "upbit_v125_tr...</span>
<span class="g">+ self.last_ui_states = {"cp": "", "avg": "", "invest": "", "eval": "", "mb": "", "ms": "...</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1427줄. 직전 버전 대비 +64/-66줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **평가 로직 조정**이다. 당시 주석이 의도를 증언한다 — "1. 통계 관리자 (V129 마이그레이션)" / "3. 개별 코인 슬롯 (V129 - 매수원금/손익 분리 UI 적용)"

## 소회

버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 알렉산더 엘더는 훌륭한 매매 기록이 훌륭한 트레이더를 만든다고 했다. 버전 파일 하나하나가 나에겐 그 기록이었다.

Developer: JH JEONG
