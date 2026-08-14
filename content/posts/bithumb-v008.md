---
title: "[개발일지] BB.V008 — 빗썸 분기 — 4시간봉 완성봉 돌파"
description: "BB.V008 · The Bithumb Fork: 4H Closed-Candle Breakout"
date: 2026-07-15T12:53:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "돌파전략", "Trading Bot Lab"]
summary: "빗썸 분기 — 4시간봉 완성봉 돌파. 병렬 실험기 105/108."
---

## 배경

이 글은 빗썸 분기의 한 페이지, BITHUMB.V008 의 기록이다. 업비트로 넘어간 뒤에도 빗썸 쪽을 유지해보려던 분기 계열이다. 이 시리즈에 보존된 3개 버전 가운데 1번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MA_bot008(bithumb).py — 471줄</em></div>
<pre><code><span class="c">$ diff v_prev v_cur</span>
<span class="g">(변경 없음 — 세이브 포인트)</span></code></pre>
</div>

## 무엇을 바꿨나

병렬 실험기 시절, 잠시 빗썸으로 되돌아간 분기 실험이다. 헤더 명세가 또렷하다 — **4시간봉(minutes/240) '완성봉(Closed Candle)' 기준 돌파 매수**, 0시 잔고 방어, 자동 시드 동기화, Atomic Write, 에러 Kill-Switch. 진행 중인 봉의 훼이크에 속지 않고 닫힌 봉만 믿는다는 원칙 — 현행 봇의 'BTC 4시간봉 레짐 판정'과 정확히 같은 시간 축이 여기서 실험됐다.

## 소회

완성봉만 믿는다는 건 결론이 난 것만 믿는다는 뜻이다. 4시간봉이라는 시간 축이 결국 현행 레짐 차단의 축이 됐다.

> 레이 달리오는 고통 더하기 반성이 진보라고 했다. 이 버전 번호가 곧 반성의 횟수다.

Developer: JH JEONG
