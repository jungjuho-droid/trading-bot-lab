---
title: "[개발일지] UP.V530 — 토탈 컨트롤"
description: "UP.V530 · Total Control"
date: 2026-06-21T00:46:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "토탈 컨트롤. 단일파일 진화기 91/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V530 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-21 00:46. 이 시리즈에 보존된 120개 버전 가운데 91번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v530_bot.py — 2,241줄</em></div>
<pre><code><span class="r">- self.filename = "upbit_v520_trade_stats.json"</span>
<span class="r">- for fb in ["upbit_v516_trade_stats.json", "upbit_v515_trade_stats.json", "upbit_v514_tr...</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V530 반응형 확장 패치 적용)</span>
<span class="c">+ # [V530] 야성 해방 모드 프리셋 유지</span>
<span class="c">+ # [V530] 수동 매매 영역 잘림 방지 (레이블과 입력칸 분리 및 확장)</span>
<span class="c">+ # 🔥 [V530 픽스] UI 체크박스 해제 시 필터 무조건 강제 패스 처리</span>
<span class="g">+ self.filename = "upbit_v530_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v520_trade_stats.json", "upbit_v516_trade_stats.json", "upbit_v515_tr...</span>
<span class="g">+ messagebox.showwarning("보안 경고", "엔진 가동 중입니다.\n파라미터 수정을 위해 먼저 [STOP] 하십시오.")</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 2241줄. 직전 버전 대비 +68/-60줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **토탈 컨트롤**이다. 당시 주석이 의도를 증언한다 — "3. 개별 코인 슬롯 (V530 반응형 확장 패치 적용)" / "[V530] 야성 해방 모드 프리셋 유지"

## 소회

파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 제시 리버모어는 시장은 결코 틀리지 않고 의견만 틀린다고 했다. 봇의 의견을 고치는 일, 그게 버전업이다.

Developer: JH JEONG
