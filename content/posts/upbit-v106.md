---
title: "[개발일지] UP.V106 — 실시간 자산 평가"
description: "UP.V106 · Swing & Real-Time Asset Viewer"
date: 2026-06-04T21:28:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "실시간 자산 평가. 단일파일 진화기 15/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V106 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-04 21:28. 이 시리즈에 보존된 120개 버전 가운데 15번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v106_bot.py — 1,731줄</em></div>
<pre><code><span class="r">- # 1. 전역 통계 관리자</span>
<span class="r">- self.filename = "upbit_v105_trade_stats.json"</span>
<span class="c">+ # 1. 전역 통계 관리자 (V106 규격)</span>
<span class="c">+ # 3. 개별 코인 슬롯 (UPBIT V106 스윙 감시 엔진)</span>
<span class="c">+ # 4. 메인 윈도우 (UPBIT V106 Swing Edition - Asset Viewer)</span>
<span class="c">+ # [V105 -&gt; V106 개선] 보유 자산 전체 리스트 팝업 띄우기</span>
<span class="g">+ self.filename = "upbit_v106_trade_stats.json"</span>
<span class="g">+ fallback_files = ["upbit_v105_trade_stats.json", "upbit_v104_trade_stats.json", "upbit_...</span>
<span class="g">+ self.root.title("Upbit Auto-Trading Bot V106 (Swing Edition &amp; Real-Time Asset Viewer)")</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1731줄. 직전 버전 대비 +24/-24줄 — 미세 조정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **실시간 자산 평가**이다. 당시 주석이 의도를 증언한다 — "1. 전역 통계 관리자 (V106 규격)" / "3. 개별 코인 슬롯 (UPBIT V106 스윙 감시 엔진)"

## 소회

이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 레이 달리오는 고통 더하기 반성이 진보라고 했다. 이 버전 번호가 곧 반성의 횟수다.

Developer: JH JEONG
