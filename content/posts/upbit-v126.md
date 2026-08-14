---
title: "[개발일지] UP.V126 — Quantum Final"
description: "UP.V126 · Quantum Final"
date: 2026-06-06T22:44:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "Quantum Final. 단일파일 진화기 35/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V126 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-06 22:44. 이 시리즈에 보존된 120개 버전 가운데 35번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v126_bot.py — 1,405줄</em></div>
<pre><code><span class="r">- # 1. 통계 관리자</span>
<span class="r">- self.filename = "upbit_v124_trade_stats.json"</span>
<span class="c">+ # 1. 통계 관리자 (V126 마이그레이션)</span>
<span class="c">+ # [핵심 패치 3] 메이저/중형/잡알트 맞춤형 3단계 하드코딩 프리셋 자동화</span>
<span class="c">+ # 콤보박스 선택/입력 시 프리셋 로드 자동 바인딩</span>
<span class="c">+ # [핵심 패치 2] 코인명 우측 실시간 리셋 타이머 배치</span>
<span class="g">+ self.filename = "upbit_v126_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v125_trade_stats.json", "upbit_v124_trade_stats.json"]:</span>
<span class="g">+ self.master_app.log(f"🚀 [Auto-Reset] 전량 청산 완료. 0.1초 내 타겟가 갱신 가동.")</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1405줄. 직전 버전 대비 +26/-25줄 — 미세 조정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **Quantum Final**이다. 당시 주석이 의도를 증언한다 — "1. 통계 관리자 (V126 마이그레이션)" / "[핵심 패치 3] 메이저/중형/잡알트 맞춤형 3단계 하드코딩 프리셋 자동화"

## 소회

이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 제시 리버모어는 시장은 결코 틀리지 않고 의견만 틀린다고 했다. 봇의 의견을 고치는 일, 그게 버전업이다.

Developer: JH JEONG
