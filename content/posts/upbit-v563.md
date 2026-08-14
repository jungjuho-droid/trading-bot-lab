---
title: "[개발일지] UP.V563 — 스레드 세이프 스나이퍼"
description: "UP.V563 · The Thread-Safe Sniper"
date: 2026-06-21T09:21:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "전략실험", "Trading Bot Lab"]
summary: "스레드 세이프 스나이퍼. 단일파일 진화기 97/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V563 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-21 09:21. 이 시리즈에 보존된 120개 버전 가운데 97번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v563_bot.py — 2,043줄</em></div>
<pre><code><span class="r">- self.filename = "upbit_v562_trade_stats.json"</span>
<span class="r">- for fb in ["upbit_v561_trade_stats.json", "upbit_v560_trade_stats.json", "upbit_v552_tr...</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V563)</span>
<span class="c">+ # 🔥 [V563 픽스] UI 접근을 메인 스레드 큐로 안전하게 전달</span>
<span class="c">+ # 🔥 [V563 픽스] 백그라운드 스레드에서 UI .get() 직접 호출 방지 (안전한 캐시 데이터 사용)</span>
<span class="c">+ # 4. 메인 윈도우 (UPBIT V563)</span>
<span class="g">+ self.filename = "upbit_v563_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v562_trade_stats.json", "upbit_v561_trade_stats.json", "upbit_v560_tr...</span>
<span class="g">+ popup.title(f"SLOT {self.slot_id} V563 스나이퍼 파라미터 정밀 설정")</span></code></pre>
</div>

## 무엇을 바꿨나

'Thread-Safe Sniper Edition'. 빗썸 말기(V89)에서 배운 큐 기반 스레드 안전화가 업비트 대형 코드에도 적용됐다. 2,043줄로 감량하면서 UI 갱신과 매매 판단의 경계를 다시 그었다. 같은 병에는 같은 약 — 이번엔 처음부터 제대로 발랐다.

## 소회

교훈이 이식되는 속도가 빨라지고 있었다. 같은 버그를 두 번째 만나면 그건 버그가 아니라 시험이다.

> 마크 더글러스는 시장이 아니라 자신의 규칙과 거래하라고 했다. 봇을 만든다는 건 그 규칙을 물리적으로 만드는 일이다.

Developer: JH JEONG
