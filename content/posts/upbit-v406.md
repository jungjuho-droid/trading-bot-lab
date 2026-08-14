---
title: "[개발일지] UP.V406 — 한 줄 제어 다듬기"
description: "UP.V406 · Quantum One-Line Control"
date: 2026-06-12T19:09:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "한 줄 제어 다듬기. 단일파일 진화기 64/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V406 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-12 19:09. 이 시리즈에 보존된 120개 버전 가운데 64번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v406_bot.py — 1,883줄</em></div>
<pre><code><span class="r">- self.filename = "upbit_v401_trade_stats.json"</span>
<span class="r">- for fb in ["upbit_v400_trade_stats.json", "upbit_v303_trade_stats.json"]:</span>
<span class="c">+ # [V406 완벽 픽스] V303과 동일한 구조의 안전한 파라미터 팝업 창</span>
<span class="c">+ # 4. 메인 윈도우 (UPBIT V406 One-Line &amp; Fixed Mode)</span>
<span class="g">+ self.filename = "upbit_v406_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v405_trade_stats.json", "upbit_v401_trade_stats.json", "upbit_v303_tr...</span>
<span class="g">+ def get_balance(self):</span>
<span class="g">+ res = self._req('GET', '/accounts')</span>
<span class="g">+ if res.get("status") == "0000": return {"status": "0000", "data": res["data"]}</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1883줄. 직전 버전 대비 +54/-46줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **한 줄 제어 다듬기**이다. 당시 주석이 의도를 증언한다 — "[V406 완벽 픽스] V303과 동일한 구조의 안전한 파라미터 팝업 창" / "4. 메인 윈도우 (UPBIT V406 One-Line & Fixed Mode)"

## 소회

파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 브루스 코브너는 자신이 틀릴 수 있는 지점을 미리 정해두는 것이 포지션의 전부라고 했다. 파라미터 파일이 곧 그 지점들의 목록이다.

Developer: JH JEONG
