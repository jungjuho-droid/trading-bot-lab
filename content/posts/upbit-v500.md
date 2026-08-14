---
title: "[개발일지] UP.V500 — 스나이퍼의 등장"
description: "UP.V500 · Enter the Sniper"
date: 2026-06-16T20:04:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "전략실험", "눌림목전략", "Trading Bot Lab"]
summary: "스나이퍼의 등장. 단일파일 진화기 75/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V500 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-16 20:04. 이 시리즈에 보존된 120개 버전 가운데 75번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v500_bot.py — 1,990줄</em></div>
<pre><code><span class="r">- self.filename = "upbit_v420_trade_stats.json"</span>
<span class="r">- for fb in ["upbit_v416_trade_stats.json", "upbit_v415_trade_stats.json", "upbit_v414_tr...</span>
<span class="c">+ # 2. 업비트 API 엔진</span>
<span class="c">+ # wait_pct와 buy_reb_pct가 0.0인 경우는 Sniper Auto Buy 강제 진입을 위한 트릭 허용</span>
<span class="g">+ self.filename = "upbit_v500_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v420_trade_stats.json", "upbit_v416_trade_stats.json"]:</span>
<span class="g">+ messagebox.showwarning("보안 경고", "엔진이 가동 중입니다!\n코인 변경을 위해 먼저 [STOP] 하십시오.")</span>
<span class="g">+ title_text = f"■ SLOT {self.slot_id} [🔥 스나이퍼 대기]" if self.slot_id == 1 else f"■ SLOT {s...</span>
<span class="g">+ title_color = "#f43f5e" if self.slot_id == 1 else self.ci_blue</span></code></pre>
</div>

## 무엇을 바꿨나

'Sniper & Scalping Edition' — 5백번대의 개막과 함께 **스나이퍼**라는 개념이 들어왔다. 조건이 완벽하게 갖춰진 한 발만 노리는 정밀 진입 모드다. 아무 때나 쏘지 않고, 표적이 조준선에 들어올 때까지 기다린다. 눌림목 대기(v1.9)의 정신이 저격수의 어휘로 다시 태어난 것.

## 소회

방아쇠보다 조준이 어렵다는 걸 코드로 배우던 구간이다. 쏘지 않은 날이 수익이던 날도 많았다.

> 니콜라스 다바스는 시장에 있는 시간보다 기록을 들여다본 시간이 자신을 만들었다고 했다. 아카이브를 정리하는 지금이 꼭 그렇다.

Developer: JH JEONG
