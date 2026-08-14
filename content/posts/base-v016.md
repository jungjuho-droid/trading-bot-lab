---
title: "[개발일지] BASE.V016 — BASE의 최종형"
description: "BASE.V016 · BASE, Finalized"
date: 2026-07-08T09:43:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "VWAP", "눌림목전략", "Trading Bot Lab"]
summary: "BASE의 최종형. 병렬 실험기 47/108."
---

## 배경

이 글은 BASE 실험기의 한 페이지, BASE.V016 의 기록이다. 바닥권 지지선 진입(Bottom Area Support Entry)이라는 단일 아이디어를 파고든 계열이다. 이 시리즈에 보존된 11개 버전 가운데 11번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>BASE016.py — 1,051줄</em></div>
<pre><code><span class="r">- # [ HYBRID TRADING ENGINE BASE015 ]</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ HYBRID TRADING ENGINE BASE016 ]</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # VER: v0.0.16 (BASE Deep Retracement Relaxation)</span>
<span class="c">+ # DESC: BASE_RET_MAX 68% -&gt; 80% 완화 (깊은 눌림목 및 덤핑 허용하여 매수 빈도 극대화)</span>
<span class="g">+ BASE_RET_MAX = 0.80           # 80% 하락까지 허용 (기존 68%에서 대폭 완화)</span>
<span class="g">+ ui = [f"{ESC}[H", "=" * 95 + f"{ESC}[K", f"UPBIT HYBRID ENGINE BASE016 [ 1~2: BASE | 3:...</span>
<span class="g">+ f"HY_bot BASE016 전체 코드 배포 완료.\n"</span></code></pre>
</div>

## 무엇을 바꿨나

눌림목 지지 반등 실험의 마지막 보존본, 1,051줄. 11개 버전의 짧은 시리즈였지만, 병렬 실험기의 시리즈 중 **현행 전략에 가장 많은 유전자를 남긴 쪽**이 이 BASE다. 지지선 근접 판정과 반등 확인 로직이 이후 VVWAP기로 흘러들어간다.

## 소회

짧게 살고 길게 남은 시리즈. 실험의 수명과 유산의 크기는 비례하지 않는다.

> 마크 더글러스는 시장이 아니라 자신의 규칙과 거래하라고 했다. 봇을 만든다는 건 그 규칙을 물리적으로 만드는 일이다.

Developer: JH JEONG
