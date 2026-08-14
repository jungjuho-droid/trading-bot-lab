---
title: "[개발일지] UP.V504 — 피라미드 스나이퍼 정비"
description: "UP.V504 · Pyramid Multi-Sniper"
date: 2026-06-16T21:14:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "전략실험", "Trading Bot Lab"]
summary: "피라미드 스나이퍼 정비. 단일파일 진화기 78/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V504 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-16 21:14. 이 시리즈에 보존된 120개 버전 가운데 78번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v504_bot.py — 2,167줄</em></div>
<pre><code><span class="r">- self.filename = "upbit_v503_trade_stats.json"</span>
<span class="r">- for fb in ["upbit_v502_trade_stats.json", "upbit_v500_trade_stats.json", "upbit_v420_tr...</span>
<span class="c">+ # [V505] 모드 변수 추가 (1, 2번 슬롯은 스나이퍼 강제, 3, 4번은 선택 가능)</span>
<span class="c">+ # 4. 메인 윈도우 (UPBIT V505)</span>
<span class="g">+ self.filename = "upbit_v505_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v503_trade_stats.json", "upbit_v502_trade_stats.json", "upbit_v500_tr...</span>
<span class="g">+ self.slot_mode_var = tk.StringVar(value="SNIPER" if self.slot_id in [1, 2] else "QUANTUM")</span>
<span class="g">+ title_text = f"■ SLOT {self.slot_id}"</span>
<span class="g">+ if self.slot_id in [1, 2]:</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 2167줄. 직전 버전 대비 +138/-101줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **피라미드 스나이퍼 정비**이다. 당시 주석이 의도를 증언한다 — "[V505] 모드 변수 추가 (1, 2번 슬롯은 스나이퍼 강제, 3, 4번은 선택 가능)" / "4. 메인 윈도우 (UPBIT V505)"

## 소회

이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 브루스 코브너는 자신이 틀릴 수 있는 지점을 미리 정해두는 것이 포지션의 전부라고 했다. 파라미터 파일이 곧 그 지점들의 목록이다.

Developer: JH JEONG
