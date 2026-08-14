---
title: "615줄짜리 시조, 그리고 2중 실행 방지"
description: "BT.V1.04 · 615 Lines, and a Lock Against Running Twice"
date: 2026-05-26T21:11:00+09:00
draft: false
series: ["빗썸 기원기"]
tags: ["개발일지", "빗썸기원기", "빗썸", "tkinter", "HMAC", "API인증", "pybithumb", "자동매매"]
summary: "전체 계보의 시조. 615줄 안에 통신 엔진과 GUI가 통째로 들어 있던 버전."
---

## 배경

보존된 코드 중 가장 오래된 파일이다. 615줄, 2026년 5월 26일 밤 9시 11분. 461개 버전의 시조다. 파일 머리에 적힌 메모는 딱 한 줄인데, 전날 요구사항 메모의 마지막 문장과 정확히 같다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>bithumb_bot_v1_4.py — 615 lines</em></div>
<pre><code><span class="c">================= [ 2중 실행 방지 로직 ] =================</span>
import tkinter as tk
from tkinter import ttk, messagebox
import pybithumb
<span class="c"># --- 시세·차트는 라이브러리로 ---</span>
mkt_price = pybithumb.get_current_price(ticker)
df        = pybithumb.get_ohlcv(ticker)
<span class="c"># --- 인증이 필요한 구간만 직접 구현 ---</span>
class <span class="w">CustomBithumbAPI</span>:
    def _req(...)        <span class="c"># HMAC-SHA512 서명</span>
    def get_balance(...)
    def buy_market(...)
    def sell_market(...)</code></pre>
</div>

## 무엇을 바꿨나

한 파일에 전부 들어 있다. 인증 통신 엔진, tkinter GUI, 매매 로직. 클래스 하나가 API를 감싸고 다른 하나가 창을 그린다.

통신은 두 갈래로 나눠져 있다. 시세와 분봉처럼 인증이 필요 없는 공개 데이터는 `pybithumb` 라이브러리를 그대로 쓴다. 반면 **잔고 조회와 주문처럼 돈이 움직이는 구간은 직접 짰다.** HMAC-SHA512로 서명을 만들어 헤더에 싣는 클래스를 따로 뒀다. 남의 코드가 어디서 실패하는지 모르는 채로 실주문을 내보내는 게 더 무서웠기 때문이다.

추정: 이 시점에 손절은 있었지만 재진입 통제도, 일일 한도도, 시장 상황 판단도 없었다. **개별 거래의 리스크는 있고 계좌 전체의 리스크는 없는 구조.** 이후 두 달은 그 빈칸을 채우는 과정이었다.

## 소회

615줄은 지금 보면 귀엽다. 현행 봇은 모듈이 여섯 개고 git으로 관리된다. 그런데 뼈대는 안 바뀌었다. 읽고, 판단하고, 주문한다. 늘어난 건 "안 사는 이유"의 개수뿐이다.

편한 건 라이브러리에 맡기고 위험한 건 직접 짠다 — 이 감각도 그대로 남았다.

> 폴 튜더 존스는 방어가 공격보다 중요하다고 했다. 이 버전의 방어는 2중 실행 방지 하나뿐이었지만, 그걸 파일 맨 위에 적어뒀다는 게 방향은 맞았다는 증거다.
