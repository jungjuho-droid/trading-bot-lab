---
title: "최신 API를 버리고 구버전으로 되돌아갔다"
description: "BT.V1.05 · Retreating From the Newer API"
date: 2026-05-26T21:45:00+09:00
draft: false
series: ["빗썸 기원기"]
tags: ["개발일지", "빗썸기원기", "빗썸", "API인증", "HMAC", "urlencode", "디버깅", "자동매매"]
summary: "V2 통신 엔진을 34분 만에 갈아엎었다. 최신이 항상 정답은 아니다."
---

## 배경

직전 버전으로부터 34분. 629줄, +40/-26줄. 시간은 짧지만 바꾼 건 봇의 심장이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>bithumb_bot_v1_5.py — 인증 엔진 교체</em></div>
<pre><code><span class="r">- class CustomBithumbAPI:          # V2 규격</span>
<span class="r">-     data  = {"endpoint":…, "nonce":…}</span>
<span class="r">-     query = quote(json.dumps(data))</span>
<span class="r">-     "Api-Sign": b64encode(sig)          <span class="c"># bytes!</span></span>
<span class="g">+ class CustomBithumbAPI_V1:        # API 1.0 규격</span>
<span class="g">+     str_data = urllib.parse.urlencode(data)</span>
<span class="g">+     query    = endpoint + chr(0) + str_data + chr(0) + nonce</span>
<span class="g">+     "Content-Type": "application/x-www-form-urlencoded"</span>
<span class="g">+     "Api-Sign": b64encode(sig).decode('utf-8')</span>
<span class="c">--------------------------------------------------</span>
<span class="r">⚠️ 로그인 실패: {'status': '5300'}</span>
<span class="g">🚀 V1.0 엔진 로그인 성공!</span></code></pre>
</div>

## 무엇을 바꿨나

통신 엔진을 통째로 교체했다. V2 대응 클래스를 지우고 API 1.0 전용 클래스를 새로 썼다. **최신 규격을 버리고 구버전으로 후퇴한 것이다.**

달라진 건 서명 방식이다. 기존엔 페이로드를 JSON으로 직렬화해 해시했는데, 새 엔진은 폼 인코딩 문자열을 만들어 해시한다. 그리고 서명 결과에 `.decode('utf-8')`을 붙였다 — 이전엔 base64 결과가 bytes 객체 그대로 헤더에 실리고 있었다.

추정: 인증이 계속 실패했을 것이다. 그것도 왜 실패하는지 메시지가 안 나오는 종류로. bytes를 헤더에 넣는 실수는 어떤 환경에선 조용히 통과하고 어떤 서버에선 거절된다. 34분 만에 엔진을 갈아엎었다는 건 원인 추적을 포기하고 **확실히 되는 규격으로 후퇴**했다는 뜻이다.

키 입력창에 눈 아이콘 토글을 붙인 것도 같은 흔적이다. 마스킹된 키에서 오타를 찾을 방법이 없었다.

## 소회

새로 나온 것보다 확실히 동작하는 것. 돈이 오가는 구간에선 이게 맞다. 지금 봇도 시뮬레이션으로 검증되지 않은 값은 배포하지 않는다.

이 34분이 알려준 게 하나 더 있다. 안 되는 걸 붙들고 있는 시간보다, 되는 길로 갈아타는 결단이 쌀 때가 있다.

> 제시 리버모어는 시장이 틀린 게 아니라 사람이 틀린 거라고 했다. 코드도 같다. API가 이상한 게 아니라 내 서명이 틀린 거였다.
