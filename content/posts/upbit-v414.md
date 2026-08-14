---
title: "[개발일지] UP.V414 — UI 픽스 패치"
description: "UP.V414 · Quantum UI Fix"
date: 2026-06-12T20:55:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "UI 픽스 패치. 단일파일 진화기 71/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V414 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-12 20:55. 이 시리즈에 보존된 120개 버전 가운데 71번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v414_bot.py — 1,944줄</em></div>
<pre><code><span class="r">- self.filename = "upbit_v412_trade_stats.json"</span>
<span class="r">- for fb in ["upbit_v411_trade_stats.json", "upbit_v410_trade_stats.json", "upbit_v409_tr...</span>
<span class="c">+ # 기본 횡보장 값</span>
<span class="c">+ # 4. 메인 윈도우 (UPBIT V413)</span>
<span class="c">+ # ==========================================</span>
<span class="c">+ # [버그 패치] 일괄 프리셋 UI 오류 해결</span>
<span class="g">+ self.filename = "upbit_v413_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v412_trade_stats.json", "upbit_v411_trade_stats.json"]:</span>
<span class="g">+ preset = {"wr": "-6.0 / 2.0", "bd": "-5.0 / -8.0", "lr": "-8.0 / 24.0"}</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1944줄. 직전 버전 대비 +66/-48줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **UI 픽스 패치**이다. 당시 주석이 의도를 증언한다 — "4. 메인 윈도우 (UPBIT V413)" / "=========================================="

## 소회

버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 레이 달리오는 고통 더하기 반성이 진보라고 했다. 이 버전 번호가 곧 반성의 횟수다.

Developer: JH JEONG
