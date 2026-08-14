---
title: "[개발일지] VVWAP.V116 — RSI 게이트 조정"
description: "VVWAP.V116 · RSI Gate Tuning"
date: 2026-07-20T22:18:00+09:00
draft: false
series: ["VVWAP기"]
tags: ["개발일지", "VVWAP기", "자동매매", "업비트", "RSI", "VWAP", "Trading Bot Lab"]
summary: "RSI 게이트 조정. VVWAP기 15/27."
---

## 배경

이 글은 VVWAP기 — VV의 기원의 한 페이지, VVWAP.V116 의 기록이다. 앵커드 VWAP 기반으로 재설계한 시기로, 현행 VV 넘버링이 여기서 시작된다. 이 시리즈에 보존된 27개 버전 가운데 16번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>VV116.py — 871줄</em></div>
<pre><code><span class="r">- # [VV115] 터미널 대시보드를 rich 기반으로 교체 (pip install rich 필요)</span>
<span class="r">- from rich.console import Console, Group</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE VV116 (VWAP + Alt B + Momentum Out)</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [VV116 전용 파라미터]</span>
<span class="c">+ # [VV116 패치] 스테이블코인만 평가 대상에서 제외.</span>
<span class="g">+ VERSION = "VV116"</span>
<span class="g">+ STATE_FILE = "UPBIT_ENGINE_VV116_STATE.json"</span>
<span class="g">+ if ticker in STABLE_COINS: continue</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 871줄. 직전 버전 대비 +94/-97줄 — 중간 수정이다. 파일 머리의 당시 메모: "======================================================================". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **RSI 게이트 조정**이다. 당시 주석이 의도를 증언한다 — "[ 코어 파라미터 ] UPBIT HYBRID ENGINE VV116 (VWAP + Alt B + Momentum Out)" / "=============================================================================="

## 소회

이때부터 '기준선 대비 위치'로 생각하는 습관이 생겼다. 지금의 게이트 사고방식의 뿌리다. VV 라는 이름이 어디서 왔냐고 묻는다면 여기다 — VVWAP. 거래량 가중 평균가를 기준선 삼자는 발상이 그대로 이름이 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 니콜라스 다바스는 시장에 있는 시간보다 기록을 들여다본 시간이 자신을 만들었다고 했다. 아카이브를 정리하는 지금이 꼭 그렇다.

Developer: JH JEONG
