---
title: "[개발일지] VVWAP.CPP — C++ 포팅 시도, 그리고 회귀"
description: "VVWAP.CPP · The C++ Port That Turned Back"
date: 2026-07-24T20:00:00+09:00
draft: false
series: ["VVWAP기"]
tags: ["개발일지", "VVWAP기", "C++", "포팅", "websocketpp", "자동매매", "업비트", "Trading Bot Lab"]
summary: "파이썬 VVWAP을 C++로 옮기려던 흔적. 완성 전에 멈추고 파이썬으로 돌아왔다. VVWAP기 27/27."
---

## 배경

VVWAP기 27/27 — 이 보존본에는 파이썬 파일이 없다. websocketpp와 jwt-cpp 기반의 **C++ 프로젝트 골격**이다. 파이썬 VVWAP 엔진을 C++로 통째로 옮기려던 시도의 흔적으로, 완성 전에 중단됐다. 게시일은 버전 순서 기준 추정 배정이다 (원본 시각 소실).

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>vvwap_cpp — 미완의 포팅</em></div>
<pre><code><span class="c"># 남은 것</span>
<span class="g">websocketpp/   — C++ 웹소켓 스택</span>
<span class="g">jwt-cpp/       — 업비트 JWT 인증</span>
<span class="y">엔진 본체      — 미완성</span>
<span class="r">결론: 파이썬 VVWAP 으로 회귀</span></code></pre>
</div>

## 무엇을 하려 했나

동기는 짐작하기 어렵지 않다 — 속도, 그리고 상주 프로세스의 가벼움. 파이썬 봇을 몇 주씩 돌리며 겪은 메모리와 지연이 C++이라는 선택지를 띄웠을 것이다. websocketpp로 시세 수신, jwt-cpp로 인증까지는 골격을 세웠지만, 매매 로직 본체를 옮기기 전에 손이 멈췄다.

추정: 중단의 이유는 성능이 아니라 **개발 속도**였을 것이다. 파이썬에서 하루에 버전 몇 개씩 갈아끼우던 실험 리듬을 C++에서는 유지할 수 없다. 봇의 경쟁력이 실행 속도가 아니라 개선 속도에 있다는 걸 확인한 실험이었던 셈이다.

## 소회

가지 않은 길도 기록할 가치가 있다. 이 폴더가 남아 있어서, "C++로 갔으면 어땠을까"라는 질문에 나는 이미 답을 갖고 있다 — 가봤고, 돌아왔다.

> 케네스 그리핀의 세계에서는 나노초가 무기지만, 개인 트레이더의 무기는 반복 속도다. 내 전장에 맞는 무기를 고르는 것 — 이 미완의 폴더가 가르쳐준 것이다.

Developer: JH JEONG
