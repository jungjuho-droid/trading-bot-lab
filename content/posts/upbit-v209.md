---
title: "[개발일지] UP.V209 — 79줄짜리 보존본"
description: "UP.V209 · A 79-Line Fragment"
date: 2026-06-12T09:21:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "스캐너", "Trading Bot Lab"]
summary: "79줄짜리 보존본. 단일파일 진화기 45/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V209 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-12 09:21. 이 시리즈에 보존된 120개 버전 가운데 45번째 기록이다. 이 보존본은 전체 파일이 아니라 당시 바꾼 부분만 남긴 스니펫이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v209_bot.py — 79줄</em></div>
<pre><code><span class="r">- # -*- coding: utf-8 -*-</span>
<span class="r">- import tkinter as tk</span>
<span class="c">+ # 4시간봉(240분) 30개 데이터 수집</span>
<span class="c">+ # 14 캔들 기준 RSI 계산</span>
<span class="g">+ import requests</span>
<span class="g">+ import pandas as pd</span>
<span class="g">+ def get_4h_oversold_and_rebound():</span>
<span class="g">+ url = "https://api.upbit.com/v1/market/all"</span>
<span class="g">+ markets = requests.get(url).json()</span></code></pre>
</div>

## 무엇을 바꿨나

이 보존본은 79줄뿐이다 — 전체 파일이 아니라 그날 바꾼 부분만 저장한 스니펫이다. bt_v1_18과 같은 패턴. 스캐너 개편 구간(V208~V210)의 한복판이라, 바뀐 조각만 떼어 백업한 것으로 추정한다.

## 소회

조각만 남은 버전도 계보의 일부다. 완전한 기록보다 정직한 기록이 낫다.

> 마크 미너비니는 손실을 작게 유지하는 것이 공격의 전제라고 했다. 방어 코드가 늘어날수록 진입은 오히려 과감해졌다.

Developer: JH JEONG
