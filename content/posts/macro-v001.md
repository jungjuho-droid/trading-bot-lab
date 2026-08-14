---
title: "[개발일지] MACRO.V001 — MACRO — 1시간봉 돌파 스윙의 개막"
description: "MACRO.V001 · MACRO: The 1H Breakout Swing"
date: 2026-07-08T09:45:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "돌파전략", "Trading Bot Lab"]
summary: "MACRO — 1시간봉 돌파 스윙의 개막. 병렬 실험기 48/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V001 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 1번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO001.py — 317줄</em></div>
<pre><code><span class="c"># [ CONFIGURATION ]</span>
<span class="c"># [ 슬롯 1,2 ]</span>
<span class="c"># [ 슬롯 3,4 ]</span>
<span class="c"># [ 공통 필터 ]</span>
<span class="g">(시리즈 첫 보존본 — diff 기준점)</span></code></pre>
</div>

## 무엇을 바꿨나

병렬 실험기의 최대 시리즈(57개), MACRO의 1번이다. 317줄의 컴팩트한 시작 — 이름대로 거시(매크로) 관점의 **1시간봉 돌파 스윙** 엔진이다. 분봉의 소음을 버리고 시간봉의 추세를 타겠다는, 단타와 정반대 방향의 가설.

## 소회

단타의 피로가 낳은 반동이 MACRO였다. 봉 하나가 길어지자 하루가 조용해졌다.

> 짐 로저스는 아무것도 하지 않는 것도 포지션이라고 했다. 진입하지 않게 만드는 코드가 진입 코드보다 늘 길었다.

Developer: JH JEONG
