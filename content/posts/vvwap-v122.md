---
title: "[개발일지] VVWAP.V122 — RSI 게이트 조정"
description: "VVWAP.V122 · RSI Gate Tuning"
date: 2026-07-22T13:20:00+09:00
draft: false
series: ["VVWAP기"]
tags: ["개발일지", "VVWAP기", "자동매매", "업비트", "RSI", "Trading Bot Lab"]
summary: "RSI 게이트 조정. VVWAP기 20/27."
---

## 배경

이 글은 VVWAP기 — VV의 기원의 한 페이지, VVWAP.V122 의 기록이다. 앵커드 VWAP 기반으로 재설계한 시기로, 현행 VV 넘버링이 여기서 시작된다. 이 시리즈에 보존된 27개 버전 가운데 21번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>VV122.py — 912줄</em></div>
<pre><code><span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE VV121 (매수 직후 보호창 등록 시차 수정)</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE VV122 (일 상승률 필터 추가)</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [VV122 패치] 일 상승률 필터 (역추세 진입 방지)</span>
<span class="g">+ VERSION = "VV122"</span>
<span class="g">+ STATE_FILE = "UPBIT_TRADING_STATE.json"  # [VV122] 버전 무관 고정 이름 (누적손익 유지)</span>
<span class="g">+ TRADE_LOG_FILE = "UPBIT_TRADES_HISTORY.json"  # 거래 이력 영구 저장</span>
<span class="g">+ TRADE_FEE = 0.0005</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 912줄. 직전 버전 대비 +171/-174줄 — 대수술이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **RSI 게이트 조정**이다. 당시 주석이 의도를 증언한다 — "[ 코어 파라미터 ] UPBIT HYBRID ENGINE VV122 (일 상승률 필터 추가)" / "=============================================================================="

## 소회

VV 라는 이름이 어디서 왔냐고 묻는다면 여기다 — VVWAP. 거래량 가중 평균가를 기준선 삼자는 발상이 그대로 이름이 됐다. 이때부터 '기준선 대비 위치'로 생각하는 습관이 생겼다. 지금의 게이트 사고방식의 뿌리다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 알렉산더 엘더는 훌륭한 매매 기록이 훌륭한 트레이더를 만든다고 했다. 버전 파일 하나하나가 나에겐 그 기록이었다.

Developer: JH JEONG
