---
title: "[개발일지] UP.V906 — 스나이퍼 권한 조정"
description: "UP.V906 · Sniper Demoted to Spotter & Perfect Trap"
date: 2026-06-22T20:25:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "전략실험", "Trading Bot Lab"]
summary: "스나이퍼 권한 조정. 단일파일 진화기 111/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V906 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-22 20:25. 이 시리즈에 보존된 120개 버전 가운데 111번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v906_bot.py — 1,734줄</em></div>
<pre><code><span class="r">- # 1. 통계 관리자 (V905)</span>
<span class="r">- self.filename = "upbit_v905_trade_stats.json"</span>
<span class="c">+ # 1. 통계 관리자 (V906)</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V906)</span>
<span class="c">+ # [V906 BUG FIX] 삭제된 불필요한 mode 조건문 로직. 이제 슬롯 변수에서 안전하게 바로 값을 가져옵니다.</span>
<span class="c">+ # 4. 메인 윈도우 (UPBIT V906)</span>
<span class="g">+ self.filename = "upbit_v906_trade_stats.json"</span>
<span class="g">+ popup = tk.Toplevel(self.root); popup.title(f"SLOT {self.slot_id} V906 스나이퍼 파라미터 정밀 설정")</span>
<span class="g">+ e_seed.insert(0, self.vars["seed"].get()); e_avg.insert(0, self.vars["manual_avg"].get(...</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1734줄. 직전 버전 대비 +53/-60줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **스나이퍼 권한 조정**이다. 당시 주석이 의도를 증언한다 — "1. 통계 관리자 (V906)" / "3. 개별 코인 슬롯 (V906)"

## 소회

버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 마크 더글러스는 시장이 아니라 자신의 규칙과 거래하라고 했다. 봇을 만든다는 건 그 규칙을 물리적으로 만드는 일이다.

Developer: JH JEONG
