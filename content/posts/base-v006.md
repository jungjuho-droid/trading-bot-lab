---
title: "[개발일지] BASE.V006 — RSI 게이트 조정"
description: "BASE.V006 · RSI Gate Tuning"
date: 2026-07-07T13:31:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "RSI", "Trading Bot Lab"]
summary: "RSI 게이트 조정. 병렬 실험기 42/108."
---

## 배경

이 글은 BASE 실험기의 한 페이지, BASE.V006 의 기록이다. 바닥권 지지선 진입(Bottom Area Support Entry)이라는 단일 아이디어를 파고든 계열이다. 이 시리즈에 보존된 11개 버전 가운데 6번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>BASE006.py — 1,044줄</em></div>
<pre><code><span class="r">- # [ HYBRID TRADING ENGINE BASE005 ]</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ HYBRID TRADING ENGINE BASE006 ]</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # VER: v0.0.6 (Frequency Optimization &amp; Final Telegram Reporting Format)</span>
<span class="c">+ # 수학적 역산을 통한 체결 빈도 타겟 최적화 (일 10회 포착 타겟)</span>
<span class="g">+ BASE_PUMP_MIN = 0.016</span>
<span class="g">+ BASE_VOL_SURGE = 3.2</span>
<span class="g">+ BASE_RET_MIN = 0.45</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1044줄. 직전 버전 대비 +55/-57줄 — 중간 수정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **RSI 게이트 조정**이다. 당시 주석이 의도를 증언한다 — "[ HYBRID TRADING ENGINE BASE006 ]" / "=============================================================================="

## 소회

지지선은 차트에서는 선명한데 코드로 쓰면 흐릿해진다. 정의를 숫자로 못 내리면 전략이 아니라는 걸 배웠다. 이 실험 자체는 접었지만, '바닥 근처에서만 산다'는 유전자는 살아남아 현행 저점근접 게이트(24시간 저점 대비 +3% 이내)가 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 브루스 코브너는 자신이 틀릴 수 있는 지점을 미리 정해두는 것이 포지션의 전부라고 했다. 파라미터 파일이 곧 그 지점들의 목록이다.

Developer: JH JEONG
