---
title: "[개발일지] UP.V114 — 분할 프리미엄 정비"
description: "UP.V114 · HTS Scale-Premium Final"
date: 2026-06-05T22:33:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "분할 프리미엄 정비. 단일파일 진화기 23/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V114 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-05 22:33. 이 시리즈에 보존된 120개 버전 가운데 23번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v114_bot.py — 1,414줄</em></div>
<pre><code><span class="r">- # 3. 개별 코인 슬롯 (UPBIT V113 프리미엄 스케일 엔진)</span>
<span class="r">- # [V113 정밀도 복구] 누적 정밀 연산용 카운터 로드 보정</span>
<span class="c">+ # 3. 개별 코인 슬롯 (UPBIT V113 콤보박스 스케일 엔진)</span>
<span class="c">+ # [V113 핵심 패치] 티커 입력창을 드롭다운 선택형 콤보박스(Combobox)로 전면 교체 신설</span>
<span class="c">+ # 콤보박스 스타일 및 크기 보정 지정</span>
<span class="g">+ coin_list = [</span>
<span class="g">+ "", "BTC", "ETH", "SOL", "AERGO", "HIVE", "AVNT", "XRP", "DOGE", "ADA",</span>
<span class="g">+ "DOT", "MATIC", "LINK", "AVAX", "TRX", "ETC", "SAND", "MANA", "FLOW",</span>
<span class="g">+ "AXS", "STX", "IMX", "NEAR", "SUI", "SEI", "APT", "MASK", "ALGO", "WAVES"</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1414줄. 직전 버전 대비 +24/-29줄 — 미세 조정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **분할 프리미엄 정비**이다. 당시 주석이 의도를 증언한다 — "3. 개별 코인 슬롯 (UPBIT V113 콤보박스 스케일 엔진)" / "[V113 핵심 패치] 티커 입력창을 드롭다운 선택형 콤보박스(Combobox)로 전면 교체 신설"

## 소회

파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 제시 리버모어는 큰돈은 매매가 아니라 기다림이 벌어준다고 했다. 이 버전의 코드 몇 줄도 결국 기다림을 만드는 장치였다.

Developer: JH JEONG
