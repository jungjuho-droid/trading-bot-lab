---
title: "[개발일지] MACRO.V036_ALT — RSI 게이트 조정"
description: "MACRO.V036_ALT · RSI Gate Tuning"
date: 2026-07-11T08:39:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "RSI", "스캐너", "Trading Bot Lab"]
summary: "RSI 게이트 조정. 병렬 실험기 72/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V036.ALT 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 25번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO036 (1).py — 744줄</em></div>
<pre><code><span class="r">- await log_queue.put(f"[{C_YELLOW}동기화{C_RESET}] 미보유 코인({ghost}) 슬롯 자동 회수")</span>
<span class="r">- await log_queue.put(f"{C_CYAN}[{VERSION} 스캐너]{C_RESET} 매수 타겟 {len(coin_memory)}개 분석 완료 ...</span>
<span class="g">+ await log_queue.put(f"[\033[93m동기화\033[0m] 미보유 코인({ghost}) 슬롯 자동 회수")</span>
<span class="g">+ await log_queue.put(f"\033[96m[{VERSION} 스캐너]\033[0m 매수 타겟 {len(coin_memory)}개 분석 완료 (B...</span>
<span class="g">+ await log_queue.put(f"[\033[91m전역격리\033[0m] {msg}")</span>
<span class="g">+ await log_queue.put(f"[\033[92m매수/BUY\033[0m] {ticker} | 진입가: {price:,.0f} | 기어: {gear_...</span>
<span class="g">+ status_str = f"[TR ON] 컷: {drop - (TR_DROP*100):&gt;+6.2f}%"</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 744줄. 직전 버전 대비 +5/-5줄 — 미세 조정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **RSI 게이트 조정**이다. 바뀐 코드의 단서: `await log_queue.put(f"[\033[93m동기화\033[0m] 미보유 코`, `await log_queue.put(f"\033[96m[{VERSION} 스캐너]\03`.

## 소회

시장 전체를 읽고 들어가겠다는 야심이었다. 절반은 과욕이었고, 절반은 지금의 레짐 차단으로 살아남았다. 매크로 지표는 느리고 코인은 빠르다. 이 속도 차이를 극복하지 못한 것이 이 계열의 사인(死因)이다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 알렉산더 엘더는 훌륭한 매매 기록이 훌륭한 트레이더를 만든다고 했다. 버전 파일 하나하나가 나에겐 그 기록이었다.

Developer: JH JEONG
