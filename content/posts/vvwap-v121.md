---
title: "[개발일지] VVWAP.V121 — RSI 게이트 조정"
description: "VVWAP.V121 · RSI Gate Tuning"
date: 2026-07-22T09:32:00+09:00
draft: false
series: ["VVWAP기"]
tags: ["개발일지", "VVWAP기", "자동매매", "업비트", "RSI", "Trading Bot Lab"]
summary: "RSI 게이트 조정. VVWAP기 19/27."
---

## 배경

이 글은 VVWAP기 — VV의 기원의 한 페이지, VVWAP.V121 의 기록이다. 앵커드 VWAP 기반으로 재설계한 시기로, 현행 VV 넘버링이 여기서 시작된다. 이 시리즈에 보존된 27개 버전 가운데 20번째 기록이다. 원본 파일 시각이 소실된 EC2 복원본이라, 게시일은 버전 순서에 따라 시대 구간 안에 배정했다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>VV121.py — 915줄</em></div>
<pre><code><span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE VV120 (VWAP + Alt B, 타임스탑 완전 제거)</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE VV121 (매수 직후 보호창 등록 시차 수정)</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [VV121 전용 파라미터]</span>
<span class="c">+ # [VV121 패치] 방금 매수한 코인이 계좌 반영 시차로 account_cache_loop에 의해</span>
<span class="g">+ VERSION = "VV121"</span>
<span class="g">+ STATE_FILE = "UPBIT_ENGINE_VV121_STATE.json"</span>
<span class="g">+ sold_protection_list[ticker] = time.time() + TRADE_SYNC_GRACE_SEC</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 915줄. 직전 버전 대비 +12/-8줄 — 미세 조정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **RSI 게이트 조정**이다. 당시 주석이 의도를 증언한다 — "[ 코어 파라미터 ] UPBIT HYBRID ENGINE VV121 (매수 직후 보호창 등록 시차 수정)" / "=============================================================================="

## 소회

이때부터 '기준선 대비 위치'로 생각하는 습관이 생겼다. 지금의 게이트 사고방식의 뿌리다. VV 라는 이름이 어디서 왔냐고 묻는다면 여기다 — VVWAP. 거래량 가중 평균가를 기준선 삼자는 발상이 그대로 이름이 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 제시 리버모어는 큰돈은 매매가 아니라 기다림이 벌어준다고 했다. 이 버전의 코드 몇 줄도 결국 기다림을 만드는 장치였다.

Developer: JH JEONG
