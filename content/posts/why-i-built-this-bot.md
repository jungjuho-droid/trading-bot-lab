---
title: "감정을 지워버린 트레이더 | Crypto Trading Bot"
date: 2026-04-20T10:00:00+09:00
draft: false
tags: ["개발기", "철학", "트레이딩심리", "자동매매", "알고리즘트레이딩", "업비트", "빗썸", "눌림목전략", "리스크관리"]
summary: "왜 이 Bot을 만들게 됐는가 — 바쁜 삶, 심리 게임, 그리고 EC2에서 맥북까지."
---

## 시간이 없는 사람의 투자

직장인의 하루엔 남는 시간이 별로 없다. 아침에 출근해서 회의 몇 개 치르고, 밀린 일 쳐내다 보면 해가 진다. 퇴근하고 나면 이미 지쳐서, 뭘 배우거나 공부할 여유조차 안 생긴다. 그런 삶 속에서 소소하게 시작한 주식이나 코인 투자는, 대개 물리는 걸로 끝났다. 사놓고 잊어버리거나, 잊어버리려다 다시 열어보거나. 차트를 들여다볼 시간은 없는데, 계좌를 신경 쓸 이유는 매일 생겼다.

이 구조가 왜 나쁘냐면, 시간이 없는 사람일수록 **판단의 밀도가 낮아지기 때문**이다. 하루 종일 차트를 보는 사람은 틀려도 자주 틀리고 자주 고친다. 그런데 하루에 세 번 계좌를 여는 사람은 그 세 번의 순간에 모든 결정이 몰린다. 그리고 그 세 번은 대개 마음이 불편해서 여는 순간이다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>계좌를 여는 순간의 분포</em></div>
<pre><code>  출근길 지하철   <span class="c">간밤에 뭔 일 있었나</span>
  점심시간        <span class="r">아까 빨간불이었는데</span>
  자기 전         <span class="r">오늘 왜 이렇게 빠졌지</span>
<span class="c">  --------------------------------------------------</span>
<span class="r">  전부 "불안해서" 여는 순간이다</span>
<span class="r">  그리고 그 자리에서 결정을 내린다</span>
<span class="g">  → 판단의 횟수는 적은데 전부 감정 상태에서 나온다</span></code></pre>
</div>

시간이 없다는 건 정보가 부족하다는 뜻만이 아니다. **차분한 상태에서 판단할 기회가 없다**는 뜻이다. 이게 내가 처음 인정해야 했던 사실이다.

## 감정이 계좌를 움직인다

인간은 원래 그런 존재다. 계좌가 -20%를 찍으면 갑자기 기도가 늘어난다. "제발 본전만..." 하면서 평소엔 믿지도 않던 것들에 빌게 된다. 반대로 +5%만 떠도 휴대폰에서 손을 못 뗀다. 더 오를까 봐, 지금 안 팔면 놓칠까 봐.

냉정하게 보면 둘 다 같은 병이다 — 숫자가 계좌를 움직이는 게 아니라, 감정이 계좌를 움직이고 있는 거다. 손실 앞에서는 근거 없는 희망을 붙잡고, 수익 앞에서는 근거 없는 불안을 붙잡는다. 어느 쪽이든 판단은 이미 감정에 넘어간 뒤였다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>같은 병의 두 얼굴</em></div>
<pre><code><span class="r">  [ -20% ]</span>  "본전만 오면 판다"
            <span class="c">→ 손절선이 사후에 만들어진다</span>
            <span class="c">→ 실은 손실을 인정하기 싫은 것</span>

<span class="r">  [ +5% ]</span>   "지금 팔면 더 오를 텐데"
            <span class="c">→ 익절 기준이 사후에 사라진다</span>
            <span class="c">→ 실은 놓치는 게 두려운 것</span>
<span class="c">  --------------------------------------------------</span>
<span class="g">  공통점: 진입 전에 정해둔 게 없다</span>
<span class="g">  결정을 그 순간에 하니까 감정이 이긴다</span></code></pre>
</div>

