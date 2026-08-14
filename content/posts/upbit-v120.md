---
title: "[개발일지] UP.V120 — 리눅스 안정화"
description: "UP.V120 · Quantum Linux-Stable"
date: 2026-06-06T02:24:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "리눅스 안정화. 단일파일 진화기 29/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V120 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-06 02:24. 이 시리즈에 보존된 120개 버전 가운데 29번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v120_bot.py — 1,349줄</em></div>
<pre><code><span class="r">- # [공통 유틸] 커스텀 확인 팝업창 (V117 우분투 렌더링 완벽 동기화 유지)</span>
<span class="r">- # 1. 통계 관리자 (V119 규격)</span>
<span class="c">+ # [공통 유틸] 커스텀 확인 팝업창</span>
<span class="c">+ # 1. 통계 관리자 (V120 규격)</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V120 퀀텀 + 수동물량 인식 패치)</span>
<span class="c">+ # [V120 패치] 수동/보유 물량 텍스트 출력 네모 괄호 제거</span>
<span class="g">+ self.filename = "upbit_v120_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v119_trade_stats.json", "upbit_v118_trade_stats.json", "upbit_v117_tr...</span>
<span class="g">+ if self.buy_step == 0: sign_str = f"🖐️ 수동/보유 물량 ➔ 1차 익절 감시중"</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1349줄. 직전 버전 대비 +25/-23줄 — 미세 조정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **리눅스 안정화**이다. 당시 주석이 의도를 증언한다 — "[공통 유틸] 커스텀 확인 팝업창" / "1. 통계 관리자 (V120 규격)"

## 소회

버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 레이 달리오는 고통 더하기 반성이 진보라고 했다. 이 버전 번호가 곧 반성의 횟수다.

Developer: JH JEONG
