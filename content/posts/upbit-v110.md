---
title: "[개발일지] UP.V110 — 1,226줄로 재작성 — 분할 매수/매도의 시작"
description: "UP.V110 · Rewritten at 1,226 Lines: Scale-In/Out"
date: 2026-06-05T22:10:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "1,226줄로 재작성 — 분할 매수/매도의 시작. 단일파일 진화기 19/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V110 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-05 22:10. 이 시리즈에 보존된 120개 버전 가운데 19번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v110_bot.py — 1,226줄</em></div>
<pre><code><span class="r">- # 1. 전역 통계 관리자 (V109 규격)</span>
<span class="r">- self.filename = "upbit_v109_trade_stats.json"</span>
<span class="c">+ # 1. 전역 통계 관리자 (V110 규격)</span>
<span class="c">+ # 3. 개별 코인 슬롯 (UPBIT V110 Scale-In/Out 커널 엔진)</span>
<span class="c">+ # 분할 진입 및 청산 제어 상태 변수 (V110 장착)</span>
<span class="g">+ self.filename = "upbit_v110_trade_stats.json"</span>
<span class="g">+ fallback_files = ["upbit_v109_trade_stats.json", "upbit_v108_trade_stats.json", "upbit_...</span>
<span class="g">+ try: err_msg = res.json()</span>
<span class="g">+ except: err_msg = res.text</span></code></pre>
</div>

## 무엇을 바꿨나

1,773줄에서 1,226줄로 — 이 시대의 첫 대규모 재작성이다. 이름도 'HTS Scale-In/Out Premium'으로 바뀌었다. 한 번에 다 사고 한 번에 다 파는 구조를 버리고, **나눠 사고 나눠 파는 분할 체계**를 중심에 놓았다. 진입도 청산도 계단이 됐다.

## 소회

분할은 겸손의 기술이다. 내 판단이 틀릴 확률을 구조에 반영하는 것 — 여기서부터 봇이 어른이 되기 시작했다.

> 니콜라스 다바스는 시장에 있는 시간보다 기록을 들여다본 시간이 자신을 만들었다고 했다. 아카이브를 정리하는 지금이 꼭 그렇다.

Developer: JH JEONG
