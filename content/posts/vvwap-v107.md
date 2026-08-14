---
title: "[개발일지] VVWAP.V107 — 웹소켓 안정화"
description: "VVWAP.V107 · Websocket Hardening"
date: 2026-07-18T09:02:00+09:00
draft: false
series: ["VVWAP기"]
tags: ["개발일지", "VVWAP기", "자동매매", "업비트", "알림", "웹소켓", "Trading Bot Lab"]
summary: "웹소켓 안정화. VVWAP기 6/27."
---

## 배경

이 글은 VVWAP기 — VV의 기원의 한 페이지, VVWAP.V107 의 기록이다. 앵커드 VWAP 기반으로 재설계한 시기로, 현행 VV 넘버링이 여기서 시작된다. 이 시리즈에 보존된 27개 버전 가운데 7번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>VV107.py — 792줄</em></div>
<pre><code><span class="c">+ # ==============================================================================</span>
<span class="c">+ # [ 설정 구역 ] API 키 및 텔레그램 설정</span>
<span class="g">+ import asyncio</span>
<span class="g">+ import aiohttp</span>
<span class="g">+ import websockets</span>
<span class="g">+ import json</span>
<span class="g">+ import time</span>
<span class="g">+ import os</span>
<span class="g">+ import sys</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 792줄. 직전 버전 대비 +792/-0줄 — 사실상의 재작성이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **웹소켓 안정화**이다. 당시 주석이 의도를 증언한다 — "==============================================================================" / "[ 설정 구역 ] API 키 및 텔레그램 설정"

## 소회

VV 라는 이름이 어디서 왔냐고 묻는다면 여기다 — VVWAP. 거래량 가중 평균가를 기준선 삼자는 발상이 그대로 이름이 됐다. 이때부터 '기준선 대비 위치'로 생각하는 습관이 생겼다. 지금의 게이트 사고방식의 뿌리다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 알렉산더 엘더는 훌륭한 매매 기록이 훌륭한 트레이더를 만든다고 했다. 버전 파일 하나하나가 나에겐 그 기록이었다.

Developer: JH JEONG
