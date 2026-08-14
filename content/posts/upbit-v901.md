---
title: "[개발일지] UP.V901 — 스나이퍼, 관측수로 강등되다"
description: "UP.V901 · Sniper Demoted to Spotter"
date: 2026-06-21T20:56:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "전략실험", "Trading Bot Lab"]
summary: "스나이퍼, 관측수로 강등되다. 단일파일 진화기 109/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V901 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-21 20:56. 이 시리즈에 보존된 120개 버전 가운데 109번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v901_bot.py — 1,741줄</em></div>
<pre><code><span class="r">- # 1. 통계 관리자 (V900)</span>
<span class="r">- self.filename = "upbit_v900_trade_stats.json"</span>
<span class="c">+ # 1. 통계 관리자 (V901)</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V901)</span>
<span class="c">+ # 🔥 [V901] STOP 상태에서는 절대 화면 강제 클리어하지 않음 (수동 입력 완벽 보장)</span>
<span class="g">+ self.filename = "upbit_v901_trade_stats.json"</span>
<span class="g">+ popup = tk.Toplevel(self.root); popup.title(f"SLOT {self.slot_id} V901 스나이퍼 파라미터 정밀 설정")</span>
<span class="g">+ if mode == "Bull":</span>
<span class="g">+ p_wr = "-0.0 / 0.0"; p_br = "100 / 0 / 0"; p_bd = "-99.0 / -99.0"; p_st = "7.0 / 12.0 /...</span></code></pre>
</div>

## 무엇을 바꿨나

이 시대 최고의 타이틀 — **'Sniper Demoted to Spotter'**. 스나이퍼 모드가 방아쇠를 뺏기고 관측수로 강등됐다. 정밀 진입 로직이 직접 쏘는 대신, 신호를 보고하고 최종 결정은 메인 엔진이 내린다. 실전에서 스나이퍼의 단독 판단이 사고를 냈다는 추정이 자연스럽다. 권한 회수를 이렇게 정직하게 이름에 적은 버전은 이것뿐이다.

## 소회

잘 쏘는 놈에게서 방아쇠를 뺏는 결정 — 사람 조직이었으면 못 했을 인사를 코드에선 하루 만에 했다.

> 폴 튜더 존스는 어제의 가격이 아니라 오늘의 리스크를 보라고 했다. 패치는 언제나 오늘의 리스크가 시켰다.

Developer: JH JEONG
