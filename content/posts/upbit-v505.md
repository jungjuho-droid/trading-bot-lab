---
title: "[개발일지] UP.V505 — 피라미드 스나이퍼 정비"
description: "UP.V505 · Pyramid Multi-Sniper"
date: 2026-06-24T20:08:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "전략실험", "Trading Bot Lab"]
summary: "피라미드 스나이퍼 정비. 단일파일 진화기 79/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V505 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 이 시리즈에 보존된 120개 버전 가운데 79번째 기록이다. 원본 파일 시각이 소실된 EC2 복원본이라, 게시일은 버전 순서에 따라 시대 구간 안에 배정했다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v505_bot.py — 2,199줄</em></div>
<pre><code><span class="r">- for fb in ["upbit_v503_trade_stats.json", "upbit_v502_trade_stats.json", "upbit_v500_tr...</span>
<span class="r">- # [V505] 모드 변수 추가 (1, 2번 슬롯은 스나이퍼 강제, 3, 4번은 선택 가능)</span>
<span class="c">+ # 슬롯별 원인분석 메시지 저장 변수</span>
<span class="c">+ # [V505] 모드 변수 설정 (1, 2번 슬롯은 스나이퍼 강제, 3, 4번은 선택 가능)</span>
<span class="c">+ # [원인 분석 병합 표기]</span>
<span class="g">+ for fb in ["upbit_v504_trade_stats.json", "upbit_v503_trade_stats.json", "upbit_v502_tr...</span>
<span class="g">+ self.reason_msg = "엔진 대기중"</span>
<span class="g">+ init_mode = "SNIPER" if self.slot_id in [1, 2] else "QUANTUM"</span>
<span class="g">+ self.slot_mode_var = tk.StringVar(value=init_mode)</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 2199줄. 직전 버전 대비 +81/-49줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **피라미드 스나이퍼 정비**이다. 당시 주석이 의도를 증언한다 — "슬롯별 원인분석 메시지 저장 변수" / "[V505] 모드 변수 설정 (1, 2번 슬롯은 스나이퍼 강제, 3, 4번은 선택 가능)"

## 소회

파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 제시 리버모어는 큰돈은 매매가 아니라 기다림이 벌어준다고 했다. 이 버전의 코드 몇 줄도 결국 기다림을 만드는 장치였다.

Developer: JH JEONG
