---
title: "[개발일지] UP.V210 — 스캐너 개편"
description: "UP.V210 · Quantum Ultra-Scanner & Layout"
date: 2026-06-12T09:23:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "스캐너", "Trading Bot Lab"]
summary: "스캐너 개편. 단일파일 진화기 46/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V210 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-12 09:23. 이 시리즈에 보존된 120개 버전 가운데 46번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v210_bot.py — 1,739줄</em></div>
<pre><code><span class="r">- import time</span>
<span class="r">- def get_4h_oversold_and_rebound():</span>
<span class="c">+ # -*- coding: utf-8 -*-</span>
<span class="c">+ # ==========================================</span>
<span class="c">+ # [공통 유틸] 커스텀 확인 팝업창</span>
<span class="g">+ import tkinter as tk</span>
<span class="g">+ from tkinter import ttk, messagebox, scrolledtext</span>
<span class="g">+ import threading</span>
<span class="g">+ import time</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1739줄. 직전 버전 대비 +1731/-71줄 — 사실상의 재작성이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **스캐너 개편**이다. 당시 주석이 의도를 증언한다 — "-*- coding: utf-8 -*-" / "=========================================="

## 소회

파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 리처드 데니스는 규칙은 가르칠 수 있어도 확신은 가르칠 수 없다고 했다. 확신은 이렇게 버전을 쌓으며 스스로 만든다.

Developer: JH JEONG
