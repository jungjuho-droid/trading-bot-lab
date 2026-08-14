---
title: "[개발일지] VVWAP.V106 — 세이브 포인트"
description: "VVWAP.V106 · A Save Point"
date: 2026-07-17T16:13:00+09:00
draft: false
series: ["VVWAP기"]
tags: ["개발일지", "VVWAP기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "세이브 포인트. VVWAP기 5/27."
---

## 배경

이 글은 VVWAP기 — VV의 기원의 한 페이지, VVWAP.V106 의 기록이다. 앵커드 VWAP 기반으로 재설계한 시기로, 현행 VV 넘버링이 여기서 시작된다. 이 시리즈에 보존된 27개 버전 가운데 6번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>vvwap_v106</em></div>
<pre><code><span class="r">- import asyncio</span>
<span class="r">- import aiohttp</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 0줄. 직전 버전 대비 +0/-776줄 — 사실상의 재작성이다. 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **세이브 포인트**이다.

## 소회

이때부터 '기준선 대비 위치'로 생각하는 습관이 생겼다. 지금의 게이트 사고방식의 뿌리다. VV 라는 이름이 어디서 왔냐고 묻는다면 여기다 — VVWAP. 거래량 가중 평균가를 기준선 삼자는 발상이 그대로 이름이 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 제시 리버모어는 큰돈은 매매가 아니라 기다림이 벌어준다고 했다. 이 버전의 코드 몇 줄도 결국 기다림을 만드는 장치였다.

Developer: JH JEONG
