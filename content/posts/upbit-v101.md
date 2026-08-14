---
title: "[개발일지] UP.V101 — 스윙과 방어의 결합"
description: "UP.V101 · Swing & Defense"
date: 2026-06-04T20:02:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "스윙과 방어의 결합. 단일파일 진화기 10/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V101 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-04 20:02. 이 시리즈에 보존된 120개 버전 가운데 10번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v101_bot.py — 1,609줄</em></div>
<pre><code><span class="r">- # 1. 전역 통계 관리자 (업비트 V100 규격)</span>
<span class="r">- self.filename = "upbit_v100_trade_stats.json"</span>
<span class="c">+ # [V101 추가 기능] 넉넉한 사이즈의 커스텀 확인 팝업창</span>
<span class="c">+ # ==========================================</span>
<span class="c">+ # 1. 전역 통계 관리자</span>
<span class="g">+ def custom_askyesno(parent, title, message):</span>
<span class="g">+ dialog = tk.Toplevel(parent)</span>
<span class="g">+ dialog.title(title)</span>
<span class="g">+ dialog.transient(parent)</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1609줄. 직전 버전 대비 +161/-138줄 — 대수술이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **스윙과 방어의 결합**이다. 당시 주석이 의도를 증언한다 — "[V101 추가 기능] 넉넉한 사이즈의 커스텀 확인 팝업창" / "=========================================="

## 소회

파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 알렉산더 엘더는 훌륭한 매매 기록이 훌륭한 트레이더를 만든다고 했다. 버전 파일 하나하나가 나에겐 그 기록이었다.

Developer: JH JEONG
