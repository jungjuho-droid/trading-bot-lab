---
title: "[개발일지] UP.V503 — 피라미드 스나이퍼 정비"
description: "UP.V503 · Pyramid Sniper"
date: 2026-06-16T20:49:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "전략실험", "Trading Bot Lab"]
summary: "피라미드 스나이퍼 정비. 단일파일 진화기 77/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V503 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-16 20:49. 이 시리즈에 보존된 120개 버전 가운데 77번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v503_bot.py — 2,130줄</em></div>
<pre><code><span class="r">- self.filename = "upbit_v502_trade_stats.json"</span>
<span class="r">- for fb in ["upbit_v500_trade_stats.json", "upbit_v420_trade_stats.json"]:</span>
<span class="c">+ # 4. 메인 윈도우 (UPBIT V503)</span>
<span class="c">+ # V503 전용 오토 스나이퍼 토글 (Slot 1 전용)</span>
<span class="c">+ # V503 5대 조건 스코어링 평가기</span>
<span class="c">+ # V503 스캐너 (스코어링 반영 및 기준점 표기)</span>
<span class="g">+ self.filename = "upbit_v503_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v502_trade_stats.json", "upbit_v500_trade_stats.json", "upbit_v420_tr...</span>
<span class="g">+ f"======== [ SLOT {self.slot_id} ({ui_tkr}) V503 매매 계획 ] ========\n\n"</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 2130줄. 직전 버전 대비 +46/-29줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **피라미드 스나이퍼 정비**이다. 당시 주석이 의도를 증언한다 — "4. 메인 윈도우 (UPBIT V503)" / "V503 전용 오토 스나이퍼 토글 (Slot 1 전용)"

## 소회

이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 제시 리버모어는 시장은 결코 틀리지 않고 의견만 틀린다고 했다. 봇의 의견을 고치는 일, 그게 버전업이다.

Developer: JH JEONG
