---
title: "[개발일지] UP.V119 — 리눅스 안정화 — 서버 시대의 예고"
description: "UP.V119 · Linux-Stable: A Server Era Foreshadowed"
date: 2026-06-06T02:07:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "리눅스 안정화 — 서버 시대의 예고. 단일파일 진화기 28/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V119 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-06 02:07. 이 시리즈에 보존된 120개 버전 가운데 28번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v119_bot.py — 1,347줄</em></div>
<pre><code><span class="r">- # 1. 통계 관리자 (V118 규격)</span>
<span class="r">- self.filename = "upbit_v118_trade_stats.json"</span>
<span class="c">+ # 1. 통계 관리자 (V119 규격)</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V119 퀀텀 + 수동물량 인식 패치)</span>
<span class="c">+ # [V119 UI 패치] 수동 매수/기존 보유 물량일 때 SYSTEM STANDBY로 빠지는 현상 교정</span>
<span class="c">+ # 4. 메인 윈도우 (UPBIT V119 퀀텀 HTS 리눅스 호환 터미널)</span>
<span class="g">+ self.filename = "upbit_v119_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v118_trade_stats.json", "upbit_v117_trade_stats.json", "upbit_v116_tr...</span>
<span class="g">+ self.master_app.send_telegram(log_msg)</span></code></pre>
</div>

## 무엇을 바꿨나

'Quantum Linux-Stable Edition'. 윈도우 PC에서 돌던 봇을 리눅스 환경에서 안정 구동하도록 손본 버전이다. 경로 처리, 인코딩, 터미널 출력 — 리눅스에서 어긋나는 지점들을 정리했다. 훗날 EC2 이주 시도(빗썸 v4.73)와 맥 이주로 이어지는 '서버에서 돌리고 싶다'는 욕망의 이른 물증이다.

## 소회

봇을 서버로 보내고 싶다는 건 결국 봇에게서 자유로워지고 싶다는 뜻이었다. 그 자유의 가격을 아직 모르던 때다.

> 짐 로저스는 아무것도 하지 않는 것도 포지션이라고 했다. 진입하지 않게 만드는 코드가 진입 코드보다 늘 길었다.

Developer: JH JEONG
