---
title: "[개발일지] UP.V102 — 스윙과 방어의 결합"
description: "UP.V102 · Swing & Defense - Hardcoded API"
date: 2026-06-04T20:16:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "스윙과 방어의 결합. 단일파일 진화기 11/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V102 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-04 20:16. 이 시리즈에 보존된 120개 버전 가운데 11번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v102_bot.py — 1,612줄</em></div>
<pre><code><span class="r">- self.filename = "upbit_v101_trade_stats.json"</span>
<span class="r">- fallback_files = ["upbit_v100_trade_stats.json", "upbit_v99_trade_stats.json"]</span>
<span class="c">+ # 3. 개별 코인 슬롯 (UPBIT V102 스윙 감시 엔진)</span>
<span class="c">+ # 시작 시 항상 STOP 상태로 강제 초기화</span>
<span class="c">+ # 4. 메인 윈도우 (UPBIT V102 Swing Edition - Hardcoded API)</span>
<span class="c">+ # [V102] API Key 하드코딩 및 마스킹 처리</span>
<span class="g">+ self.filename = "upbit_v102_trade_stats.json"</span>
<span class="g">+ fallback_files = ["upbit_v101_trade_stats.json", "upbit_v100_trade_stats.json", "upbit_...</span>
<span class="g">+ self.root.title("Upbit Auto-Trading Bot V102 (Swing &amp; Defense Edition - Hardcoded API)")</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1612줄. 직전 버전 대비 +40/-37줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **스윙과 방어의 결합**이다. 당시 주석이 의도를 증언한다 — "3. 개별 코인 슬롯 (UPBIT V102 스윙 감시 엔진)" / "시작 시 항상 STOP 상태로 강제 초기화"

## 소회

파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 폴 튜더 존스는 어제의 가격이 아니라 오늘의 리스크를 보라고 했다. 패치는 언제나 오늘의 리스크가 시켰다.

Developer: JH JEONG
