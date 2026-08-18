---
title: "[개발일지] VV211 — 원장 캐시 키가 폭발해 메모리 434MB를 먹었다 (Dev Log VV211: A Ledger Cache Key Explosion That Ate 434MB)"
description: "손익표에 한 번도 안 나타난 버그가 봇을 OOM 직전까지 몰고 갔다. A bug that never touched the P&L pushed the bot to the edge of an out-of-memory kill."
date: 2026-08-17T10:05:00+09:00
draft: false
tags: ["개발일지", "자동매매", "업비트", "메모리누수"]
summary: "3일 11시간 가동한 봇의 RSS가 434MB까지 부풀었다. 원인은 전략이 아니라 캐시 키 하나였다."
---

## 조용히 무거워지고 있었다

주말 사이 봇이 부풀어 있었다. 3일 11시간 연속 가동한 시점의 수치다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>2026-08-17 · 서버 메모리 실측</em></div>
<pre><code><span class="r">봇 RSS</span> 434MB <span class="c">전체 911MB 의 46.50%</span>
<span class="r">익명 메모리</span> 403MB
<span class="r">스왑 사용</span> 810MB
<span class="r">가용</span> 84MB <span class="c">OOM 직전</span>
<span class="c">--------------------------------------------------</span>
<span class="g">fd 8개 · 스레드 4개</span> <span class="c">핸들 누수는 아니다</span>
<span class="w">→ 파이썬 객체가 쌓이고 있다</span></code></pre>
</div>

핸들이 새면 파일 디스크립터나 스레드가 같이 늘어난다. 둘 다 정상이었다. 그러면 남는 건 객체다.

## 창 경계가 매번 밀리고 있었다

범인은 원장 조회 캐시였다. `vv_ledger` 는 거래소 체결 내역을 45일치 소급해 읽는데, 긴 기간을 한 번에 안 주기 때문에 6일씩 창을 나눠 페이징한다. 그 창의 시작점을 '지금부터 45일 전'으로 잡은 것이 문제였다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>창 경계를 어디에 고정하느냐</em></div>
<pre><code><span class="r">[ 이전 ]</span> start = now - 45일
<span class="c">5분 뒤 호출하면 경계가 5분 밀린다</span>
<span class="r">캐시 키 매번 신규 · 적중률 0% · 삭제 없음</span>
<span class="c"> </span>
<span class="g">[ VV211 ]</span> start = epoch 6일 배수 격자에 스냅
<span class="c">같은 구간이면 언제 물어봐도 같은 키</span>
<span class="g">키 재사용 9/9</span> <span class="c">(이전 방식 0/8)</span>
<span class="c">--------------------------------------------------</span>
<span class="w">5분 주기 × 창 8개 × 종목 수 → 3.5일에 40만 키</span></code></pre>
</div>

재현해 보니 계산대로였다. 캐시가 하는 일이 없었고, 지워지지도 않았다. 안전망도 하나 붙였다. 캐시가 500개를 넘으면 오래된 창부터 200개를 정리한다. 캔들 캐시와 일봉 캐시가 이미 쓰던 방식 그대로다.

부수 효과가 하나 더 있었다. 적중률이 0이었으니 대조할 때마다 전량 재조회를 했다. 원장 대조 자체가 느렸던 이유다. 캐시가 살아나면서 그것도 같이 풀렸다.

배포 전 무결성 검사와 게이트21은 통과했다. 총자산 3,228,929원이 거래소 값과 일치했고, 그 시점엔 보유 포지션이 없었다.

## 손익표 바깥의 계기판

두 달 넘게 진입 게이트와 청산 파라미터만 들여다봤다. 메모리는 한 번도 안 봤다. 손익표에 안 나타나니까.

그런데 OOM 이 나면 파라미터가 아무리 좋아도 그 순간 봇은 없는 것과 같다. 이 버그는 내 수익을 한 푼도 깎지 않았고, 대신 봇을 죽일 뻔했다. 계기판을 손익 쪽에만 달아뒀다는 걸 434MB 를 보고 알았다.

> 폴 튜더 존스는 트레이딩에서 중요한 건 화려한 공격이 아니라 탄탄한 수비라고 했다. 수비를 진입 게이트 얘기로만 읽고 있었다. 봇이 내일 아침에도 켜져 있는 것, 그것도 수비다.

---

## 약어 풀이

\* 이 글에 나온 영어 약어를 풀어 둔다.

- **RSS** (Resident Set Size): 상주 메모리 크기. 프로세스가 실제로 물리 메모리에 올려두고 쓰는 용량.
- **OOM** (Out Of Memory): 메모리 고갈. 남은 메모리가 없어 운영체제가 프로세스를 강제 종료하는 상태.
