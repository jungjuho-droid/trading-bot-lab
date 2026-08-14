---
title: "[개발일지] BASE.V001 — BASE — 눌림목 지지 반등, 전략의 이름이 되다"
description: "BASE.V001 · BASE: Bottom-Area Support Entry"
date: 2026-07-06T22:20:00+09:00
draft: false
series: ["병렬 실험기"]
tags: ["개발일지", "병렬실험기", "자동매매", "업비트", "슬롯구조", "눌림목전략", "Trading Bot Lab"]
summary: "BASE — 눌림목 지지 반등, 전략의 이름이 되다. 병렬 실험기 37/108."
---

## 배경

이 글은 BASE 실험기의 한 페이지, BASE.V001 의 기록이다. 바닥권 지지선 진입(Bottom Area Support Entry)이라는 단일 아이디어를 파고든 계열이다. 이 시리즈에 보존된 11개 버전 가운데 1번째 기록이다. 원본 파일 시각이 소실된 EC2 복원본이라, 게시일은 버전 순서에 따라 시대 구간 안에 배정했다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>BASE001.py — 1,008줄</em></div>
<pre><code><span class="c"># [ HYBRID TRADING ENGINE BASE_001 ]</span>
<span class="c"># [ 시스템 통합 설정 ]</span>
<span class="c"># [ 1~2번 슬롯: BASE (눌림목 지지 반등) 파라미터 ]</span>
<span class="c"># [ 1, 2 ]</span>
<span class="g">(시리즈 첫 보존본 — diff 기준점)</span></code></pre>
</div>

## 무엇을 바꿨나

시리즈 이름부터 전략 선언이다 — BASE, **Bottom Area Support Entry**. 헤더에 '1~2번 슬롯: BASE (눌림목 지지 반등) 파라미터'라고 적혀 있다. v1.9(빗썸)에서 태어나 흩어져 있던 눌림목 아이디어가, 여기서 처음으로 **시리즈 전체의 정체성**이 됐다. 현행 봇의 '과매도 눌림목 반등' 전략의 직계 실험실이다.

## 소회

전략에 이름을 붙이는 순간 책임이 생긴다. BASE라는 넉 자가 지금 봇의 전략 한 줄 요약과 같다는 게, 이 실험의 승리를 말해준다.

> 마크 미너비니는 손실을 작게 유지하는 것이 공격의 전제라고 했다. 방어 코드가 늘어날수록 진입은 오히려 과감해졌다.

Developer: JH JEONG
