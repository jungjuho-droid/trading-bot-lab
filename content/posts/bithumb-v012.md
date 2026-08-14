---
title: "[개발일지] BB.V012 — 텔레그램 리포트 정비"
description: "BB.V012 · Telegram Reporting"
date: 2026-07-15T18:57:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "알림", "Trading Bot Lab"]
summary: "텔레그램 리포트 정비. 병렬 실험기 107/108."
---

## 배경

이 글은 빗썸 분기의 한 페이지, BITHUMB.V012 의 기록이다. 업비트로 넘어간 뒤에도 빗썸 쪽을 유지해보려던 분기 계열이다. 이 시리즈에 보존된 3개 버전 가운데 3번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MA_botv012(bit).py — 437줄</em></div>
<pre><code><span class="r">- [ ALGORITHMIC TRADING ENGINE V9.2 - 4H CLOSED CANDLE + FULL REPORTING ]</span>
<span class="r">- ■ V9.2 최종 업데이트 내역</span>
<span class="c">+ # 2. CORE UTILITIES</span>
<span class="c">+ # ==============================================================================</span>
<span class="g">+ [ ALGORITHMIC TRADING ENGINE V9.5 - CORE SPECIFICATION MANUAL ]</span>
<span class="g">+ ■ [알고리즘 운용 명세서 (핵심 요약)]</span>
<span class="g">+ 1. 매매 타점 (4H Breakout)</span>
<span class="g">+ - 4시간 '완성봉(종가)' 기준 최근 N주기 고점 돌파 시 매수.</span>
<span class="g">+ - 단기 과열(RSI 75 초과) 및 장대양봉(전고점 대비 +5% 초과) 추격 매수 금지.</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 437줄. 직전 버전 대비 +110/-57줄 — 중간 수정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **텔레그램 리포트 정비**이다. 당시 주석이 의도를 증언한다 — "2. CORE UTILITIES" / "=============================================================================="

## 소회

두 거래소를 같이 굴리는 건 코드가 아니라 주의력의 문제였다. 결국 업비트에 집중하기로 했다. 장기투자 계좌와 트레이딩 계좌는 분리해야 한다는 처음의 원칙으로 돌아온 셈이다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 마크 미너비니는 손실을 작게 유지하는 것이 공격의 전제라고 했다. 방어 코드가 늘어날수록 진입은 오히려 과감해졌다.

Developer: JH JEONG
