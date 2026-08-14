---
title: "[개발일지] UP.V506 — 피라미드 스나이퍼 정비"
description: "UP.V506 · Pyramid Multi-Sniper"
date: 2026-06-17T18:21:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "전략실험", "Trading Bot Lab"]
summary: "피라미드 스나이퍼 정비. 단일파일 진화기 80/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V506 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-17 18:21. 이 시리즈에 보존된 120개 버전 가운데 80번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v506_bot.py — 2,305줄</em></div>
<pre><code><span class="r">- "wait_reb": tk.StringVar(value=self.active_params.get("wait_reb_str", self.def_data["wa...</span>
<span class="r">- "buy_ratio": tk.StringVar(value=self.active_params.get("buy_ratio_str", self.def_data["...</span>
<span class="c">+ # 퀀텀 모드 복원용 유저 파라미터 백업 저장소</span>
<span class="c">+ # 실시간 상태 전광판 연동용 메인 변수 풀</span>
<span class="g">+ self.quantum_backup_vars = {</span>
<span class="g">+ "wait_reb": self.active_params.get("wait_reb_str", self.def_data["wait_reb"]),</span>
<span class="g">+ "buy_ratio": self.active_params.get("buy_ratio_str", self.def_data["buy_ratio"]),</span>
<span class="g">+ "buy_drop": self.active_params.get("buy_drop_str", self.def_data["buy_drop"]),</span>
<span class="g">+ "tf": self.active_params.get("tf", self.def_data.get("tf", "240"))</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 2305줄. 직전 버전 대비 +226/-88줄 — 대수술이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **피라미드 스나이퍼 정비**이다. 당시 주석이 의도를 증언한다 — "퀀텀 모드 복원용 유저 파라미터 백업 저장소" / "실시간 상태 전광판 연동용 메인 변수 풀"

## 소회

버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 알렉산더 엘더는 훌륭한 매매 기록이 훌륭한 트레이더를 만든다고 했다. 버전 파일 하나하나가 나에겐 그 기록이었다.

Developer: JH JEONG
