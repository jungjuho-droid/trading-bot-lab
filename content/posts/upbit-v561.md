---
title: "[개발일지] UP.V561 — Absolute UI Sync"
description: "UP.V561 · Absolute UI Sync"
date: 2026-06-21T09:03:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "Absolute UI Sync. 단일파일 진화기 96/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V561 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-21 09:03. 이 시리즈에 보존된 120개 버전 가운데 96번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v561_bot.py — 2,248줄</em></div>
<pre><code><span class="r">- self.filename = "upbit_v560_trade_stats.json"</span>
<span class="r">- for fb in ["upbit_v552_trade_stats.json", "upbit_v551_trade_stats.json", "upbit_v550_tr...</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V562)</span>
<span class="c">+ # 🔥 [V562] 메인 대시보드 화면의 라벨 이름도 정확히 동기화 완료!</span>
<span class="g">+ self.filename = "upbit_v562_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v561_trade_stats.json", "upbit_v560_trade_stats.json", "upbit_v552_tr...</span>
<span class="g">+ self.vars["sell_target"].set("2.0/4.0/1.5")</span>
<span class="g">+ labels_l2 = ["대기/반등", "매수비율", "추가하락", "익절타점/TR하락", "익절비율", "손절/리셋"]</span>
<span class="g">+ popup.title(f"SLOT {self.slot_id} V562 스나이퍼 파라미터 정밀 설정")</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 2248줄. 직전 버전 대비 +67/-64줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **Absolute UI Sync**이다. 당시 주석이 의도를 증언한다 — "3. 개별 코인 슬롯 (V562)" / "🔥 [V562] 메인 대시보드 화면의 라벨 이름도 정확히 동기화 완료!"

## 소회

버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 에드 세이코타는 규칙을 지키는 것보다 지킬 수 있는 규칙을 만드는 게 먼저라고 했다. 파라미터 손질은 그 '지킬 수 있는'을 찾는 과정이었다.

Developer: JH JEONG
