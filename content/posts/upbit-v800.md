---
title: "[개발일지] UP.V800 — 딥 씨 어쌔신과 유령 데이터"
description: "UP.V800 · Deep Sea Assassin & Ghost Data"
date: 2026-06-21T18:45:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "딥 씨 어쌔신과 유령 데이터. 단일파일 진화기 104/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V800 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-21 18:45. 이 시리즈에 보존된 120개 버전 가운데 104번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v800_bot.py — 1,765줄</em></div>
<pre><code><span class="r">- # 1. 통계 관리자 (V750)</span>
<span class="r">- self.filename = "upbit_v750_trade_stats.json"</span>
<span class="c">+ # 1. 통계 관리자 (V800)</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V800)</span>
<span class="c">+ # 🔥 [V800 유령 잔고 완벽 클리어 로직]</span>
<span class="g">+ self.filename = "upbit_v800_trade_stats.json"</span>
<span class="g">+ "tf": tk.StringVar(value=self.active_params.get("tf", self.def_data.get("tf", "60"))),</span>
<span class="g">+ popup = tk.Toplevel(self.root); popup.title(f"SLOT {self.slot_id} V800 스나이퍼 파라미터 정밀 설정")</span>
<span class="g">+ log_msg = f"🚀 [V800 수동 개입] {tkr} 강제 매수 완료 (금액: {buy_amt:,.0f}원)."</span></code></pre>
</div>

## 무엇을 바꿨나

'Deep Sea Assassin & Ghost Data'. 두 가지 사냥 — 깊은 저점(딥 씨)에서만 진입하는 어쌔신 모드, 그리고 **유령 데이터 사냥**: 거래소 API가 돌려주는 불완전한 응답(빈 캔들, 지연 체결)을 걸러내는 검증층이다. 전략과 데이터 위생이 같은 버전에서 다뤄졌다.

## 소회

시장보다 먼저 데이터와 싸워야 한다는 걸 8백번대에서 배웠다. 쓰레기 캔들 하나가 완벽한 로직을 무너뜨린다.

> 윌리엄 오닐은 손절은 보험료라고 했다. 보험료 계산식을 고치는 날이 제일 많았다.

Developer: JH JEONG
