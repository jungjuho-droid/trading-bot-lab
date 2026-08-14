---
title: "[개발일지] BASE.V004 — 슬롯 운용 조정"
description: "BASE.V004 · Slot Management"
date: 2026-07-07T09:27:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "슬롯구조", "Trading Bot Lab"]
summary: "슬롯 운용 조정. 병렬 실험기 40/108."
---

## 배경

이 글은 BASE 실험기의 한 페이지, BASE.V004 의 기록이다. 바닥권 지지선 진입(Bottom Area Support Entry)이라는 단일 아이디어를 파고든 계열이다. 이 시리즈에 보존된 11개 버전 가운데 4번째 기록이다. 원본 파일 시각이 소실된 EC2 복원본이라, 게시일은 버전 순서에 따라 시대 구간 안에 배정했다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>BASE004.py — 651줄</em></div>
<pre><code><span class="r">- # [ HYBRID TRADING ENGINE BASE003 ]</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ HYBRID TRADING ENGINE BASE004 ]</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # VER: v0.0.4 (Telegram Report Formatting &amp; API Rate Limit Fix)</span>
<span class="g">+ pnl_tracker = {'total_net': 0, 'daily': {}, 'weekly': {}, 'monthly': {}, 'hourly': {'ne...</span>
<span class="g">+ pnl_tracker['hourly'] = loaded_pnl.get('hourly', {'net': 0, 'win': 0, 'loss': 0, 'vol':...</span>
<span class="g">+ def record_trade_history(realized_profit, total_investment=0):</span>
<span class="g">+ pnl_tracker['hourly']['vol'] = pnl_tracker['hourly'].get('vol', 0) + total_investment</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 651줄. 직전 버전 대비 +34/-416줄 — 대수술이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **슬롯 운용 조정**이다. 당시 주석이 의도를 증언한다 — "[ HYBRID TRADING ENGINE BASE004 ]" / "=============================================================================="

## 소회

지지선은 차트에서는 선명한데 코드로 쓰면 흐릿해진다. 정의를 숫자로 못 내리면 전략이 아니라는 걸 배웠다. 이 실험 자체는 접었지만, '바닥 근처에서만 산다'는 유전자는 살아남아 현행 저점근접 게이트(24시간 저점 대비 +3% 이내)가 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 윌리엄 오닐은 손절은 보험료라고 했다. 보험료 계산식을 고치는 날이 제일 많았다.

Developer: JH JEONG