이 표를 그려보고 나서야 문제의 정체를 알았다. 내가 감정적인 게 문제가 아니라, **감정이 개입할 자리에 결정이 놓여 있었던 게** 문제였다. 진입 전에 손절선과 익절선을 정해두면 그 순간에 할 일이 없다. 정해둔 대로 하면 된다. 그런데 대부분의 개인 투자는 그 순서가 반대다. 일단 사고, 나중에 어떻게 할지 그때 생각한다.

## 결론은 심리 게임이었다

몇 번 겪어보니 결론은 하나였다. 투자는 결국 심리 게임이더라. 차트도, 뉴스도, 재무제표도 아니고 결국은 그 앞에 앉은 사람의 감정이 승패를 갈랐다.

그렇다면 답은 생각보다 간단했다. 감정과 본성을 아예 매매 과정에서 빼버리면 된다. 철저한 기준, 철저한 로직 — 사람이 개입할 틈을 최소화하는 것. 그게 이 Bot의 출발점이었다.

여기서 오해를 하나 풀어둬야겠다. 봇을 만든 이유가 **더 잘 벌기 위해서가 아니었다.** 나보다 똑똑한 알고리즘을 만들 자신이 없었다. 다만 나보다 규율 있는 알고리즘은 만들 수 있을 것 같았다. 규칙을 정해두고 그대로 실행하는 건 코드가 사람보다 압도적으로 잘하는 일이니까.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>봇이 사람보다 잘하는 것 / 못하는 것</em></div>
<pre><code><span class="g">  잘하는 것</span>
   · 정해둔 규칙을 <span class="g">예외 없이</span> 실행한다
   · 손실 중에도 손이 안 떨린다
   · 24시간 같은 기준으로 본다
   · 어제 성적을 오늘 판단에 안 섞는다

<span class="r">  못하는 것</span>
   · 처음 보는 상황을 해석한다
   · 뉴스의 맥락을 읽는다
   · 규칙 자체가 틀렸다는 걸 안다
<span class="c">  --------------------------------------------------</span>
<span class="g">  그래서 규칙을 정하는 건 내 일 · 지키는 건 봇 일</span></code></pre>
</div>

역할 분담이 명확해지니 마음이 편해졌다. 내가 할 일은 차분할 때 규칙을 정하는 것이고, 봇이 할 일은 불편한 순간에 그 규칙을 지키는 것이다. 내가 제일 못하는 게 두 번째였다.

## 랩톱 한 대로 시작했다

처음엔 거창하지 않았다. 집 랩톱을 24시간 켜두고, 장기투자용으로 넣어둔 빗썸 계좌를 지키려고 만든 작은 프로그램이었다. 윈도우에서 tkinter로 창을 띄우고, 단타로 시세를 훑는 봇이었다.

그런데 랩톱을 상시로 돌리다 보니 이슈가 하나둘 터졌다. 재부팅 한 번, 업데이트 한 번이면 포지션이 그대로 방치됐다. 화면은 얼어붙어 있는데 포지션은 살아있는, 그 불안이 매일 쌓였다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>봇이 죽으면 벌어지는 일</em></div>
<pre><code>  프로세스 종료
     ↓
<span class="r">  손절 감시 정지</span>   <span class="c">기준가를 넘어도 아무도 안 판다</span>
<span class="r">  익절 감시 정지</span>   <span class="c">목표에 닿아도 그대로 지나간다</span>
<span class="r">  알림 정지</span>       <span class="c">죽었다는 사실조차 안 알려준다</span>
<span class="c">  --------------------------------------------------</span>
<span class="r">  자동매매에서 제일 무서운 건 잘못 사는 게 아니라</span>
<span class="r">  들고 있는데 아무도 안 보고 있는 상태다</span></code></pre>
</div>

