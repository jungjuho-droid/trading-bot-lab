---
title: "[개발일지] BT.V1.0F — PRO의 원형 — 168줄의 코어"
description: "BT.V1.0F · The PRO Core, 168 Lines"
date: 2026-05-29T15:03:00+09:00
draft: false
series: ["빗썸 기원기"]
tags: ["개발일지", "빗썸기원기", "빗썸", "자동매매", "전략", "슬롯구조", "수동제어", "Trading Bot Lab"]
summary: "PRO의 원형 — 168줄의 코어. 빗썸 기원기 43/95."
---

## 배경

5월 29일 15:03 저장, 168줄. 굵직한 변경이 담긴 버전이다 (+85 / -151 줄). 이 시리즈에 보존된 95개 버전 가운데 43번째 기록이다. 장기투자용 빗썸 계좌를 지키자고 시작한 봇이 점점 판을 키워가던 무렵이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>bithumb_bot_v1_f.py — 168줄</em></div>
<pre><code><span class="w">BITHUMB SMART TRADING TERMINAL PRO</span>
<span class="r">- except Exception as e:</span>
<span class="r">- return {"status": "9999", "message": str(e)}</span>
<span class="c">+ # 1. Symbol &amp; Avg Price</span>
<span class="c">+ # 2. Params</span>
<span class="c">+ # 3. Control</span>
<span class="c">+ # 4. Manual (가로 배치)</span>
<span class="g">+ except Exception as e: return {"status": "9999", "message": str(e)}</span>
<span class="g">+ self.bg = "#1e293b"</span></code></pre>
</div>

## 무엇을 바꿨나

'TERMINAL PRO'라는 이름이 처음 붙은 168줄짜리 코어다. 통신 엔진의 예외 처리를 `{"status": "9999", "message": str(e)}` 한 줄로 표준화하고, 시드 30만 원·대기 -9%·반등 +0.5%·익절 7%·손절 -4.5%의 기본 파라미터 세트를 확정했다. 이후 PRO 계열 전 버전이 이 틀을 상속한다.

## 소회

이름에 PRO를 붙인 날, 스스로에게 건 주문 같은 것이었다. 장난감이 아니라 도구를 만들고 있다는. 돌아보면 이런 버전들이 쌓여서 규율이 됐다. 규율은 언제나 사후에 이름이 붙는다.

> 마크 미너비니는 손실을 작게 유지하는 것이 공격의 전제라고 했다. 방어 코드가 늘어날수록 진입은 오히려 과감해졌다.

Developer: JH JEONG
