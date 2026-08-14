---
title: "[개발일지] UP.V700 — 택티컬 AI라는 이름의 조건 트리"
description: "UP.V700 · The 'Tactical AI' Condition Tree"
date: 2026-06-21T13:37:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "택티컬 AI라는 이름의 조건 트리. 단일파일 진화기 102/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V700 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-21 13:37. 이 시리즈에 보존된 120개 버전 가운데 102번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v700_bot.py — 2,084줄</em></div>
<pre><code><span class="r">- # 1. 통계 관리자 (V610)</span>
<span class="r">- self.filename = "upbit_v610_trade_stats.json"</span>
<span class="c">+ # 1. 통계 관리자 (V700)</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V700)</span>
<span class="c">+ # 🔥 [V700] 동적 손절 래칫 룰 변수</span>
<span class="c">+ # 🔥 [V700] 동적 손절 변수 초기화</span>
<span class="g">+ self.filename = "upbit_v700_trade_stats.json"</span>
<span class="g">+ self.current_soft_sl = saved_state.get("current_soft_sl", -99.0)</span>
<span class="g">+ self.highest_yield = saved_state.get("highest_yield", -99.0)</span></code></pre>
</div>

## 무엇을 바꿨나

'Zero-Bug & Tactical AI Edition'. 여기서 AI는 머신러닝이 아니라 **시장 국면별 조건 분기 트리**다 — 상승장/하락장/횡보장을 판정해 슬롯 전술을 바꾼다. 이름은 과장이지만 방향은 진짜였다. 시장 상태를 먼저 판정하고 전술을 고르는 사고방식이, 훗날 BTC 4시간봉 레짐 차단으로 완성된다.

## 소회

AI라는 말이 부끄럽지 않으려면 판정이 정직해야 했다. 조건 트리는 유행어보다 오래 살아남았다.

> 리처드 데니스는 규칙은 가르칠 수 있어도 확신은 가르칠 수 없다고 했다. 확신은 이렇게 버전을 쌓으며 스스로 만든다.

Developer: JH JEONG
