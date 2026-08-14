---
title: "[개발일지] UP.V409 — 수동 입력 정비"
description: "UP.V409 · Quantum Manual Input"
date: 2026-06-12T19:42:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "수동 입력 정비. 단일파일 진화기 67/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V409 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-12 19:42. 이 시리즈에 보존된 120개 버전 가운데 67번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v409_bot.py — 1,897줄</em></div>
<pre><code><span class="r">- self.filename = "upbit_v408_trade_stats.json"</span>
<span class="r">- else:</span>
<span class="c">+ # 4. 메인 윈도우 (UPBIT V409 Manual Override Edition)</span>
<span class="c">+ # [V409 픽스] 사용자가 수동으로 입력한 키가 없으면 무리해서 연결하지 않고 대기합니다.</span>
<span class="c">+ # [V409 픽스] API 연결 실패 시 오류 원인을 명확히 띄우고 즉시 정지합니다.</span>
<span class="g">+ self.filename = "upbit_v409_trade_stats.json"</span>
<span class="g">+ chk_var = tk.BooleanVar(popup)</span>
<span class="g">+ summary_msg = f"======== [ SLOT {self.slot_id} ({ui_tkr}) V409 매매 계획 ] ========\n\n"</span>
<span class="g">+ summary_msg += "이 정밀한 V409 엔진 설정을 하드락(Lock-up) 승인하십니까?"</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1897줄. 직전 버전 대비 +69/-83줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **수동 입력 정비**이다. 당시 주석이 의도를 증언한다 — "4. 메인 윈도우 (UPBIT V409 Manual Override Edition)" / "[V409 픽스] 사용자가 수동으로 입력한 키가 없으면 무리해서 연결하지 않고 대기합니다."

## 소회

이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 폴 튜더 존스는 어제의 가격이 아니라 오늘의 리스크를 보라고 했다. 패치는 언제나 오늘의 리스크가 시켰다.

Developer: JH JEONG
