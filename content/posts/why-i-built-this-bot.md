---
title: "감정을 지워버린 트레이더"
date: 2026-04-20T10:00:00+09:00
draft: false
tags: ["개발기", "철학", "트레이딩심리", "자동매매", "알고리즘트레이딩", "업비트", "빗썸", "눌림목전략", "리스크관리", "Trading Bot Lab"]
summary: "왜 이 Bot을 만들게 됐는가 — 바쁜 삶, 심리 게임, 그리고 EC2에서 맥북까지."
---

직장인의 하루엔 남는 시간이 별로 없다. 아침에 출근해서 회의 몇 개 치르고, 밀린 일 쳐내다 보면 해가 진다. 퇴근하고 나면 이미 지쳐서, 뭘 배우거나 공부할 여유조차 안 생긴다. 그런 삶 속에서 소소하게 시작한 주식이나 코인 투자는, 대개 물리는 걸로 끝났다. 사놓고 잊어버리거나, 잊어버리려다 다시 열어보거나. 차트를 들여다볼 시간은 없는데, 계좌를 신경 쓸 이유는 매일 생겼다.

인간은 원래 그런 존재다. 계좌가 -20%를 찍으면 갑자기 기도가 늘어난다. "제발 본전만..." 하면서 평소엔 믿지도 않던 것들에 빌게 된다. 반대로 +5%만 떠도 휴대폰에서 손을 못 뗀다. 더 오를까 봐, 지금 안 팔면 놓칠까 봐. 냉정하게 보면 둘 다 같은 병이다 — 숫자가 계좌를 움직이는 게 아니라, 감정이 계좌를 움직이고 있는 거다. 손실 앞에서는 근거 없는 희망을 붙잡고, 수익 앞에서는 근거 없는 불안을 붙잡는다. 어느 쪽이든 판단은 이미 감정에 넘어간 뒤였다.

몇 번 겪어보니 결론은 하나였다. 투자는 결국 심리 게임이더라. 차트도, 뉴스도, 재무제표도 아니고 결국은 그 앞에 앉은 사람의 감정이 승패를 갈랐다. 그렇다면 답은 생각보다 간단했다. 감정과 본성을 아예 매매 과정에서 빼버리면 된다. 철저한 기준, 철저한 로직 — 사람이 개입할 틈을 최소화하는 것. 그게 이 Bot의 출발점이었다.

처음엔 거창하지 않았다. 집 랩톱을 24시간 켜두고, 장기투자용으로 넣어둔 빗썸 계좌를 지키려고 만든 작은 프로그램이었다. 윈도우에서 tkinter로 창을 띄우고, 단타로 시세를 훑는 봇이었다. 그런데 랩톱을 상시로 돌리다 보니 이슈가 하나둘 터졌다. 재부팅 한 번, 업데이트 한 번이면 포지션이 그대로 방치됐다. 화면은 얼어붙어 있는데 포지션은 살아있는, 그 불안이 매일 쌓였다. 그래서 EC2로 옮기려 했는데, 메모리 스펙이 Bot을 안정적으로 돌리기엔 너무 빠듯했다. 위험을 감수할 이유가 없었다. 결국 맥북을 샀다. 맥으로 옮기면서 창을 띄우던 GUI는 사라지고, 터미널 모니터링만 남았다 — 화면은 단순해졌지만, 대신 더 이상 재부팅에 떨지 않아도 됐다.

거기서 끝이 아니었다. 윈도우 버전에서 맥 버전으로, 단타에서 눌림목으로 — Bot도 나도 그렇게 조금씩 바뀌었다. 처음엔 순전히 호기심으로 시작한 단타 HFT였는데, 왕복 수수료 0.1%의 무게를 계좌로 직접 배우고 나서야 전략을 다시 짰다. 빗썸에서 시작한 엔진은 곧 업비트로 옮겨 갔고, 이동평균 기반 스캔, 단일파일 모놀리스, 여러 전략이 동시에 경쟁하던 병렬 실험기를 거쳐, 지금은 git으로 관리하는 모듈형 구조에 정착했다. 그 사이에 버전은 수백 개를 넘겼고, 시행착오 하나하나가 지금 로직의 게이트 하나, 조건 하나로 남아 있다.

