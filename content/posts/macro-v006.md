---
title: "[개발일지] MACRO.V006 — 업비트 인증을 직접 — JWT 도입"
description: "MACRO.V006 · Native Upbit Auth via JWT"
date: 2026-07-08T13:49:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "업비트 인증을 직접 — JWT 도입. 병렬 실험기 50/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V006 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 3번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO006.py — 319줄</em></div>
<pre><code><span class="r">- import websockets</span>
<span class="r">- import sys</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # [ MACRO006 스윙 코어 파라미터 ]</span>
<span class="c">+ # 1H 돌파 스윙 파라미터</span>
<span class="g">+ import jwt</span>
<span class="g">+ import uuid</span>
<span class="g">+ import hashlib</span>
<span class="g">+ from urllib.parse import urlencode</span></code></pre>
</div>

## 무엇을 바꿨나

`import jwt`, `import uuid` — 업비트 공식 인증(JWT 서명)을 라이브러리 의존 없이 직접 구현했다. 헤더에는 'API 인증 및 통신 인프라 (동기화 100% 강제)'가 붙었다. 빗썸 시절 HMAC을 직접 짜던 그 습관 그대로 — 돈이 지나가는 길목은 직접 놓는다.

## 소회

인증 코드를 직접 짜면 실패 지점을 전부 안다. 세 번째 거래소 규격을 손으로 옮기며 이제 이 작업이 의식(儀式)처럼 느껴졌다.

> 워런 버핏은 썰물이 되면 누가 벌거벗고 수영했는지 드러난다고 했다. 안전장치는 밀물일 때 만들어야 한다 — 이 버전처럼.

Developer: JH JEONG
