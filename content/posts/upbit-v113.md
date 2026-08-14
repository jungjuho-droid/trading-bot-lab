---
title: "[개발일지] UP.V113 — 분할 프리미엄 정비"
description: "UP.V113 · HTS Scale-Premium Final"
date: 2026-06-05T22:25:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "분할 프리미엄 정비. 단일파일 진화기 22/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V113 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-05 22:25. 이 시리즈에 보존된 120개 버전 가운데 22번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v113_bot.py — 1,419줄</em></div>
<pre><code><span class="r">- # 1. 전역 통계 관리자 (V112 규격)</span>
<span class="r">- self.filename = "upbit_v112_trade_stats.json"</span>
<span class="c">+ # 1. 전역 통계 관리자 (V113 규격)</span>
<span class="c">+ # 3. 개별 코인 슬롯 (UPBIT V113 프리미엄 스케일 엔진)</span>
<span class="c">+ # [V113 정밀도 복구] 누적 정밀 연산용 카운터 로드 보정</span>
<span class="c">+ # [선생님 기획 반영] 3차 FULL 배팅이 완료된 최후 상태에서만 최종 보정 합성 평단가 기준 SL 마지노선 작동</span>
<span class="g">+ self.filename = "upbit_v113_trade_stats.json"</span>
<span class="g">+ fallback_files = ["upbit_v112_trade_stats.json", "upbit_v111_trade_stats.json", "upbit_...</span>
<span class="g">+ self.cum_krw = saved_state.get("cum_krw", 0.0)</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1419줄. 직전 버전 대비 +53/-28줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **분할 프리미엄 정비**이다. 당시 주석이 의도를 증언한다 — "1. 전역 통계 관리자 (V113 규격)" / "3. 개별 코인 슬롯 (UPBIT V113 프리미엄 스케일 엔진)"

## 소회

버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 브루스 코브너는 자신이 틀릴 수 있는 지점을 미리 정해두는 것이 포지션의 전부라고 했다. 파라미터 파일이 곧 그 지점들의 목록이다.

Developer: JH JEONG
