---
title: "[개발일지] UP.V925 — 택티컬 AI 조건 트리"
description: "UP.V925 · Absolute Tactical AI & Dynamic Engine"
date: 2026-06-30T13:14:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "택티컬 AI 조건 트리. 단일파일 진화기 117/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V925 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-30 13:14. 이 시리즈에 보존된 120개 버전 가운데 117번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v925_bot.py — 1,859줄</em></div>
<pre><code><span class="r">- # [V923] 폰트 및 UI 상수</span>
<span class="r">- # 1. 통계 관리자 (V923)</span>
<span class="c">+ # [V925] 폰트 및 UI 상수</span>
<span class="c">+ # 1. 통계 관리자 (V925)</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V925)</span>
<span class="c">+ # 🔥 [V925] 락업 상태 보존</span>
<span class="g">+ self.filename = "upbit_v925_trade_stats.json"</span>
<span class="g">+ popup = tk.Toplevel(self.root); popup.title(f"SLOT {self.slot_id} V925 스나이퍼 파라미터 정밀 설정")</span>
<span class="g">+ e_rsi = make_row(form_frame, "RSI 목표치", is_chk=True)</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1859줄. 직전 버전 대비 +67/-59줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **택티컬 AI 조건 트리**이다. 당시 주석이 의도를 증언한다 — "[V925] 폰트 및 UI 상수" / "1. 통계 관리자 (V925)"

## 소회

버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 니콜라스 다바스는 시장에 있는 시간보다 기록을 들여다본 시간이 자신을 만들었다고 했다. 아카이브를 정리하는 지금이 꼭 그렇다.

Developer: JH JEONG
