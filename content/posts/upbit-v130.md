---
title: "[개발일지] UP.V130 — 디버그 패치"
description: "UP.V130 · Quantum Final Debug"
date: 2026-06-08T22:25:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "디버그 패치. 단일파일 진화기 39/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V130 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-08 22:25. 이 시리즈에 보존된 120개 버전 가운데 39번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v130_bot.py — 1,442줄</em></div>
<pre><code><span class="r">- for fb in ["upbit_v128_trade_stats.json", "upbit_v126_trade_stats.json", "upbit_v125_tr...</span>
<span class="r">- # 3. 개별 코인 슬롯 (V129 - 매수원금/손익 분리 UI 적용)</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V129 패치)</span>
<span class="c">+ # =========================================================================</span>
<span class="c">+ # [V129 핵심 디버깅 패치] 보유 코인 0개(먼지 포함)일 때 발생하는 평단가 좀비 현상 완벽 제거</span>
<span class="g">+ for fb in ["upbit_v128_trade_stats.json", "upbit_v127_trade_stats.json"]:</span>
<span class="g">+ self.last_ui_states = {"cp": "", "avg": "", "eval": "", "mb": "", "ms": "", "tgt": "", ...</span>
<span class="g">+ if coin &lt;= 0.0001:</span>
<span class="g">+ self.synthetic_avg = 0.0</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1442줄. 직전 버전 대비 +90/-75줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **디버그 패치**이다. 당시 주석이 의도를 증언한다 — "3. 개별 코인 슬롯 (V129 패치)" / "========================================================================="

## 소회

이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 폴 튜더 존스는 어제의 가격이 아니라 오늘의 리스크를 보라고 했다. 패치는 언제나 오늘의 리스크가 시켰다.

Developer: JH JEONG
