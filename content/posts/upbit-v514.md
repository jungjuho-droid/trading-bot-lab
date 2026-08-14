---
title: "[개발일지] UP.V514 — 컴팩트 UI"
description: "UP.V514 · Compact UI"
date: 2026-06-19T23:22:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "컴팩트 UI. 단일파일 진화기 87/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V514 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-19 23:22. 이 시리즈에 보존된 120개 버전 가운데 87번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v514_bot.py — 2,212줄</em></div>
<pre><code><span class="r">- self.filename = "upbit_v515_trade_stats.json"</span>
<span class="r">- for fb in ["upbit_v513_trade_stats.json", "upbit_v512_trade_stats.json", "upbit_v511_tr...</span>
<span class="c">+ # 구버전 연동</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V514 가로 압축 UI 패치)</span>
<span class="c">+ # [V514] 가격 및 지표 정보를 상하 수직 배치하여 가로폭 축소</span>
<span class="c">+ # [V514] 파라미터 6개를 1행 6열에서 2행 3열 다단 구조로 변경하여 가로 폭 50% 절약</span>
<span class="g">+ self.filename = "upbit_v514_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v513_trade_stats.json", "upbit_v512_trade_stats.json"]:</span>
<span class="g">+ for i in range(3):</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 2212줄. 직전 버전 대비 +143/-134줄 — 대수술이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **컴팩트 UI**이다. 당시 주석이 의도를 증언한다 — "3. 개별 코인 슬롯 (V514 가로 압축 UI 패치)" / "[V514] 가격 및 지표 정보를 상하 수직 배치하여 가로폭 축소"

## 소회

파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 마크 미너비니는 손실을 작게 유지하는 것이 공격의 전제라고 했다. 방어 코드가 늘어날수록 진입은 오히려 과감해졌다.

Developer: JH JEONG
