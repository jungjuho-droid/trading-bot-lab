---
title: "[개발일지] UP.V400 — 한 줄 제어 — One-Line Control"
description: "UP.V400 · One-Line Control"
date: 2026-06-12T17:57:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "한 줄 제어 — One-Line Control. 단일파일 진화기 60/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V400 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-12 17:57. 이 시리즈에 보존된 120개 버전 가운데 60번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v400_bot.py — 1,406줄</em></div>
<pre><code><span class="r">- import threading, time, datetime, urllib.parse, hashlib, requests, json, os, math, gc, ...</span>
<span class="r">- # 1. 통계 관리자 (V321 일일/월간 금액 추적)</span>
<span class="c">+ # 1. 통계 관리자 (V400 일일/월간 금액 추적)</span>
<span class="c">+ # 업비트의 경우 accounts 자체가 리스트로 반환됨</span>
<span class="g">+ import threading</span>
<span class="g">+ import time</span>
<span class="g">+ import datetime</span>
<span class="g">+ import urllib.parse</span>
<span class="g">+ import hashlib</span></code></pre>
</div>

## 무엇을 바꿨나

1,406줄로 다시 감량하며 'One-Line Control'이라는 이름을 달았다. 슬롯 하나의 상태·조작을 터미널 한 줄에 압축해 표시/제어하는 체계다. 화면을 쓰는 방식이 표 중심에서 행 중심으로 — 현행 터미널 대시보드의 '슬롯 한 줄 표기'가 여기서 원형을 얻는다.

## 소회

한 줄에 담기지 않는 상태는 대개 설계가 덜 된 상태였다. 압축은 표시의 문제가 아니라 사고의 문제였다.

> 리처드 데니스는 규칙은 가르칠 수 있어도 확신은 가르칠 수 없다고 했다. 확신은 이렇게 버전을 쌓으며 스스로 만든다.

Developer: JH JEONG
