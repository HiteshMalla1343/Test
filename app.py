import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="A Little Question of Love 💗",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# This app is intentionally self-contained: the quiz, scoring, animations and transitions
# run in the embedded HTML/CSS/JavaScript, so no external image assets are required.
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}
    [data-testid="stAppViewContainer"] {background: #fff7fb;}
    [data-testid="stHeader"] {height: 0;}
    [data-testid="stMainBlockContainer"] {padding: 0 !important; max-width: 100% !important;}
    iframe {border: 0;}
</style>
""", unsafe_allow_html=True)

html = r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');
:root{--pink:#ff5d91;--deep:#9f174d;--ink:#3e2031;--muted:#8e6c7d;--cream:#fff7fb}
*{box-sizing:border-box}
html,body{margin:0;min-height:100%;font-family:'DM Sans',sans-serif;color:var(--ink);background:radial-gradient(circle at 10% 0%,#ffe0ed 0,transparent 35%),radial-gradient(circle at 95% 25%,#ffe9d5 0,transparent 30%),var(--cream)}
body{overflow-x:hidden}
#app{min-height:100vh;display:flex;justify-content:center;align-items:center;padding:28px 16px;position:relative;isolation:isolate}
.glow{position:fixed;inset:0;pointer-events:none;z-index:-1;background:radial-gradient(ellipse at center,rgba(255,255,255,.65),transparent 65%)}
.card{width:min(760px,100%);background:rgba(255,255,255,.82);border:1px solid rgba(255,255,255,.9);box-shadow:0 24px 80px rgba(145,41,86,.12);border-radius:30px;padding:clamp(24px,5vw,52px);text-align:center;backdrop-filter:blur(14px);animation:arrive .65s cubic-bezier(.2,.8,.2,1) both}
@keyframes arrive{from{opacity:0;transform:translateY(18px) scale(.985)}to{opacity:1;transform:translateY(0) scale(1)}}
.eyebrow{display:inline-flex;align-items:center;gap:8px;padding:8px 13px;border-radius:999px;background:#fff0f6;color:#b52d65;font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase}
h1,h2{font-family:'Playfair Display',Georgia,serif;font-weight:600;letter-spacing:-.035em}
h1{font-size:clamp(36px,6vw,58px);line-height:1.08;margin:22px 0 14px}
h2{font-size:clamp(28px,4.5vw,42px);line-height:1.15;margin:12px 0}
p{color:var(--muted);font-size:16px;line-height:1.7;margin:0 auto;max-width:560px}
button{font-family:inherit;cursor:pointer;border:0;transition:transform .22s,box-shadow .22s,background .22s}
button:focus-visible{outline:3px solid #ff9bbd;outline-offset:4px}
.primary{margin-top:28px;border-radius:999px;padding:15px 25px;background:linear-gradient(135deg,#ff79a5,#f14380);color:white;font-size:15px;font-weight:700;box-shadow:0 10px 24px rgba(241,67,128,.25)}
.primary:hover{transform:translateY(-2px);box-shadow:0 14px 30px rgba(241,67,128,.33)}
.tiny{font-size:12px;margin-top:18px;color:#b99aaa}
.progress-wrap{height:6px;border-radius:99px;background:#f7e4ed;overflow:hidden;margin:0 0 26px}
.progress{height:100%;width:0;background:linear-gradient(90deg,#ff9cba,#f13f7e);border-radius:99px;transition:width .5s ease}
.q-number{font-size:12px;letter-spacing:.13em;text-transform:uppercase;color:#c15a83;font-weight:700}
.question{font-size:clamp(24px,4vw,34px);margin:13px auto 24px;max-width:610px}
.options{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:10px}
.option{padding:16px 14px;background:#fff9fc;border:1.5px solid #f2dbe5;border-radius:17px;color:#61364b;text-align:left;font-weight:600;font-size:15px;min-height:62px}
.option:hover{border-color:#ff8bb0;transform:translateY(-2px);background:#fff2f7}
.option.selected{border-color:#f14c86;background:#fff0f6;box-shadow:inset 0 0 0 1px #f14c86}
.option .letter{display:inline-grid;place-items:center;width:27px;height:27px;border-radius:9px;background:#fbe3ed;color:#b33366;font-size:12px;margin-right:9px}
.answer-feedback{margin-top:16px;min-height:24px;font-weight:700;font-size:14px;line-height:1.5}
.answer-feedback.correct{color:#218653}
.answer-feedback.wrong{color:#c13c65}
.navrow{display:flex;justify-content:space-between;gap:12px;margin-top:26px}
.secondary{background:transparent;color:#9b6e83;font-weight:700;padding:13px 18px;border-radius:999px}
.secondary:hover{background:#fff0f6}
.navrow .primary{margin:0}
.hidden{display:none!important}
.big-heart{font-size:clamp(95px,19vw,170px);line-height:1;display:inline-block;filter:drop-shadow(0 14px 18px rgba(241,67,128,.22));animation:heartbeat 1.25s ease-in-out infinite}
@keyframes heartbeat{0%,100%{transform:scale(1)}12%{transform:scale(1.09)}24%{transform:scale(1)}36%{transform:scale(1.06)}50%{transform:scale(1)}}
.score-line{font-weight:700;color:#b62f67;margin-top:14px}
.stage{display:flex;min-height:390px;flex-direction:column;align-items:center;justify-content:center;position:relative;overflow:hidden}
.stage-title{font-family:'Playfair Display',Georgia,serif;font-size:clamp(25px,4vw,39px);margin:14px 0 7px}
.stage-sub{font-size:14px;color:#a37b8d}
.scale-object{font-size:48px;line-height:1.1;display:flex;align-items:center;justify-content:center;min-width:60px;min-height:60px;transform-origin:center;filter:drop-shadow(0 10px 18px rgba(214,71,127,.14))}
.scale-object.transition{animation:scaleIn 1.05s cubic-bezier(.2,.85,.25,1) both}
@keyframes scaleIn{0%{opacity:0;transform:scale(.18) rotate(-12deg);filter:blur(5px)}65%{opacity:1;transform:scale(1.08) rotate(2deg);filter:blur(0)}100%{opacity:1;transform:scale(1) rotate(0)}}
.scale-visual{width:min(420px,85%);height:190px;display:flex;align-items:center;justify-content:center;position:relative}
.scale-visual:before{content:'';position:absolute;width:170px;height:170px;border-radius:50%;background:radial-gradient(circle,rgba(255,114,164,.16),transparent 70%);animation:halo 2s ease-in-out infinite}
@keyframes halo{50%{transform:scale(1.5);opacity:.55}}
.heart-rain{position:fixed;inset:0;pointer-events:none;overflow:hidden;z-index:20}
.float-heart{position:absolute;bottom:-50px;animation:floatUp linear forwards;opacity:0;filter:drop-shadow(0 5px 6px rgba(227,55,116,.12))}
@keyframes floatUp{0%{transform:translateY(0) rotate(0) scale(.7);opacity:0}10%{opacity:.95}80%{opacity:.85}100%{transform:translateY(-115vh) rotate(35deg) scale(1.25);opacity:0}}
.confetti{position:fixed;top:-20px;z-index:30;pointer-events:none;animation:confettiFall 3.3s ease-in forwards}
@keyframes confettiFall{to{transform:translateY(110vh) rotate(720deg);opacity:.1}}
.final-message{font-family:'Playfair Display',Georgia,serif;font-size:clamp(28px,5vw,48px);line-height:1.2;color:#a51f58;margin:18px 0 12px}
.final-note{font-size:16px;max-width:550px}
@media(max-width:540px){.card{border-radius:23px;padding:24px 18px}.options{grid-template-columns:1fr}.option{min-height:55px}.stage{min-height:350px}.navrow{align-items:center}.primary{padding:14px 20px}}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{animation-duration:.01ms!important;animation-iteration-count:1!important;scroll-behavior:auto!important;transition-duration:.01ms!important}}
</style>
</head>
<body>
<div class="glow"></div><div id="app">
<section class="card" id="welcome">
  <div class="eyebrow">♡ a tiny love quiz ♡</div>
  <h1>Bujjiiii<br>Happy Monthiversary</h1>
  <p>I made a few questions just for you. Pick the answers that feel right, and at the end, let’s see how big my heart for you can get. Spoiler: the scale might be a little unfair. 💗</p>
  <button class="primary" onclick="startQuiz()">Okay, let’s do this <span aria-hidden="true">→</span></button>
  <div class="tiny">Made with an unreasonable amount of love.</div>
</section>

<section class="card hidden" id="quiz">
  <div class="progress-wrap"><div class="progress" id="progress"></div></div>
  <div class="q-number" id="qnumber">QUESTION 1 OF 10</div>
  <h2 class="question" id="question"></h2>
  <div class="options" id="options"></div>
  <div id="answerFeedback" class="answer-feedback" aria-live="polite"></div>
  <div class="navrow"><button class="secondary" id="back" onclick="prevQuestion()">← Back</button><button class="primary" id="next" onclick="nextQuestion()">Next →</button></div>
  <div class="tiny">No pressure. Just choose what you think! ♡</div>
</section>

<section class="card hidden" id="result">
  <div class="eyebrow">your official love report</div>
  <div id="resultHeart" class="big-heart">💗</div>
  <h2 id="resultTitle">A heart, just for you</h2>
  <p id="resultCopy"></p>
  <div class="score-line" id="scoreLine"></div>
  <button class="primary" id="journeyButton" onclick="beginJourney()">See how big my love is <span aria-hidden="true">→</span></button>
  <div class="tiny">Warning: may contain excessive cuteness.</div>
</section>

<section class="card hidden" id="journey">
  <div class="eyebrow">measuring my love</div>
  <div class="stage">
    <div class="stage-sub">A love that keeps growing</div>
    <div class="scale-visual"><div class="scale-object" id="scaleObject">🌾</div></div>
    <div class="stage-title" id="stageTitle">The size of a grain of rice</div>
    <p id="stageDescription">A tiny beginning… but even this is full of love.</p>
  </div>
  <button class="primary" id="nextStageButton" onclick="nextStage()">Next size →</button>
  <div class="tiny">Just when you think it can’t get any bigger…</div>
</section>

<section class="card hidden" id="final">
  <div class="eyebrow">the only answer that matters</div>
  <div class="big-heart">❤️</div>
  <div class="final-message">My love for you is bigger than the universe.</div>
  <p class="final-note">And even that doesn’t quite cover it. You make ordinary days feel special, you make me smile in ways I can’t explain, and if I had to choose all over again, I’d still choose you. Today, tomorrow, and all the little moments in between. ♡</p>
  <div style="font-size:28px;margin-top:22px;letter-spacing:8px">💗 💖 💞</div>
  <button class="primary" onclick="replay()">One more time? ↻</button>
</section>
</div>
<div class="heart-rain" id="heartRain"></div>
<script>
const questions = [
 {q:"What is my favourite kind of moment with you?",a:["Doing absolutely nothing together","Going on a little adventure","Talking for hours","All of the above"],correct:3},
 {q:"If I had a rough day, what would help most?",a:["A hug from you","Your voice and a chat","Something silly to make me laugh","Honestly, any time with you"],correct:2},
 {q:"What do I think makes you special?",a:["Your smile","Your kind heart","The way you are unapologetically you","Every single thing"],correct:3},
 {q:"Our perfect date would be…",a:["A cosy evening together","A spontaneous little trip","Good food and endless talking","Anything, as long as it’s with you"],correct:3},
 {q:"What do I want us to keep doing?",a:["Making each other laugh","Being there for each other","Making little memories","All of these, always"],correct:3},
 {q:"When do you look the cutest to me?",a:["When you’re smiling","When you’re excited about something","When you’re being silly","You really want me to pick just one?"],correct:3},
 {q:"What is one thing I never want you to doubt?",a:["That you matter to me","That I’m proud of you","That you can talk to me","That you are loved"],correct:0},
 {q:"If we could teleport anywhere right now…",a:["Somewhere peaceful","Somewhere with amazing food","Somewhere new to explore","Wherever we can be together"],correct:1},
 {q:"What do I hope you feel when you’re with me?",a:["Safe","Seen and understood","Happy and appreciated","All of the above"],correct:3},
 {q:"What's my favorite chocolaty snack?",a:["Waffle","Milkshake","Icecream","Chocolate"],correct:0}
];
let answers = Array(questions.length).fill(null), current=0, score=0, journeyTimer=null;
const $ = id => document.getElementById(id);
function show(id){['welcome','quiz','result','journey','final'].forEach(x=>$(x).classList.toggle('hidden',x!==id));window.scrollTo({top:0,behavior:'smooth'});}
function startQuiz(){current=0;renderQuestion();show('quiz');}
function renderQuestion(){
 const item=questions[current];
 $('qnumber').textContent=`QUESTION ${current+1} OF ${questions.length}`;
 $('question').textContent=item.q;
 $('progress').style.width=`${(current/questions.length)*100}%`;
 $('back').style.visibility=current===0?'hidden':'visible';
 $('next').textContent=current===questions.length-1?'Reveal my score ♡':'Next →';
 $('options').innerHTML='';
 item.a.forEach((answer,i)=>{
   const b=document.createElement('button');
   b.className='option'+(answers[current]===i?' selected':'');
   b.innerHTML=`<span class="letter">${String.fromCharCode(65+i)}</span>${answer}`;
   b.onclick=()=>{answers[current]=i;renderQuestion();};
   $('options').appendChild(b);
 });
 const feedback=$('answerFeedback');
 feedback.className='answer-feedback';
 if(answers[current]===null){
   feedback.textContent='';
 }else if(answers[current]===item.correct){
   feedback.classList.add('correct');
   feedback.textContent='✓ Correct! You know us so well. 💗';
 }else{
   feedback.classList.add('wrong');
   feedback.textContent=`Not quite! 💕 `;
 }
}
function nextQuestion(){if(answers[current]===null){$('question').animate([{transform:'translateX(-5px)'},{transform:'translateX(5px)'},{transform:'translateX(0)'}],{duration:230});return;}
 if(current<questions.length-1){current++;renderQuestion();}else finishQuiz();}
function prevQuestion(){if(current>0){current--;renderQuestion();}}
function heartFor(s){return s===10?'💖':s>=7?'💗':s>=4?'💓':'🤍';}
function finishQuiz(){
 score=answers.reduce((n,a,i)=>n+(a===questions[i].correct?1:0),0);
 $('resultHeart').textContent=heartFor(score);
 $('scoreLine').textContent=`You scored ${score}/10`;
 $('resultTitle').textContent=score===10?'PERFECT SCORE, PARTY TIME!':score>=7?'A heart full of love':'A little heart, a lot of love';
 $('resultCopy').textContent=score===10?'10 out of 10! You know us so well. Initiating maximum-cuteness protocol…':score>=7?'Pretty great! But don’t worry: my love isn’t graded, and you get full marks for being you.':'The quiz may have tricked you, but my heart is still yours. No score could measure this.';
 $('journeyButton').textContent=score===10?'Celebrate & measure my love! →':'See how big my love is →';
 $('progress').style.width='100%';show('result');
 if(score===10){confettiBurst();startHearts(4500,30);}
}
function confettiBurst(){const symbols=['💗','💖','💕','✨','🎉','♥'];for(let i=0;i<65;i++){const el=document.createElement('div');el.className='confetti';el.textContent=symbols[Math.floor(Math.random()*symbols.length)];el.style.left=Math.random()*100+'vw';el.style.fontSize=(14+Math.random()*20)+'px';el.style.animationDelay=(Math.random()*.9)+'s';el.style.animationDuration=(2.5+Math.random()*2)+'s';document.body.appendChild(el);setTimeout(()=>el.remove(),5200);}}
let heartInterval=null;
function startHearts(duration=6000,rate=15){const rain=$('heartRain');const end=Date.now()+duration;if(heartInterval)clearInterval(heartInterval);heartInterval=setInterval(()=>{for(let j=0;j<rate;j++){const el=document.createElement('span');el.className='float-heart';el.textContent=['💗','💖','💕','💘','♥','✨'][Math.floor(Math.random()*6)];el.style.left=Math.random()*100+'%';el.style.fontSize=(15+Math.random()*28)+'px';el.style.animationDuration=(3.5+Math.random()*4)+'s';rain.appendChild(el);setTimeout(()=>el.remove(),8000);}if(Date.now()>end){clearInterval(heartInterval);heartInterval=null;}},380);}
const stages=[
 {name:'The size of a grain of rice',emoji:'🌾',desc:'Tiny enough to fit on a fingertip. Still, every little bit is yours.',size:0.45},
 {name:'The size of a bug',emoji:'🐞',desc:'A little bigger… like the butterflies you give me.',size:0.72},
 {name:'The size of a dog',emoji:'🐕',desc:'Big enough for a cuddle, a wagging tail, and all the happy chaos.',size:1.05},
 {name:'The size of a human',emoji:'🧍',desc:'A whole person’s worth of love. And then some.',size:1.35},
 {name:'The size of an elephant',emoji:'🐘',desc:'Massive, gentle, and impossible to ignore.',size:1.7},
 {name:'The size of a building',emoji:'🏢',desc:'A love with its own skyline.',size:2.1},
 {name:'The size of the Burj Khalifa',emoji:'🏙️',desc:'Taller than the tallest building on Earth. Still not tall enough.',size:2.5},
 {name:'The size of Earth',emoji:'🌍',desc:'A whole planet could hold all these feelings… maybe.',size:2.9},
 {name:'The size of the Sun',emoji:'☀️',desc:'A star’s worth of warmth, shining just for you.',size:3.2},
 {name:'The size of this universe',emoji:'🌌',desc:'Every star, every galaxy, every little speck of space…',size:3.5}
];
let stageIndex=0;
function beginJourney(){
 stageIndex=0;
 show('journey');
 startHearts(4000,8);
 renderStage();
}
function renderStage(){
 const s=stages[stageIndex];
 $('scaleObject').textContent=s.emoji;
 $('scaleObject').style.fontSize=(48+s.size*19)+'px';
 $('scaleObject').classList.remove('transition');
 void $('scaleObject').offsetWidth;
 $('scaleObject').classList.add('transition');
 $('stageTitle').textContent=s.name;
 $('stageDescription').textContent=s.desc;
 $('nextStageButton').textContent=stageIndex===stages.length-1?'Reveal my love ♡':'Next size →';
}
function nextStage(){
 if(stageIndex<stages.length-1){
   stageIndex++;
   renderStage();
 }else{
   show('final');
   startHearts(15000,22);
   confettiBurst();
 }
}
function replay(){answers=Array(questions.length).fill(null);current=0;score=0;if(journeyTimer)clearTimeout(journeyTimer);if(heartInterval)clearInterval(heartInterval);$('heartRain').innerHTML='';document.querySelectorAll('.confetti').forEach(x=>x.remove());show('welcome');}
</script>
</body></html>
"""

components.html(html, height=1050, scrolling=True)
