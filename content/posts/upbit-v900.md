---
title: "[개발일지] UP.V900 — 걸작 선언"
description: "UP.V900 · The Masterpiece Declaration"
date: 2026-06-21T20:21:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "걸작 선언. 단일파일 진화기 108/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V900 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-21 20:21. 이 시리즈에 보존된 120개 버전 가운데 108번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v900_bot.py — 1,783줄</em></div>
<pre><code><span class="r">- # 1. 통계 관리자 (V806)</span>
<span class="r">- self.filename = "upbit_v806_trade_stats.json"</span>
<span class="c">+ # 1. 통계 관리자 (V900)</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V900)</span>
<span class="c">+ # 🔥 [V900] position_start_time을 API 호출 쉴드용으로 사용</span>
<span class="c">+ # 🔥 [V900] FocusOut 팝업 버그 영구 제거. 엔터와 선택으로만 작동.</span>
<span class="g">+ self.filename = "upbit_v900_trade_stats.json"</span>
<span class="g">+ popup = tk.Toplevel(self.root); popup.title(f"SLOT {self.slot_id} V900 스나이퍼 파라미터 정밀 설정")</span>
<span class="g">+ log_msg = f"🚀 [V900 수동 개입] {tkr} 강제 매수 완료 (금액: {buy_amt:,.0f}원)."</span></code></pre>
</div>

## 무엇을 바꿨나

'The Masterpiece - All Bugs Annihilated'. 9백번대의 개막을 자축하는 이름이다. 물론 다음 버전에서 또 버그가 잡힌다 — 이 시대 타이틀의 낙관은 언제나 하루짜리였다. 그래도 1,783줄로 정돈된 이 버전은 단일파일 시대의 완숙기를 대표한다.

## 소회

'모든 버그 전멸'이라고 쓴 다음 날 버그를 잡는 삶. 그 낙관과 배신의 반복이 개발이었다.

> 알렉산더 엘더는 훌륭한 매매 기록이 훌륭한 트레이더를 만든다고 했다. 버전 파일 하나하나가 나에겐 그 기록이었다.

Developer: JH JEONG
