---
title: "[개발일지] UP.V092 — 업비트 CI를 입히다"
description: "UP.V092 · Upbit CI & Dynamic UI"
date: 2026-06-03T14:51:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "업비트 CI를 입히다. 단일파일 진화기 2/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V092 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-03 14:51. 이 시리즈에 보존된 120개 버전 가운데 2번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v92_bot.py — 1,534줄</em></div>
<pre><code><span class="r">- # 1. 전역 통계 관리자 (업비트 V91 규격)</span>
<span class="r">- self.filename = "upbit_v91_trade_stats.json"</span>
<span class="c">+ # 1. 전역 통계 관리자 (업비트 V92 규격)</span>
<span class="c">+ # 업비트 고유 패널 배경색 적용 (다크 네이비 계열)</span>
<span class="c">+ # 4. 메인 윈도우 (업비트 V92 동적 UI 및 CI 릴리즈)</span>
<span class="c">+ # 업비트 전용 CI 컬러 변수 설정</span>
<span class="g">+ self.filename = "upbit_v92_trade_stats.json"</span>
<span class="g">+ fallback_files = ["upbit_v91_trade_stats.json", "upbit_v90_trade_stats.json", "v91_trad...</span>
<span class="g">+ rec_seed = self.active_params.get("seed", self.def_data.get("seed", "1,000,000")) if se...</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1534줄. 직전 버전 대비 +31/-30줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **업비트 CI를 입히다**이다. 당시 주석이 의도를 증언한다 — "1. 전역 통계 관리자 (업비트 V92 규격)" / "업비트 고유 패널 배경색 적용 (다크 네이비 계열)"

## 소회

파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 워런 버핏은 썰물이 되면 누가 벌거벗고 수영했는지 드러난다고 했다. 안전장치는 밀물일 때 만들어야 한다 — 이 버전처럼.

Developer: JH JEONG