손절선을 아무리 잘 정해놔도 프로세스가 죽어 있으면 그 값은 없는 것과 같다. 감정을 지우려고 만든 봇인데, 봇이 죽어 있을까 봐 불안해하는 상태가 된 것이다. 문제를 옮겨놓았을 뿐 없앤 게 아니었다.

그래서 EC2로 옮기려 했는데, 메모리 스펙이 Bot을 안정적으로 돌리기엔 너무 빠듯했다. 위험을 감수할 이유가 없었다. 결국 맥북을 샀다. 맥으로 옮기면서 창을 띄우던 GUI는 사라지고, 터미널 모니터링만 남았다 — 화면은 단순해졌지만, 대신 더 이상 재부팅에 떨지 않아도 됐다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>운영 환경이 바뀌며 사라진 것들</em></div>
<pre><code><span class="y">  윈도우 랩톱</span>
    창을 띄운다 → 창이 곧 프로세스
    <span class="r">업데이트·재부팅·절전에 취약</span>
    <span class="r">창을 봐야만 상황을 안다</span>

<span class="g">  맥북 + 터미널</span>
    세션에 붙여두고 돌린다
    <span class="g">GUI 소멸 → 화면 코드와 판단 코드 분리</span>
    <span class="g">알림으로 상태를 받는다</span>
<span class="c">  --------------------------------------------------</span>
<span class="c">  하드웨어를 바꾼 김에 구조도 정리됐다</span></code></pre>
</div>

돌아보면 이 이사가 기술적으로도 전환점이었다. GUI를 버리면서 화면 그리는 코드와 판단하는 코드가 분리됐고, 그 분리가 나중에 전략을 검증 가능하게 만드는 전제가 됐다. 불안 때문에 산 노트북이 구조를 정리해준 셈이다.

## 수수료를 계좌로 배웠다

거기서 끝이 아니었다. 윈도우 버전에서 맥 버전으로, 단타에서 눌림목으로 — Bot도 나도 그렇게 조금씩 바뀌었다.

처음엔 순전히 호기심으로 시작한 단타 HFT였다. 초 단위로 사고파는 봇을 만들어보고 싶었다. 그런데 왕복 수수료의 무게를 계좌로 직접 배우고 나서야 전략을 다시 짰다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>회전율은 비용을 곱한다</em></div>
<pre><code>  왕복 비용 <span class="y">a</span> · 회전 <span class="y">n</span>회 → 누적 비용 <span class="y">a × n</span>
<span class="c">  --------------------------------------------------</span>
<span class="r">  단타</span>    회전 많음 · 회당 목표 작음
          <span class="r">비용이 목표를 잠식한다</span>
          <span class="r">승률이 높아도 계좌는 준다</span>
<span class="g">  스윙</span>    회전 적음 · 회당 목표 큼
          <span class="g">같은 비용이 훨씬 덜 아프다</span>
<span class="c">  --------------------------------------------------</span>
<span class="c">  ※ 실제 요율은 거래소·등급마다 다르다</span>
<span class="c">  요점은 숫자가 아니라 구조다</span></code></pre>
</div>

숫자로는 별거 아닌 것 같은데, 하루에 수십 번 돌리면 그게 전부 나간다. 그리고 더 중요한 게 있었다. **단타 봇은 내가 원래 고치려던 문제를 오히려 키웠다.** 로그가 끊임없이 올라가니까 화면을 계속 보게 된다. 감정을 지우려고 만든 봇 앞에 하루 종일 앉아 있게 된 것이다.

이 자각이 방향을 바꿨다. 좋은 자동매매는 성적이 좋은 게 아니라 **안 봐도 되는 것**이라는 기준이 생겼다.

## 봇을 만들면서 알게 된 나

이 프로젝트가 예상 못 한 걸 하나 줬다. **내가 어떻게 판단하는 사람인지 알게 됐다.**

