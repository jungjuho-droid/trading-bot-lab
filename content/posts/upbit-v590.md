---
title: "[개발일지] UP.V590 — 듀얼 코어 어쌔신"
description: "UP.V590 · The Dual-Core Assassin"
date: 2026-06-21T09:52:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "듀얼 코어 어쌔신. 단일파일 진화기 99/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V590 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-21 09:52. 이 시리즈에 보존된 120개 버전 가운데 99번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v590_bot.py — 2,232줄</em></div>
<pre><code><span class="r">- self.filename = "upbit_v570_trade_stats.json"</span>
<span class="r">- for fb in ["upbit_v563_trade_stats.json", "upbit_v562_trade_stats.json", "upbit_v561_tr...</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V590 완벽 격리 엔진)</span>
<span class="c">+ # 4. 메인 윈도우 (UPBIT V590)</span>
<span class="c">+ # 🔥 [V590 핵심] 듀얼 코어 스코어링 평가기</span>
<span class="c">+ # 공통 지표 계산</span>
<span class="g">+ self.filename = "upbit_v590_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v570_trade_stats.json", "upbit_v563_trade_stats.json", "upbit_v562_tr...</span>
<span class="g">+ popup.title(f"SLOT {self.slot_id} V590 스나이퍼 파라미터 정밀 설정")</span></code></pre>
</div>

## 무엇을 바꿨나

'Dual-Core Assassin Edition' — 성격이 다른 두 엔진을 한 봇 안에서 병렬 구동하는 실험이다. 슬롯 일부는 스윙, 일부는 초단타로 갈라 서로 다른 시장 국면을 맡겼다. 훗날 병렬 실험기(HY 하이브리드)의 사상이 단일 파일 안에서 먼저 시연된 셈이다.

## 소회

한 봇에 두 성격을 넣어보니 알겠더라 — 전략보다 어려운 게 전략들의 동거였다.

> 레이 달리오는 고통 더하기 반성이 진보라고 했다. 이 버전 번호가 곧 반성의 횟수다.

Developer: JH JEONG
