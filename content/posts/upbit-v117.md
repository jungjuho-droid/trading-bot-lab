---
title: "[개발일지] UP.V117 — 분할 매수/매도 체계"
description: "UP.V117 · Quantum Scale-In/Out Premium"
date: 2026-06-06T01:36:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "분할 매수/매도 체계. 단일파일 진화기 26/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V117 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-06 01:36. 이 시리즈에 보존된 120개 버전 가운데 26번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v117_bot.py — 1,330줄</em></div>
<pre><code><span class="r">- # [공통 유틸] 커스텀 확인 팝업창</span>
<span class="r">- dialog.grab_set()</span>
<span class="c">+ # [공통 유틸] 커스텀 확인 팝업창 (V116 렌더링 동기화 패치)</span>
<span class="c">+ # [V116 패치] 리눅스/우분투 환경 grab_set 크래시 방지를 위한 렌더링 대기 동기화</span>
<span class="c">+ # 1. 통계 관리자 (V116 규격 - 영구 보존)</span>
<span class="c">+ # 3. 개별 코인 슬롯 (V116 퀀텀 엔진)</span>
<span class="g">+ dialog.wait_visibility()</span>
<span class="g">+ dialog.grab_set()</span>
<span class="g">+ self.filename = "upbit_v116_trade_stats.json"</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1330줄. 직전 버전 대비 +40/-44줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **분할 매수/매도 체계**이다. 당시 주석이 의도를 증언한다 — "[공통 유틸] 커스텀 확인 팝업창 (V116 렌더링 동기화 패치)" / "[V116 패치] 리눅스/우분투 환경 grab_set 크래시 방지를 위한 렌더링 대기 동기화"

## 소회

파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 에드 세이코타는 규칙을 지키는 것보다 지킬 수 있는 규칙을 만드는 게 먼저라고 했다. 파라미터 손질은 그 '지킬 수 있는'을 찾는 과정이었다.

Developer: JH JEONG