규칙을 코드로 옮기려면 애매하게 둘 수가 없다. "많이 빠지면 산다"를 그대로 못 쓴다. 얼마나 빠져야 많이 빠진 건지, 무엇 대비 빠진 건지, 얼마 동안 빠진 건지를 전부 숫자로 적어야 한다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>말로는 되는데 코드로는 안 되는 것들</em></div>
<pre><code>  "<span class="y">많이</span> 빠지면 산다"
     → 얼마나? 무엇 대비? 며칠 동안?
  "<span class="y">거래량이 붙으면</span> 산다"
     → 평소 대비 몇 배? 평소는 며칠 평균?
  "<span class="y">분위기가 안 좋으면</span> 쉰다"
     → 무엇으로 판정? 어느 주기로?
<span class="c">  --------------------------------------------------</span>
<span class="r">  코드로 옮기려는 순간, 내가 사실 아무것도</span>
<span class="r">  정해두지 않았다는 게 드러난다</span></code></pre>
</div>

그 과정에서 알게 됐다. 나는 **규칙이 있다고 생각했지 실제로는 없었다.** 머릿속에 있던 건 규칙이 아니라 느낌이었고, 느낌은 그날 기분에 따라 기준이 바뀐다. 같은 -5%가 어떤 날은 기회고 어떤 날은 위험 신호였다.

봇을 만드는 작업의 절반은 코딩이 아니라 **내 기준을 문장으로 적어내는 일**이었다. 그리고 적어놓고 보면 대부분 근거가 없다. 그때부터 근거를 찾기 시작했고, 그게 지금의 검증 습관이 됐다.

## 자동화가 옮겨놓는 문제

한 가지 더 배운 게 있다. 자동화는 문제를 없애는 게 아니라 옮긴다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>해결한 문제 → 새로 생긴 문제</em></div>
<pre><code><span class="g">  감정적 매매를 막았다</span>
     → <span class="r">봇이 잘 돌고 있는지 불안해진다</span>
<span class="g">  화면을 안 봐도 되게 했다</span>
     → <span class="r">봇이 죽었는지 알 방법이 필요해진다</span>
<span class="g">  규칙을 코드로 고정했다</span>
     → <span class="r">규칙이 틀렸을 때 알아챌 방법이 필요해진다</span>
<span class="c">  --------------------------------------------------</span>
<span class="g">  → 알림 · 무결성 검사 · 매매기록 검증이 여기서 나왔다</span></code></pre>
</div>

세 번째가 제일 어렵다. 봇은 규칙을 완벽하게 지키는데, 그 규칙 자체가 틀렸으면 완벽하게 틀린 방향으로 간다. 사람이 매매하면 뭔가 이상하다는 느낌이 들어서 멈추는데, 봇은 안 멈춘다.

그래서 결국 기록과 검증이 필요해졌다. 봇이 규칙대로 했는지가 아니라, **그 규칙이 여전히 맞는지**를 주기적으로 확인해야 한다. 자동매매를 오래 하려면 봇을 만드는 것보다 이 확인 절차를 만드는 게 더 중요하더라.

## 여섯 번의 시대

빗썸에서 시작한 엔진은 곧 업비트로 옮겨 갔고, 이동평균 기반 스캔, 단일파일 모놀리스, 여러 전략이 동시에 경쟁하던 병렬 실험기를 거쳐, 지금은 git으로 관리하는 모듈형 구조에 정착했다. 그 사이에 버전은 수백 개를 넘겼고, 시행착오 하나하나가 지금 로직의 게이트 하나, 조건 하나로 남아 있다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>각 시대가 남긴 한 가지</em></div>
<pre><code><span class="w">  빗썸 기원기</span>    수수료의 무게 · 리스크 관리의 부재를 자각
<span class="w">  MA봇 전환기</span>    봇이 종목을 스스로 고르기 시작
<span class="w">  단일파일 진화기</span>  구조가 없으면 검증이 불가능하다
<span class="w">  병렬 실험기</span>     전략보다 "지금이 어떤 장인가" 가 먼저
<span class="w">  VVWAP기</span>        시장 판단이 처음 코드가 되다
<span class="g">  VV 모듈 시대</span>    근거 없는 값은 배포하지 않는다
<span class="c">  --------------------------------------------------</span>
<span class="c">  각 시대를 끝낸 건 좋은 아이디어가 아니라</span>
<span class="c">  한계에 부딪힌 경험이었다</span></code></pre>
</div>

