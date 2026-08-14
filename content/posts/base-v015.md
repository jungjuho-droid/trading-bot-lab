---
title: "[개발일지] BASE.V015 — 웹소켓 안정화"
description: "BASE.V015 · Websocket Hardening"
date: 2026-07-08T09:40:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "웹소켓", "Trading Bot Lab"]
summary: "웹소켓 안정화. 병렬 실험기 46/108."
---

## 배경

이 글은 BASE 실험기의 한 페이지, BASE.V015 의 기록이다. 바닥권 지지선 진입(Bottom Area Support Entry)이라는 단일 아이디어를 파고든 계열이다. 이 시리즈에 보존된 11개 버전 가운데 10번째 기록이다. 원본 파일 시각이 소실된 EC2 복원본이라, 게시일은 버전 순서에 따라 시대 구간 안에 배정했다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>BASE015.py — 1,051줄</em></div>
<pre><code><span class="r">- import datetime</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [ HYBRID TRADING ENGINE BASE015 ]</span>
<span class="c">+ # VER: v0.0.15 (BASE Smart Relaxation &amp; F-KNIFE Sniper Mode + Hotfix)</span>
<span class="g">+ import websockets</span>
<span class="g">+ import aiohttp</span>
<span class="g">+ import json</span>
<span class="g">+ import os</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1051줄. 직전 버전 대비 +1043/-98줄 — 사실상의 재작성이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **웹소켓 안정화**이다. 당시 주석이 의도를 증언한다 — "==============================================================================" / "[ HYBRID TRADING ENGINE BASE015 ]"

## 소회

이 실험 자체는 접었지만, '바닥 근처에서만 산다'는 유전자는 살아남아 현행 저점근접 게이트(24시간 저점 대비 +3% 이내)가 됐다. 지지선은 차트에서는 선명한데 코드로 쓰면 흐릿해진다. 정의를 숫자로 못 내리면 전략이 아니라는 걸 배웠다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 에드 세이코타는 규칙을 지키는 것보다 지킬 수 있는 규칙을 만드는 게 먼저라고 했다. 파라미터 손질은 그 '지킬 수 있는'을 찾는 과정이었다.

Developer: JH JEONG
