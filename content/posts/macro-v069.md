---
title: "[개발일지] MACRO.V069 — MACRO의 종장"
description: "MACRO.V069 · MACRO's Finale"
date: 2026-07-15T09:51:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "돌파전략", "눌림목전략", "Trading Bot Lab"]
summary: "MACRO의 종장. 병렬 실험기 104/108."
---

## 배경

이 글은 MACRO 실험기의 한 페이지, MACRO.V069 의 기록이다. 거시 신호를 진입 필터로 쓰려던 60여 개 버전의 실험 계열이다. 이 시리즈에 보존된 57개 버전 가운데 57번째 기록이다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>MACRO069.py — 959줄</em></div>
<pre><code><span class="r">- # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO068 (Time-out TR Edition)</span>
<span class="r">- # ==============================================================================</span>
<span class="c">+ # [ 코어 파라미터 ] UPBIT HYBRID ENGINE MACRO069 (Deep Trench Edition)</span>
<span class="c">+ # ==============================================================================</span>
<span class="c">+ # TR 타임스탑(Time-out) 파라미터 (초 단위)</span>
<span class="c">+ # [V69 패치] 섀도우 진입 대기 완전히 제거 (0.0% 즉시 진입)</span>
<span class="g">+ VERSION = "MACRO069"</span>
<span class="g">+ SHADOW_DROP_TARGET = 0.000</span>
<span class="g">+ SHADOW_CANCEL_BOUNCE = 0.002</span></code></pre>
</div>

## 무엇을 바꿨나

57개 버전을 이어온 최대 병렬 시리즈의 마지막, 959줄. 1시간봉 돌파 가설은 여기서 실험을 마친다. 돌파 매매의 유산 — 완성봉 기준 판정, 시간봉 필터 — 은 살아남아 다음 시대로 넘어가고, '돌파 그 자체'는 훗날 vv168에서 눌림목에게 자리를 내준다.

## 소회

가장 오래 실험한 가설이 가장 담담하게 은퇴했다. 돌파는 틀리지 않았다. 다만 내 성격과 맞지 않았을 뿐.

> 짐 로저스는 아무것도 하지 않는 것도 포지션이라고 했다. 진입하지 않게 만드는 코드가 진입 코드보다 늘 길었다.

Developer: JH JEONG
