---
title: "[개발일지] UP.V300 — V300 고지 — 레이아웃 대개편"
description: "UP.V300 · Hill V300: The Layout Overhaul"
date: 2026-06-12T12:17:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "스캐너", "슬롯구조", "Trading Bot Lab"]
summary: "V300 고지 — 레이아웃 대개편. 단일파일 진화기 47/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V300 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-12 12:17. 이 시리즈에 보존된 120개 버전 가운데 47번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v300_bot.py — 1,889줄</em></div>
<pre><code><span class="r">- # 1. 통계 관리자 (V210 일일/월간 금액 추적 연동)</span>
<span class="r">- self.filename = "upbit_v210_trade_stats.json"</span>
<span class="c">+ # 1. 통계 관리자 (V300 일일/월간 금액 추적 연동)</span>
<span class="g">+ self.filename = "upbit_v300_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v210_trade_stats.json", "upbit_v208_trade_stats.json", "upbit_v207_tr...</span>
<span class="g">+ def start_bot(self, bypass_prompt=False):</span>
<span class="g">+ summary_msg = f"======== [ SLOT {self.slot_id} ({ui_tkr}) V300 매매 계획 ] ========\n\n"</span>
<span class="g">+ summary_msg += "이 정밀한 V300 엔진 설정을 하드락(Lock-up) 승인하십니까?"</span>
<span class="g">+ if bypass_prompt:</span></code></pre>
</div>

## 무엇을 바꿨나

1,889줄. 'Ultra-Scanner & Layout' — 스캐너가 전 종목을 훑고, 화면은 슬롯 중심 레이아웃으로 재편됐다. 3백번대의 개막이다. 이 구간의 봇은 '종목을 고르는 봇'에서 '시장을 훑는 봇'으로 넘어가는 중이었다.

## 소회

번호가 100 단위로 뛸 때마다 야심도 함께 뛰었다. 그 야심의 절반만 살아남아도 봇은 진보했다.

> 니콜라스 다바스는 시장에 있는 시간보다 기록을 들여다본 시간이 자신을 만들었다고 했다. 아카이브를 정리하는 지금이 꼭 그렇다.

Developer: JH JEONG
