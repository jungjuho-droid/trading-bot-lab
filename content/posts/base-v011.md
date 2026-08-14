---
title: "[개발일지] BASE.V011 — RSI 게이트 조정"
description: "BASE.V011 · RSI Gate Tuning"
date: 2026-07-07T16:34:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "RSI", "Trading Bot Lab"]
summary: "RSI 게이트 조정. 병렬 실험기 43/108."
---

## 배경

이 글은 BASE 실험기의 한 페이지, BASE.V011 의 기록이다. 바닥권 지지선 진입(Bottom Area Support Entry)이라는 단일 아이디어를 파고든 계열이다. 이 시리즈에 보존된 11개 버전 가운데 7번째 기록이다. 원본 파일 시각이 소실된 EC2 복원본이라, 게시일은 버전 순서에 따라 시대 구간 안에 배정했다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>BASE011.py — 1,044줄</em></div>
<pre><code><span class="r">- # [ HYBRID TRADING ENGINE BASE006 ]</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ HYBRID TRADING ENGINE BASE011 ]</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # VER: v0.0.11 (BASE Frequency Maximize &amp; F-KNIFE 5min Sniper Mode)</span>
<span class="c">+ # DESC: BASE frequency increased, FK strict sniper entry with 5m TimeStop.</span>
<span class="g">+ BASE_PUMP_MIN = 0.012         # 1.2% 상승 포착 (기존 1.5%)</span>
<span class="g">+ BASE_VOL_SURGE = 2.5          # 2.5배 거래량 폭발 (기존 3.0)</span>
<span class="g">+ BASE_RET_MIN = 0.50</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1044줄. 직전 버전 대비 +55/-55줄 — 중간 수정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **RSI 게이트 조정**이다. 당시 주석이 의도를 증언한다 — "[ HYBRID TRADING ENGINE BASE011 ]" / "=============================================================================="

## 소회

이 실험 자체는 접었지만, '바닥 근처에서만 산다'는 유전자는 살아남아 현행 저점근접 게이트(24시간 저점 대비 +3% 이내)가 됐다. 지지선은 차트에서는 선명한데 코드로 쓰면 흐릿해진다. 정의를 숫자로 못 내리면 전략이 아니라는 걸 배웠다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 제시 리버모어는 큰돈은 매매가 아니라 기다림이 벌어준다고 했다. 이 버전의 코드 몇 줄도 결국 기다림을 만드는 장치였다.

Developer: JH JEONG
