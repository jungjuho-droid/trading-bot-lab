---
title: "[개발일지] UP.V511 — 피라미드 스나이퍼 정비"
description: "UP.V511 · Pyramid Multi-Sniper"
date: 2026-06-18T19:57:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "전략실험", "Trading Bot Lab"]
summary: "피라미드 스나이퍼 정비. 단일파일 진화기 84/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V511 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-18 19:57. 이 시리즈에 보존된 120개 버전 가운데 84번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v511_bot.py — 2,199줄</em></div>
<pre><code><span class="r">- self.filename = "upbit_v510_trade_stats.json"</span>
<span class="r">- for fb in ["upbit_v509_trade_stats.json", "upbit_v507_trade_stats.json", "upbit_v500_tr...</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V511 전체 스나이퍼 &amp; 옵션 동기화 완료)</span>
<span class="c">+ # [V511 핫픽스] 폰트 크기 10, fill="x" 적용, 텍스트 축소로 잘림 현상 원천 봉쇄</span>
<span class="c">+ # [V511 핫픽스] 텍스트 길이 최소화하여 UI 레이아웃 붕괴 방지</span>
<span class="c">+ # 4. 메인 윈도우 (UPBIT V511)</span>
<span class="g">+ self.filename = "upbit_v511_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v510_trade_stats.json", "upbit_v509_trade_stats.json", "upbit_v500_tr...</span>
<span class="g">+ self.vars["tf"].set("15")</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 2199줄. 직전 버전 대비 +160/-304줄 — 대수술이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **피라미드 스나이퍼 정비**이다. 당시 주석이 의도를 증언한다 — "3. 개별 코인 슬롯 (V511 전체 스나이퍼 & 옵션 동기화 완료)" / "[V511 핫픽스] 폰트 크기 10, fill="x" 적용, 텍스트 축소로 잘림 현상 원천 봉쇄"

## 소회

이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 짐 로저스는 아무것도 하지 않는 것도 포지션이라고 했다. 진입하지 않게 만드는 코드가 진입 코드보다 늘 길었다.

Developer: JH JEONG