이 목록을 정리하면서 알게 된 게 하나 있다. 늘어난 코드의 대부분이 **"안 사는 이유"**였다는 것. 615줄짜리 첫 코드에도 읽고, 판단하고, 주문하는 뼈대는 다 있었다. 그 뒤로 붙은 건 거의 전부 진입을 막는 조건이다. 게이트, 슬롯 상한, 손절, 본전 사수, 손실 한도, 하락장 차단.

감정을 지우겠다고 시작했는데, 실제로 한 일은 **하지 말아야 할 것을 코드로 정해두는 것**이었다. 생각해보면 감정을 지운다는 게 그것 말고 무엇이겠나.

## 지금의 봇

지금은 과매도 구간에서 눌림목 반등을 노리는, 스윙에 가까운 구조로 자리를 잡았다. RSI와 거래량, 저점 근접도 같은 조건들을 여러 겹의 게이트로 걸러 종목을 고르고, 손절선을 정해두고, 일정 수익에 도달하면 본전을 지키는 안전장치를 걸고, 포트폴리오 전체가 목표한 만큼 벌면 미련 없이 수확한다. 그리고 시장 전체가 무너지는 구간에는 아예 신규 진입 자체를 막아버린다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>봇이 나 대신 참아주는 순간들</em></div>
<pre><code><span class="w">  손절선에 닿았을 때</span>
    사람: "조금만 더 버티면 돌아올 것 같은데"
    <span class="g">봇: 정해둔 대로 자른다</span>

<span class="w">  이익이 났을 때</span>
    사람: "지금 팔면 더 오를 텐데"
    <span class="g">봇: +0.8% 도달 → 하한선을 올려둔다</span>

<span class="w">  하락장에서 좋아 보이는 종목이 있을 때</span>
    사람: <span class="r">"이번엔 다를 거야"</span>
    <span class="g">봇: 신규 진입 자체를 안 한다</span>
<span class="c">  --------------------------------------------------</span>
<span class="c">  세 순간 모두 내가 실제로 틀렸던 자리다</span></code></pre>
</div>

마지막 항목이 특히 그렇다. 시장이 통째로 빠지는 날에는 좋아 보이는 종목이 오히려 많아진다. 다 빠졌으니 다 싸 보인다. 사람이었다면 "이번엔 다를 거야" 하고 들어갔을 자리다. 실제로 그렇게 들어가서 여러 번 물렸다.

## 규칙을 정하는 사람과 지키는 코드

봇을 운영하면서 규칙이 하나 더 생겼다. **파라미터를 바꿀 때 근거 수치를 같이 남긴다는 것.** 손절선을 몇 퍼센트로 할지, 진입 문턱을 어디에 둘지 — 감으로 정하지 않고 실제 매매 기록을 그 값으로 다시 돌려본다. 그리고 결과를 커밋 메시지에 적는다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>왜 근거를 적어두나</em></div>
<pre><code><span class="g">  1.</span> 틀렸을 때 <span class="g">왜 틀렸는지</span> 추적할 수 있다
<span class="g">  2.</span> 과거의 나와 <span class="g">논쟁</span>할 수 있다
      <span class="c">"석 달 전엔 이 값이 좋다고 했는데 뭐가 달라졌나"</span>
<span class="g">  3.</span> 같은 실험을 <span class="g">반복하지 않게</span> 된다
<span class="g">  4.</span> 바꾸기 어렵게 만든다 <span class="c">← 이것도 안전장치</span>
<span class="c">  --------------------------------------------------</span>
<span class="r">  근거 없이 정한 값은 틀려도 배울 게 없다</span></code></pre>
</div>

