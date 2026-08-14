---
title: "[개발일지] VVWAP.V128 — RSI 게이트 조정"
description: "VVWAP.V128 · RSI Gate Tuning"
date: 2026-07-23T20:34:00+09:00
draft: false
series: ["VVWAP기"]
tags: ["개발일지", "VVWAP기", "자동매매", "업비트", "RSI", "Trading Bot Lab"]
summary: "RSI 게이트 조정. VVWAP기 24/27."
---

## 배경

이 글은 VVWAP기 — VV의 기원의 한 페이지, VVWAP.V128 의 기록이다. 앵커드 VWAP 기반으로 재설계한 시기로, 현행 VV 넘버링이 여기서 시작된다. 이 시리즈에 보존된 27개 버전 가운데 25번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>VV128.py — 1,030줄</em></div>
<pre><code><span class="r">- VERSION = "VV127"</span>
<span class="r">- DAILY_TRADE_COOLDOWN_SEC = 36000    # 같은 날 거래 후 10시간 격리</span>
<span class="c">+ # [VV127 패치] 당일 거래 기록 초기화</span>
<span class="c">+ # [VV127 패치] 수동 청산도 같은 날 거래로 기록 → 10일 격리 + 당일만 재진입 불가</span>
<span class="c">+ # [VV127 패치] 당일 중복매매 방지 - 같은 날에 이미 거래한 코인 차단</span>
<span class="c">+ # [VV127 패치] 격리: 전체 10일(QUARANTINE_SEC) + 당일 기록(daily_trade_record)</span>
<span class="g">+ VERSION = "VV128"</span>
<span class="g">+ global daily_trade_record</span>
<span class="g">+ daily_trade_record = {}</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1030줄. 직전 버전 대비 +16/-9줄 — 미세 조정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **RSI 게이트 조정**이다. 당시 주석이 의도를 증언한다 — "[VV127 패치] 당일 거래 기록 초기화" / "[VV127 패치] 수동 청산도 같은 날 거래로 기록 → 10일 격리 + 당일만 재진입 불가"

## 소회

이때부터 '기준선 대비 위치'로 생각하는 습관이 생겼다. 지금의 게이트 사고방식의 뿌리다. VV 라는 이름이 어디서 왔냐고 묻는다면 여기다 — VVWAP. 거래량 가중 평균가를 기준선 삼자는 발상이 그대로 이름이 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 짐 로저스는 아무것도 하지 않는 것도 포지션이라고 했다. 진입하지 않게 만드는 코드가 진입 코드보다 늘 길었다.

Developer: JH JEONG
