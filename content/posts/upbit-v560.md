---
title: "[개발일지] UP.V560 — Telegram Absolute Sync"
description: "UP.V560 · Telegram Absolute Sync"
date: 2026-06-21T01:49:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "알림", "슬롯구조", "Trading Bot Lab"]
summary: "Telegram Absolute Sync. 단일파일 진화기 95/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V560 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-21 01:49. 이 시리즈에 보존된 120개 버전 가운데 95번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v560_bot.py — 2,245줄</em></div>
<pre><code><span class="r">- self.filename = "upbit_v552_trade_stats.json"</span>
<span class="r">- for fb in ["upbit_v551_trade_stats.json", "upbit_v550_trade_stats.json", "upbit_v540_tr...</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V560)</span>
<span class="c">+ # 텔레그램 시작 알림 추가</span>
<span class="c">+ # 텔레그램 정지 알림 추가</span>
<span class="g">+ self.filename = "upbit_v560_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v552_trade_stats.json", "upbit_v551_trade_stats.json", "upbit_v550_tr...</span>
<span class="g">+ popup.title(f"SLOT {self.slot_id} V560 스나이퍼 파라미터 정밀 설정")</span>
<span class="g">+ log_msg = f"[Upbit] [Slot {self.slot_id}] {tkr} ○ UI 수동 매수 체결 완료 (금액: {buy_amt:,.0f}원)."</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 2245줄. 직전 버전 대비 +74/-67줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **Telegram Absolute Sync**이다. 당시 주석이 의도를 증언한다 — "3. 개별 코인 슬롯 (V560)" / "텔레그램 시작 알림 추가"

## 소회

버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 폴 튜더 존스는 어제의 가격이 아니라 오늘의 리스크를 보라고 했다. 패치는 언제나 오늘의 리스크가 시켰다.

Developer: JH JEONG