4번이 의외로 중요하다. 값을 바꾸려면 시뮬레이션을 먼저 돌려야 하니 귀찮아서 안 바꾸게 되는 경우가 생긴다. 그것도 나쁘지 않다고 본다. **바꾸기 어렵게 만드는 것 자체가 안전장치**니까. 성적이 안 좋은 날에 충동적으로 파라미터를 만지는 걸 막아준다.

결국 이것도 같은 이야기다. 차분할 때 정한 규칙이 불편한 순간의 나를 이기게 하는 것. 봇에 손절선을 넣는 것과 배포 절차를 만드는 건 다른 층위에서 같은 일을 한다.

## 자동매매를 시작하려는 분께

이 글을 읽고 봇을 만들어볼까 하는 분이 있다면, 몇 달 먼저 해본 사람으로서 몇 가지만 적어두고 싶다.

<div class="term">
<div class="term-bar"><i></i><i></i><i></i><em>먼저 해봤으면 좋았을 것들</em></div>
<pre><code><span class="g">  1.</span> <span class="g">전략보다 기록을 먼저 만든다</span>
      <span class="c">전략은 어차피 바뀐다. 기록은 계속 쌓인다</span>
      <span class="c">기록 없는 기간은 나중에 복원이 안 된다</span>
<span class="g">  2.</span> <span class="g">"안 사는 규칙" 을 일찍 넣는다</span>
      <span class="c">진입 조건 다듬기가 재밌지만</span>
      <span class="c">계좌를 지키는 건 슬롯 상한과 손실 한도다</span>
<span class="g">  3.</span> <span class="g">조용한 실패를 시끄럽게 만든다</span>
      <span class="c">주문이 거부됐는데 그냥 넘어가는 게 제일 위험</span>
      <span class="c">"안 샀다" 와 "못 샀다" 를 구분할 수 있어야</span>
<span class="g">  4.</span> <span class="g">키와 설정을 코드에서 분리한다</span>
      <span class="c">10분이면 되는 작업. 안 하면 두고두고 발목</span></code></pre>
</div>

1번이 특히 그렇다. 초기 몇 주 동안 봇은 실제로 사고팔고 있었는데 그 기록을 안 남겼다. 전략이 미숙했으니 의미 없다고 생각했는데, 미숙한 전략의 기록도 데이터다. 지금 두 달치가 더 있었으면 훨씬 나은 판단을 했을 것 같다.

그리고 하나 더. **봇이 돈을 벌어줄 거라는 기대로 시작하면 오래 못 간다.** 초기 몇 달은 거의 확실히 마이너스다. 코드가 미숙해서가 아니라 규칙이 아직 없어서 그렇다. 그 구간을 버티려면 다른 동기가 필요하다. 나는 "내가 못 하는 걸 코드가 대신하는 게 재밌어서" 버텼다.

## 가장 솔직한 이유

돌아보면 이 Bot은 나 대신 감정을 참아주는 존재다. 나는 여전히 -20%에서 기도하고 싶고, +5%에서 휴대폰을 놓기 싫어하는 인간이니까. 대신 로직이 참는다.

그리고 하나 더 있다. 봇은 **어제를 오늘에 안 섞는다.** 사람은 어제 크게 잃으면 오늘 만회하려 들고, 어제 크게 벌면 오늘 대담해진다. 봇은 매일 같은 기준으로 본다. 이게 성적에 얼마나 기여하는지는 숫자로 모르겠지만, 계좌를 오래 유지하는 데는 확실히 도움이 됐다.

지금도 매일 플러스인 건 아니다. 다만 지금의 봇은 자기가 왜 그 값으로 돌아가는지 전부 답할 수 있다. 나한테는 그게 수익률보다 먼저 온 자산이다.

