---
title: "[개발일지] UP.V412 — 텔레그램 리포트 정비"
description: "UP.V412 · Telegram Reporting"
date: 2026-06-12T20:42:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "알림", "Trading Bot Lab"]
summary: "텔레그램 리포트 정비. 단일파일 진화기 70/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V412 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-12 20:42. 이 시리즈에 보존된 120개 버전 가운데 70번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v412_bot.py — 1,926줄</em></div>
<pre><code><span class="r">- self.filename = "upbit_v411_trade_stats.json"</span>
<span class="r">- for fb in ["upbit_v410_trade_stats.json", "upbit_v409_trade_stats.json", "upbit_v303_tr...</span>
<span class="c">+ # 2. 업비트 API V1 엔진</span>
<span class="c">+ # 4. 메인 윈도우 (UPBIT V412 Final Master Edition)</span>
<span class="c">+ # API는 오직 수동 연결만 하도록 자동 연결 제외. (텔레그램은 유지)</span>
<span class="c">+ # [V412 픽스] API 연결 시 실시간으로 잔고를 찔러 테스트하고,</span>
<span class="g">+ self.filename = "upbit_v412_trade_stats.json"</span>
<span class="g">+ for fb in ["upbit_v411_trade_stats.json", "upbit_v410_trade_stats.json", "upbit_v409_tr...</span>
<span class="g">+ summary_msg = f"======== [ SLOT {self.slot_id} ({ui_tkr}) V412 매매 계획 ] ========\n\n"</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1926줄. 직전 버전 대비 +61/-63줄 — 중간 수정이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **텔레그램 리포트 정비**이다. 당시 주석이 의도를 증언한다 — "2. 업비트 API V1 엔진" / "4. 메인 윈도우 (UPBIT V412 Final Master Edition)"

## 소회

이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 짐 로저스는 아무것도 하지 않는 것도 포지션이라고 했다. 진입하지 않게 만드는 코드가 진입 코드보다 늘 길었다.

Developer: JH JEONG
