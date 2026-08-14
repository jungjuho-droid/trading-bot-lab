---
title: "[개발일지] UP.V103 — 스윙과 방어의 결합"
description: "UP.V103 · Swing & Defense - Hardcoded API"
date: 2026-06-04T20:33:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "스윙과 방어의 결합. 단일파일 진화기 12/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V103 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-04 20:33. 이 시리즈에 보존된 120개 버전 가운데 12번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v103_bot.py — 1,612줄</em></div>
<pre><code><span class="r">- self.filename = "upbit_v102_trade_stats.json"</span>
<span class="r">- fallback_files = ["upbit_v101_trade_stats.json", "upbit_v100_trade_stats.json", "upbit_...</span>
<span class="c">+ # 3. 개별 코인 슬롯 (UPBIT V103 스윙 감시 엔진)</span>
<span class="c">+ # 4. 메인 윈도우 (UPBIT V103 Swing Edition - Hardcoded API)</span>
<span class="c">+ # [V103] API Key 하드코딩 및 마스킹 처리 (새로운 키 반영)</span>
<span class="c">+ # [V103] API 입력 오류 원천 차단: 기존 config 내용과 관계없이 하드코딩된 API 강제 복구</span>
<span class="g">+ self.filename = "upbit_v103_trade_stats.json"</span>
<span class="g">+ fallback_files = ["upbit_v102_trade_stats.json", "upbit_v101_trade_stats.json", "upbit_...</span>
<span class="g">+ self.root.title("Upbit Auto-Trading Bot V103 (Swing &amp; Defense Edition - Hardcoded API)")</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1612줄. 직전 버전 대비 +25/-25줄 — 미세 조정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **스윙과 방어의 결합**이다. 당시 주석이 의도를 증언한다 — "3. 개별 코인 슬롯 (UPBIT V103 스윙 감시 엔진)" / "4. 메인 윈도우 (UPBIT V103 Swing Edition - Hardcoded API)"

## 소회

이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 에드 세이코타는 규칙을 지키는 것보다 지킬 수 있는 규칙을 만드는 게 먼저라고 했다. 파라미터 손질은 그 '지킬 수 있는'을 찾는 과정이었다.

Developer: JH JEONG
