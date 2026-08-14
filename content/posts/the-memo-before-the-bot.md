---
title: "봇보다 먼저 있었던 건 메모 한 장"
description: "BT.ARTIFACTS · The Memo That Came Before the Bot"
date: 2026-05-25T09:00:00+09:00
draft: false
series: ["빗썸 기원기"]
tags: ["개발일지", "빗썸기원기", "빗썸", "윈도우", "tkinter", "요구사항", "트레일링스톱", "자동매매"]
summary: "코드보다 먼저 남은 건 요구사항 메모와 배치파일이었다. 이 봇의 0번째 기록."
---

## 배경

아카이브에서 가장 오래된 파일은 코드가 아니다. `Futuring Request.txt`, 2026년 5월 25일. 봇에게 뭘 고쳐달라고 적어둔 메모다. 옆에는 윈도우 실행용 배치파일이 같이 남아 있다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>C:\codezero — RunTrader.bat</em></div>
<pre><code><span class="c">C:\Trader&gt;</span> <span class="w">type RunTrader.bat</span>
@echo off
cd /d <span class="y">"C:\codezero"</span>
python <span class="y">"bithumb_pure_bot.py"</span>
pause
<span class="c">C:\Trader&gt;</span> <span class="w">dir</span>
 Futuring Request.txt   <span class="c">← 최초 요구사항 메모 (보존 최고문서)</span>
 bithumb.txt / BAPI.txt <span class="c">← 당시 API 규격 메모</span>
 bithum.pdf             <span class="c">← 거래소 문서</span>
 v81~v90_slot_states.json</code></pre>
</div>

## 무엇이 남았나

배치파일 네 줄이 이 시절을 다 설명한다. `C:\codezero`로 들어가서 파이썬을 띄우고 `pause`. 더블클릭으로 봇을 켜던 윈도우 시절이다.

메모 쪽이 더 재밌다. 대부분은 UI 요청이다. 시총 화면 색을 통일하고, 연결 버튼을 연결/연결해지 둘로 쪼개고, 입력창 글자를 크게. 그런데 그 사이에 이런 문장이 섞여 있다. **"목표 수익률 도달 시 50% 물량은 즉시 익절하고, 나머지 50%는 트레일링 스톱으로 추세를 끝까지 추적."** 그리고 마지막 줄, **"2중으로 창 실행을 막는 로직을 추가해줘."**

첫날부터 익절 폭, 손절 폭, 트레일링 스톱이 요구사항에 들어 있었다는 뜻이다. 그리고 저 마지막 한 줄은 바로 다음 버전 코드의 파일 머리에 그대로 박힌다.

## 소회

기록을 정리하다 알게 된 건, 코드를 짜기 전에 문장을 먼저 썼다는 사실이다. 그 문장들은 대부분 화면 이야기였지만, 그 안에 이미 "얼마에 팔고 얼마에 손절할지"가 들어 있었다.

461개 버전을 다시 여는 이유도 그거다. 뭘 고쳤는지보다 **왜 고쳐야 했는지**가 안 남으면, 다음에 또 같은 자리에서 넘어진다.

> 에드 세이코타는 모두가 시장에서 원하는 걸 얻는다고 했다. 스릴을 원하면 스릴을, 규칙을 원하면 규칙을. 이 메모는 내가 어느 쪽을 원하는지 처음 적어둔 문서였다.
