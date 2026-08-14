---
title: "[개발일지] BB.V010 — 텔레그램 리포트 정비"
description: "BB.V010 · Telegram Reporting"
date: 2026-07-15T15:55:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "알림", "Trading Bot Lab"]
summary: "텔레그램 리포트 정비. 병렬 실험기 106/108."
---

## 배경

이 글은 빗썸 분기의 한 페이지, BITHUMB.V010 의 기록이다. 업비트로 넘어간 뒤에도 빗썸 쪽을 유지해보려던 분기 계열이다. 이 시리즈에 보존된 3개 버전 가운데 2번째 기록이다. 원본 파일 시각이 소실된 EC2 복원본이라, 게시일은 버전 순서에 따라 시대 구간 안에 배정했다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MA_bot010(bithumb).py — 384줄</em></div>
<pre><code><span class="r">- [ ALGORITHMIC TRADING ENGINE V8.0 - BITHUMB API 2.0 PRO EDITION ]</span>
<span class="r">- ■ 시스템 핵심 로직 및 픽스 내역</span>
<span class="c">+ # 1. BITHUMB API 2.0 CORE CLASS</span>
<span class="g">+ [ ALGORITHMIC TRADING ENGINE V9.2 - 4H CLOSED CANDLE + FULL REPORTING ]</span>
<span class="g">+ ■ V9.2 최종 업데이트 내역</span>
<span class="g">+ - [복구] 3시간(10800초) 단위 텔레그램 상세 정기 리포트 기능 전면 복구</span>
<span class="g">+ - [유지] 4시간봉(minutes/240) '완성봉(Closed Candle)' 기준 돌파 매수</span>
<span class="g">+ - [유지] 0시 잔고 방어, 자동 시드 동기화, Atomic Write, 에러 Kill-Switch</span>
<span class="g">+ import math</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 384줄. 직전 버전 대비 +188/-275줄 — 대수술이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **텔레그램 리포트 정비**이다. 당시 주석이 의도를 증언한다 — "1. BITHUMB API 2.0 CORE CLASS"

## 소회

두 거래소를 같이 굴리는 건 코드가 아니라 주의력의 문제였다. 결국 업비트에 집중하기로 했다. 장기투자 계좌와 트레이딩 계좌는 분리해야 한다는 처음의 원칙으로 돌아온 셈이다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 워런 버핏은 썰물이 되면 누가 벌거벗고 수영했는지 드러난다고 했다. 안전장치는 밀물일 때 만들어야 한다 — 이 버전처럼.

Developer: JH JEONG
