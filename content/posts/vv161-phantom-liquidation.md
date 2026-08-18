---
title: "[개발일지] VV161 — 실제로는 +4,706원이었는데 봇은 -30.85%를 보고 전량 청산했다 (Dev Log VV161: The Bot Liquidated Everything Over a Loss That Never Happened)"
description: "같은 거래소의 두 조회 API가 응답 필드를 다르게 준다는 걸 몰랐다. Two endpoints on the same exchange returned different fields, and the bot read a total loss that never existed."
date: 2026-07-29T21:48:00+09:00
draft: false
tags: ["개발일지", "자동매매", "업비트", "장애복기"]
summary: "표시 손실 -1,072,270원은 전액 허수였다. 실제 손익은 +4,706원이었고 잔고는 멀쩡했다."
---

## 21시 10분, 멀쩡한 포지션 세 개가 날아갔다

포트폴리오 손절이 발동해 보유 종목 전부가 시장가로 정리됐다. 화면에 찍힌 손실은 -1,072,270원, -30.85%. 그런데 실계좌 잔고는 멀쩡했다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>2026-07-29 21:10 · 표시값 vs 실제</em></div>
<pre><code><span class="r">봇이 본 것</span> -1,072,270원 <span class="c">(-30.85%)</span>
<span class="c"> </span>
<span class="g">실제 손익</span> PIEVERSE <span class="g">+764원</span>
<span class="g"> </span> PROS <span class="g">+5,399원</span>
<span class="g"> </span> TRX <span class="r">-1,113원</span>
<span class="c">--------------------------------------------------</span>
<span class="g">합계 +4,706원</span> <span class="c">· 금전 손실 없음</span>
<span class="r">전량청산은 되돌릴 수 없다</span></code></pre>
</div>

## 엔드포인트 두 개가 다른 말을 했다

원인은 응답 스키마였다. 같은 거래소인데 주문 조회 API 두 개가 서로 다른 필드를 준다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>체결대금을 어디서 읽는가</em></div>
<pre><code><span class="w">GET /v1/orders/closed</span> <span class="c">(다건)</span> <span class="g">executed_funds 있음</span>
<span class="w">GET /v1/order</span> <span class="c">(단건)</span> <span class="r">없음 · trades[] 배열만</span>
<span class="c">--------------------------------------------------</span>
<span class="r">직전 버전은 단건 조회에서 executed_funds 를 읽었다</span>
<span class="r">→ 항상 0 수신 → 실수령액 0원</span>
<span class="r">→ 투자금 전액 손실로 계산 → 포트폴리오 -32.84%</span>
<span class="r">→ 전량청산</span></code></pre>
</div>

`_extract_executed_funds()` 를 새로 만들었다. `executed_funds` 가 있으면 그걸 쓰고, 없으면 `trades[]` 의 체결금액을 합산한다. 두 엔드포인트 모두 345,927원을 정확히 뽑는 것을 확인했다.

여기서 멈추지 않았다. 체결수량이 0보다 큰데 체결대금이 0이면 미확정으로 보고 다시 조회한다. 타임아웃까지 불명이면 0이 아니라 None 을 돌려준다. **모른다는 것과 0원은 다르다.** 이 구분이 없어서 사고가 났다.

그리고 상한을 하나 걸었다. 손익률이 ±20%를 벗어나면 데이터 오류로 간주하고 전량청산을 실행하지 않는다.

## 의심스러우면 실행하지 않는다

전량청산은 되돌릴 수 없다. 그런데 그 방아쇠를 당기는 판단이 검증 안 된 숫자 하나에 걸려 있었다.

방어 장치를 만들 때 보통 "언제 발동할까"만 생각한다. 이번에 배운 건 반대쪽이다. **언제 발동하지 않을까**도 같이 정해둬야 한다. 되돌릴 수 없는 행동일수록 그렇다.

> 브루스 코브너는 포지션을 잡기 전에 무엇이 잘못될 수 있는지부터 그려본다고 했다. 나는 청산에도 같은 걸 해야 했다. 사는 쪽만 최악을 상상하고 있었다.

---

## 약어 풀이

\* 이 글에 나온 영어 약어를 풀어 둔다.

- **API** (Application Programming Interface): 응용 프로그램 인터페이스. 거래소 서버에 시세·주문·체결 내역을 요청하고 받아오는 규격.
