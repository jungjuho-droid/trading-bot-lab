---
title: "[개발일지] UP.V115 — 분할 매수/매도 체계"
description: "UP.V115 · Quantum Scale-In/Out"
date: 2026-06-06T01:14:00+09:00
draft: false
series: ["단일파일 진화기"]
tags: ["개발일지", "단일파일진화기", "자동매매", "업비트", "Trading Bot Lab"]
summary: "분할 매수/매도 체계. 단일파일 진화기 24/120."
---

## 배경

이 글은 단일파일 진화기의 한 페이지, UPBIT.V115 의 기록이다. 한 파일 1,500줄짜리 모놀리스가 버전 번호를 바꿔가며 증식하던, 가장 왕성하고 가장 어지럽던 시기다. 파일이 기억하는 시각은 2026-06-06 01:14. 이 시리즈에 보존된 120개 버전 가운데 24번째 기록이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>upbit_v115_bot.py — 1,334줄</em></div>
<pre><code><span class="r">- # [V101 추가 기능] 넉넉한 사이즈의 커스텀 확인 팝업창</span>
<span class="r">- def on_yes():</span>
<span class="c">+ # [공통 유틸] 커스텀 확인 팝업창</span>
<span class="c">+ # [API 보호] 글로벌 호출 속도 제한기</span>
<span class="c">+ # 1. 통계 관리자 (V115 규격 - 영구 보존)</span>
<span class="c">+ # 2. 업비트 API V1 엔진</span>
<span class="g">+ def on_yes(): result.set(True); dialog.destroy()</span>
<span class="g">+ def on_no(): result.set(False); dialog.destroy()</span>
<span class="g">+ if elapsed &lt; self.interval: time.sleep(self.interval - elapsed)</span></code></pre>
</div>

## 무엇을 바꿨나

코드는 1334줄. 직전 버전 대비 +475/-555줄 — 사실상의 재작성이다. 파일 머리의 당시 메모: "-*- coding: utf-8 -*-". 커밋이 없던 시절이라 의도는 diff 로만 남았다. 이번 보존본의 무게중심은 **분할 매수/매도 체계**이다. 당시 주석이 의도를 증언한다 — "[공통 유틸] 커스텀 확인 팝업창" / "[API 보호] 글로벌 호출 속도 제한기"

## 소회

버전 번호가 백 단위로 뛰던 건 자신감이 아니라 시행착오의 개수였다. 이때 매매 데이터를 체계적으로 안 남긴 게 지금도 아쉽다. 기록이 있었다면 절반의 실험은 안 해도 됐다. 파일 하나에 다 넣는 방식은 빨랐다. 대신 어디를 고치면 어디가 부서지는지 아무도 몰랐다 — 나조차도. 다음 버전은 언제나 직전 버전이 남긴 질문에 대한 답이었고, 이 버전도 예외가 아니다.

> 알렉산더 엘더는 훌륭한 매매 기록이 훌륭한 트레이더를 만든다고 했다. 버전 파일 하나하나가 나에겐 그 기록이었다.

Developer: JH JEONG
