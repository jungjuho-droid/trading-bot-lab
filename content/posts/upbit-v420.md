---
title: "[개발일지] UP.V420 — UI 픽스 패치"
description: "UP.V420 · Quantum UI Fix"
date: 2026-06-15T21:47:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "UI 픽스 패치. 단일파일 진화기 74/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V420 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-15 21:47. 이 시리즈에 보존된 120개 버전 가운데 74번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v420_bot.py — 2,013줄</em></div>
<pre><code><span class="r">- code_content = '''# -*- coding: utf-8 -*-</span>
<span class="r">- self.filename = "upbit_v416_trade_stats.json"</span>
<span class="c">+ # -*- coding: utf-8 -*-</span>
<span class="g">+ self.filename = "upbit_v420_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v416_trade_stats.json", "upbit_v415_trade_stats.json", "upbit_v414_tr...</span>
<span class="g">+ messagebox.showwarning(</span>
<span class="g">+ "보안 경고",</span>
<span class="g">+ "엔진이 가동 중입니다!\n"</span>
<span class="g">+ "코인 변경을 위해 먼저 [STOP] 하십시오."</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 2013줄. 직전 버전 대비 +132/-80줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **UI 픽스 패치**이다. 당시 주석이 의도를 증언한다 — "-*- coding: utf-8 -*-"

## 소회

이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 리처드 데니스는 규칙은 가르칠 수 있어도 확신은 가르칠 수 없다고 했다. 확신은 이렇게 버전을 쌓으며 스스로 만든다.

Developer: JH JEONG