내가 못 하는 일을, 코드로 짜서 대신 시키는 것 — 어쩌면 이게 자동매매 봇을 만드는 가장 솔직한 이유일지도 모른다.

> 제시 리버모어는 시장이 인간의 감정을 먹고 산다고 했다. 나는 여기에 한 줄만 더 붙이고 싶다 — 감정을 이길 수 없다면, 감정이 끼어들 자리 자체를 코드로 지워버리면 된다.

---

## English

There isn't much spare time in a working professional's day. You show up, sit through a few meetings, clear the backlog, and the sun is already down. By the time you get home, you're too drained to learn or study anything new. Within that kind of life, the stock and crypto investing I dabbled in on the side almost always ended the same way: bags I was stuck holding. I'd buy, forget, and either stay forgotten or check back in out of anxiety. I never had time to actually study a chart, but somehow I always had a reason to worry about the account.

That's just how humans are wired. The moment an account drops -20%, the praying starts — "please, just let me break even" — bargaining with things you don't normally believe in. And the moment it's up +5%, you can't put the phone down, afraid it'll go higher, afraid that if you don't sell right now you'll miss it. Looked at coldly, both are the same disease. It isn't the numbers moving the account — it's emotion. In loss, you grab onto baseless hope. In gain, you grab onto baseless anxiety. Either way, the decision has already been handed over to feeling.

After going through that cycle a few times, I landed on one conclusion: investing is, in the end, a psychology game. Not the chart, not the news, not the fundamentals — it's the emotional state of the person sitting in front of the screen that decides the outcome. And if that's true, the fix turned out to be simpler than expected: strip emotion and human nature out of the trading process entirely. Strict criteria, strict logic — minimize the room for a person to step in. That's where this Bot started.

It didn't start big. It was a small program running on a laptop at home, left on 24/7, built just to protect a long-term investment account on Bithumb. A Windows box with a tkinter window, scanning the market for short-term entries. But running a laptop around the clock brought its own problems, one after another. A single reboot or update and open positions sat there unmanaged — the screen frozen while the position stayed live. That anxiety compounded daily. So I tried moving it to EC2, but the memory spec was too tight to run the Bot reliably. There was no reason to take that risk. In the end, I bought a MacBook. Moving to Mac, the GUI window disappeared — the screen got simpler, but I also stopped flinching every time a reboot was due.

That wasn't the end of it. From a Windows version to a Mac version, from day trading to pullback entries — the Bot changed, and so did I, little by little. It started as pure curiosity: a day-trading HFT bot. Only after learning the weight of a round-trip fee the hard way, through my own account, did I rebuild the strategy. The engine that started on Bithumb soon moved to Upbit, passed through a moving-average scanner, a single-file monolith, and an era where several strategies competed in parallel, before settling into the git-managed, modular structure it runs on today. Along the way the version count climbed into the hundreds, and every round of trial and error is still there — as a gate, a condition, a line of logic in what runs now.

Today it's settled into something closer to a swing structure, hunting for pullback rebounds in oversold conditions. It filters candidates through layered gates — RSI, volume, proximity to a recent low — sets a stop loss up front, locks in breakeven once a position clears a certain gain, and harvests the whole portfolio without hesitation once it hits its target. And when the broader market is falling apart, it simply refuses to open new positions at all — exactly the spot where a human would've told themselves "this time is different" and jumped in anyway.

Looking back, this Bot is what holds the emotions I can't. I'm still the kind of person who wants to pray at -20% and can't let go of the phone at +5%. The logic holds the line instead. And there's one more thing: the bot doesn't carry yesterday into today. People try to make back a big loss and get bold after a big win. The bot looks at every day through the same lens. Writing code to do the thing I can't do myself — that might be the most honest reason to build a trading bot at all.

> Jesse Livermore said the market feeds on human emotion. I'd only add one line to that — if you can't beat emotion, delete the space where it gets a say, and write that space into code instead.
