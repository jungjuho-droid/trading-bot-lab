---
title: "[개발일지] UP.V124 — 파이널 프루프 검증"
description: "UP.V124 · Quantum Final Proof"
date: 2026-06-06T22:08:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "파이널 프루프 검증. 단일파일 진화기 33/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V124 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-06 22:08. 이 시리즈에 보존된 120개 버전 가운데 33번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v124_bot.py — 1,404줄</em></div>
<pre><code><span class="r">- self.filename = "upbit_v123_trade_stats.json"</span>
<span class="r">- for fb in ["upbit_v122_trade_stats.json", "upbit_v121_trade_stats.json", "upbit_v120_tr...</span>
<span class="c">+ # 3단계 하드코딩 프리셋 자동 매핑</span>
<span class="g">+ self.filename = "upbit_v124_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v123_trade_stats.json", "upbit_v122_trade_stats.json"]:</span>
<span class="g">+ self.last_ui_states = {"cp": "", "avg": "", "eval": "", "mb": "", "ms": "", "tgt": "", ...</span>
<span class="g">+ def auto_preset(self, event=None):</span>
<span class="g">+ if self.bot_state == "MONITORING":</span>
<span class="g">+ messagebox.showwarning("보안 경고", "엔진이 가동 중입니다!\n코인 변경을 위해 먼저 [STOP] 하십시오.")</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1404줄. 직전 버전 대비 +107/-69줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **파이널 프루프 검증**이다. 당시 주석이 의도를 증언한다 — "3단계 하드코딩 프리셋 자동 매핑"

## 소회

버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 니콜라스 다바스는 시장에 있는 시간보다 기록을 들여다본 시간이 자신을 만들었다고 했다. 아카이브를 정리하는 지금이 꼭 그렇다.

Developer: JH JEONG
