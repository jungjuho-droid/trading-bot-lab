---
title: "[개발일지] UP.V405 — 한 줄 제어 다듬기"
description: "UP.V405 · Quantum One-Line Control"
date: 2026-06-12T19:02:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "한 줄 제어 다듬기. 단일파일 진화기 63/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V405 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-12 19:02. 이 시리즈에 보존된 120개 버전 가운데 63번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v405_bot.py — 1,875줄</em></div>
<pre><code><span class="r">- import uuid</span>
<span class="r">- # 1. 통계 관리자 (V401 일일/월간 금액 추적)</span>
<span class="c">+ # 1. 통계 관리자</span>
<span class="g">+ import uuid</span>
<span class="g">+ for period in ["daily", "weekly", "monthly"]:</span>
<span class="g">+ self.stats[period]["profit"] = self.stats[period].get("profit", 0.0) + amount</span>
<span class="g">+ def get_balance(self): return self._req('GET', '/accounts')</span>
<span class="g">+ def buy_market(self, ticker, krw_amount): return self._req('POST', '/orders', {'market'...</span>
<span class="g">+ def sell_market(self, ticker, volume): return self._req('POST', '/orders', {'market': f...</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1875줄. 직전 버전 대비 +918/-477줄 — 사실상의 재작성이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **한 줄 제어 다듬기**이다. 바뀐 코드의 단서: `import uuid`, `self.stats[period]["profit"] = self.stats[period`.

## 소회

파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 제시 리버모어는 시장은 결코 틀리지 않고 의견만 틀린다고 했다. 봇의 의견을 고치는 일, 그게 버전업이다.

Developer: JH JEONG
