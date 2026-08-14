---
title: "[개발일지] VVWAP.V101 — VV의 탄생 — VVWAP 엔진 1호"
description: "VVWAP.V101 · The Birth of VV: VVWAP Engine No.1"
date: 2026-07-16T09:00:00+09:00
draft: false
series: ["VVWAP기"]
tags: ["개발일지", "VVWAP기", "자동매매", "업비트", "VWAP", "Trading Bot Lab"]
summary: "VV의 탄생 — VVWAP 엔진 1호. VVWAP기 1/27."
---

## 배경

이 글은 VVWAP기 — VV의 기원의 한 페이지, VVWAP.V101 의 기록이다. 앵커드 VWAP 기반으로 재설계한 시기로, 현행 VV 넘버링이 여기서 시작된다. 이 시리즈에 보존된 27개 버전 가운데 2번째 기록이다. 원본 파일 시각이 소실된 EC2 복원본이라, 게시일은 버전 순서에 따라 시대 구간 안에 배정했다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>VV101.py — 693줄</em></div>
<pre><code><span class="c"># [ 설정 구역 ]</span>
<span class="c"># [ 코어 파라미터 ]</span>
<span class="c"># [ 'KRW-USDT', 'KRW-USDC', 'KRW-TUSD', 'KRW-DAI', 'KRW-USDP' ]</span>
<span class="c"># [ 'KRW-AERGO' ]</span>
<span class="g">(시리즈 첫 보존본 — diff 기준점)</span></code></pre>
</div>

## 무엇을 바꿨나

**현행 봇 이름 'VV'가 태어난 지점이다.** UPBIT HYBRID ENGINE VV101 — VWAP(거래량 가중 평균가)을 앵커로 삼는 엔진의 첫 보존본, 693줄. 스테이블 코인 제외 필터, 코어 파라미터 구획 등 이후 시리즈의 골격이 이미 서 있다. vv141의 'vv'는 버전 표기가 아니라 이 시리즈의 성(姓)이다.

## 소회

이름의 족보가 밝혀지는 순간은 늘 사소한 파일에서다. VV = VVWAP — 두 글자에 한 시대의 전략이 압축돼 있다.

> 니콜라스 다바스는 시장에 있는 시간보다 기록을 들여다본 시간이 자신을 만들었다고 했다. 아카이브를 정리하는 지금이 꼭 그렇다.

Developer: JH JEONG