지금은 과매도 구간에서 눌림목 반등을 노리는, 스윙에 가까운 구조로 자리를 잡았다. RSI와 거래량, 저점 근접도 같은 조건들을 여러 겹의 게이트로 걸러 종목을 고르고, 손절선을 정해두고, 일정 수익에 도달하면 본전을 지키는 안전장치를 걸고, 포트폴리오 전체가 목표한 만큼 벌면 미련 없이 수확한다. 그리고 시장 전체가 무너지는 구간에는 아예 신규 진입 자체를 막아버린다. 사람이었다면 "이번엔 다를 거야" 하고 들어갔을 자리다.

돌아보면 이 Bot은 나 대신 감정을 참아주는 존재다. 나는 여전히 -20%에서 기도하고 싶고, +5%에서 휴대폰을 놓기 싫어하는 인간이니까. 대신 로직이 참는다. 내가 못 하는 일을, 코드로 짜서 대신 시키는 것 — 어쩌면 이게 자동매매 봇을 만드는 가장 솔직한 이유일지도 모른다.

> 제시 리버모어는 시장이 인간의 감정을 먹고 산다고 했다. 나는 여기에 한 줄만 더 붙이고 싶다 — 감정을 이길 수 없다면, 감정이 끼어들 자리 자체를 코드로 지워버리면 된다.

Developer: JH JEONG

---

There isn't much spare time in a working professional's day. You show up, sit through a few meetings, clear the backlog, and the sun is already down. By the time you get home, you're too drained to learn or study anything new. Within that kind of life, the stock and crypto investing I dabbled in on the side almost always ended the same way: bags I was stuck holding. I'd buy, forget, and either stay forgotten or check back in out of anxiety. I never had time to actually study a chart, but somehow I always had a reason to worry about the account.

That's just how humans are wired. The moment an account drops -20%, the praying starts — "please, just let me break even" — bargaining with things you don't normally believe in. And the moment it's up +5%, you can't put the phone down, afraid it'll go higher, afraid that if you don't sell right now you'll miss it. Looked at coldly, both are the same disease. It isn't the numbers moving the account — it's emotion. In loss, you grab onto baseless hope. In gain, you grab onto baseless anxiety. Either way, the decision has already been handed over to feeling.

After going through that cycle a few times, I landed on one conclusion: investing is, in the end, a psychology game. Not the chart, not the news, not the fundamentals — it's the emotional state of the person sitting in front of the screen that decides the outcome. And if that's true, the fix turned out to be simpler than expected: strip emotion and human nature out of the trading process entirely. Strict criteria, strict logic — minimize the room for a person to step in. That's where this Bot started.

It didn't start big. It was a small program running on a laptop at home, left on 24/7, built just to protect a long-term investment account on Bithumb. A Windows box with a tkinter window, scanning the market for short-term entries. But running a laptop around the clock brought its own problems, one after another. A single reboot or update and open positions sat there unmanaged — the screen frozen while the position stayed live. That anxiety compounded daily. So I tried moving it to EC2, but the memory spec was too tight to run the Bot reliably. There was no reason to take that risk. In the end, I bought a MacBook. Moving to Mac, the GUI window disappeared — the screen got simpler, but I also stopped flinching every time a reboot was due.

That wasn't the end of it. From a Windows version to a Mac version, from day trading to pullback entries — the Bot changed, and so did I, little by little. It started as pure curiosity: a day-trading HFT bot. Only after learning the weight of a 0.1% round-trip fee the hard way, through my own account, did I rebuild the strategy. The engine that started on Bithumb soon moved to Upbit, passed through a moving-average scanner, a single-file monolith, and an era where several strategies competed in parallel, before settling into the git-managed, modular structure it runs on today. Along the way the version count climbed into the hundreds, and every round of trial and error is still there — as a gate, a condition, a line of logic in what runs now.

Today it's settled into something closer to a swing structure, hunting for pullback rebounds in oversold conditions. It filters candidates through layered gates — RSI, volume, proximity to a recent low — sets a stop loss up front, locks in breakeven once a position clears a certain gain, and harvests the whole portfolio without hesitation once it hits its target. And when the broader market is falling apart, it simply refuses to open new positions at all — exactly the spot where a human would've told themselves "this time is different" and jumped in anyway.

Looking back, this Bot is what holds the emotions I can't. I'm still the kind of person who wants to pray at -20% and can't let go of the phone at +5%. The logic holds the line instead. Writing code to do the thing I can't do myself — that might be the most honest reason to build a trading bot at all.

> Jesse Livermore said the market feeds on human emotion. I'd only add one line to that — if you can't beat emotion, delete the space where it gets a say, and write that space into code instead.

Developer: JH JEONG
