---
title: "[개발일지] UP.V502 — 피라미드 스나이퍼"
description: "UP.V502 · The Pyramid Sniper"
date: 2026-06-16T20:39:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "전략실험", "Trading Bot Lab"]
summary: "피라미드 스나이퍼. 단일파일 진화기 76/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V502 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-16 20:39. 이 시리즈에 보존된 120개 버전 가운데 76번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v502_bot.py — 2,113줄</em></div>
<pre><code><span class="r">- self.filename = "upbit_v500_trade_stats.json"</span>
<span class="r">- for fb in ["upbit_v420_trade_stats.json", "upbit_v416_trade_stats.json"]:</span>
<span class="c">+ # 스나이퍼 모드 비중 조절용 (Slot 1)</span>
<span class="c">+ # 익절 및 손절 (스나이퍼 모드 포함 공통)</span>
<span class="c">+ # 일반 분할 매수</span>
<span class="c">+ # 스나이퍼 최초 매수</span>
<span class="g">+ self.filename = "upbit_v502_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v500_trade_stats.json", "upbit_v420_trade_stats.json"]:</span>
<span class="g">+ self.sniper_max_pct_reached = 0</span></code></pre>
</div>

## 무엇을 바꿨나

'Pyramid Sniper' — 저격에 피라미딩이 결합됐다. 첫 발이 맞으면(수익 구간 진입) 포지션을 계단식으로 키우고, 빗나가면 바로 후퇴한다. 2,113줄 — 이 시대 최대 체급의 코드가 이 전략 실험에 투입됐다.

## 소회

이기는 판에만 판돈을 키운다 — 말은 쉽고 구현은 길었다. 2천 줄의 대부분이 '지금이 이기는 판인가'를 판정하는 코드였다.

> 윌리엄 오닐은 손절은 보험료라고 했다. 보험료 계산식을 고치는 날이 제일 많았다.

Developer: JH JEONG
