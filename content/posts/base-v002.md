---
title: "[개발일지] BASE.V002 — 청산 로직 손질"
description: "BASE.V002 · Exit Logic Pass"
date: 2026-07-07T09:22:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "청산 로직 손질. 병렬 실험기 38/108."
---

## 배경

이 글은 BASE 실험기의 한 페이지, BASE.V002 의 기록이다. 바닥권 지지선 진입(Bottom Area Support Entry)이라는 단일 아이디어를 파고든 계열이다. 이 시리즈에 보존된 11개 버전 가운데 2번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>BASE002.py — 1,031줄</em></div>
<pre><code><span class="r">- # [ HYBRID TRADING ENGINE BASE_001 ]</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ HYBRID TRADING ENGINE BASE_002 ]</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # VER: v0.0.2 (Watchlist Target Expose &amp; Transparent Logging UI)</span>
<span class="c">+ #       * NEW: Real-time Candidate Coin Tracking Panel &amp; Drop Reason Logs.</span>
<span class="g">+ 'support_min_price': trade_price,</span>
<span class="g">+ 'ret_ratio': 0.0 # UI 표시용 되돌림 비율</span>
<span class="g">+ sys_log(f"[WATCHLIST_ADD] {coin} ➡️ +{trend_60s*100:.1f}% 펌핑 포착. 추격 금지 및 눌림목 대기")</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1031줄. 직전 버전 대비 +42/-19줄 — 중간 수정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **청산 로직 손질**이다. 당시 주석이 의도를 증언한다 — "[ HYBRID TRADING ENGINE BASE_002 ]" / "=============================================================================="

## 소회

지지선은 차트에서는 선명한데 코드로 쓰면 흐릿해진다. 정의를 숫자로 못 내리면 전략이 아니라는 걸 배웠다. 이 실험 자체는 접었지만, '바닥 근처에서만 산다'는 유전자는 살아남아 현행 저점근접 게이트(24시간 저점 대비 +3% 이내)가 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 리처드 데니스는 규칙은 가르칠 수 있어도 확신은 가르칠 수 없다고 했다. 확신은 이렇게 버전을 쌓으며 스스로 만든다.

Developer: JH JEONG
