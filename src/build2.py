import os,sys,json,html
from urllib.parse import quote
HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.environ.get('CF_OUT',os.path.join(HERE,'..','_build'))
os.makedirs(OUT,exist_ok=True)

HEAD='''<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Figtree:wght@300;400;500;600;700;800&display=swap" rel="stylesheet"><script src="https://cdn.tailwindcss.com/3.4.17"></script>
<script>tailwind.config={theme:{extend:{fontFamily:{sans:['Figtree','ui-sans-serif','system-ui','sans-serif'],serif:['Figtree','ui-sans-serif','system-ui','sans-serif']}}}}</script>
<script src="https://unpkg.com/lucide@0.469.0/dist/umd/lucide.min.js"></script><link rel="icon" type="image/png" href="assets/icone.png">'''

CSS='''
:root{--bg:#fafaf9;--ink:#111827;--glass:rgba(255,255,255,.95);color-scheme:light}
html{background:var(--bg)}
body{margin:0;font-family:'Figtree',system-ui,sans-serif;background:linear-gradient(135deg,#fafaf9,#fff 50%,rgba(236,253,245,.4));color:var(--ink);overflow-x:hidden;-webkit-font-smoothing:antialiased}
.glass-effect{backdrop-filter:blur(20px);background:var(--glass);border:1px solid rgba(255,255,255,.2)}
.gradient-border{background:linear-gradient(white,white) padding-box,linear-gradient(135deg,#10b981,#059669) border-box;border:2px solid transparent}
.js .rv{opacity:0;transform:translateY(24px);transition:opacity .8s ease-out,transform .8s ease-out}
.js .rv.in{opacity:1;transform:none}
.d2{transition-delay:.15s!important}.d3{transition-delay:.3s!important}.d4{transition-delay:.45s!important}
.js .rv.in.done{transition:transform .35s cubic-bezier(.22,1,.36,1),box-shadow .35s ease,border-color .35s ease,background-color .35s ease,opacity .35s ease}
.lift:hover,.lift-s:hover{border-color:#a7f3d0}
@media (hover:hover){
.js .rv.in.done.lift:hover{transform:translateY(-6px);box-shadow:0 22px 40px -14px rgba(6,95,70,.28)}
.js .rv.in.done.lift-t:hover{transform:translateY(-6px)}
.js .rv.in.done.lift-s:hover{box-shadow:0 12px 26px -12px rgba(6,95,70,.25)}
}
a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible{outline:2px solid #047857;outline-offset:3px}
.sem-dot{width:14px;height:14px;border-radius:9999px;display:block}
.fld{width:100%;border:1px solid #d6d3d1;border-radius:.9rem;background:#fff;padding:.75rem 1rem;font:500 .95rem Figtree,sans-serif;color:#111827}
.lbl{font-size:.8rem;font-weight:600;color:#44403c;margin-bottom:.35rem;display:block}
@view-transition{navigation:auto}
nav.glass-effect{view-transition-name:site-nav}
@keyframes pageIn{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
@keyframes fadeOnly{from{opacity:0}to{opacity:1}}
main{animation:pageIn .65s cubic-bezier(.22,1,.36,1) backwards}
footer{animation:fadeOnly .7s .2s ease-out backwards}
main,footer{transition:opacity .22s ease,transform .22s ease}
body.leaving main,body.leaving footer{opacity:0;transform:translateY(-10px)}
.card-link{transition:transform .3s ease}
.plan{position:relative;overflow:hidden;isolation:isolate;cursor:default}
.plan::before{content:'';position:absolute;inset:0;z-index:-1;background:linear-gradient(135deg,#065f46,#064e3b);opacity:0;transition:opacity .4s ease}
.plan .pt,.plan .pn,.plan .ps{transition:color .4s ease}
.plan:hover::before,.plan:active::before{opacity:1}
.plan:hover .pt,.plan:hover .pn,.plan:active .pt,.plan:active .pn{color:#fff}
.plan:hover .ps,.plan:active .ps{color:#a7f3d0}
[hidden]{display:none!important}
.wa-fab{position:fixed;right:max(16px,env(safe-area-inset-right));bottom:max(16px,env(safe-area-inset-bottom));z-index:60;width:56px;height:56px;border-radius:9999px;background:#16a34a;color:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 25px rgba(0,0,0,.25);transition:transform .25s ease,background-color .25s ease}
.wa-fab:hover{transform:scale(1.08);background:#15803d}
.wa-fab svg{width:30px;height:30px}
details>summary{list-style:none}details>summary::-webkit-details-marker{display:none}
details>summary::after{content:'+';float:right;font-weight:500;color:#047857;margin-left:1rem}
details[open]>summary::after{content:'\\2212'}
/* Tipografia: títulos em Figtree, sem itálico nos destaques (cor verde destaca) */
.font-serif{font-weight:700!important;letter-spacing:-.01em!important}
.font-serif .italic,.font-serif .font-light{font-style:normal!important;font-weight:inherit!important}
h1.font-serif{line-height:1.1!important;font-size:clamp(2.25rem,4.3vw,3.6rem)!important}
h2.font-serif{line-height:1.15!important}
h3.font-serif{line-height:1.2!important}
/* Artigos do blog */
.post h2{font-family:'Figtree',sans-serif;font-weight:700;font-size:1.55rem;line-height:1.2;margin:2.4rem 0 .8rem;letter-spacing:-.01em}
.post h3{font-weight:700;font-size:1.2rem;margin:1.8rem 0 .6rem}
.post p{color:#44403c;line-height:1.8;margin:0 0 1.15rem;font-size:1.06rem}
.post ul,.post ol{margin:0 0 1.4rem;padding-left:1.4rem;color:#44403c;line-height:1.75;font-size:1.06rem}
.post ul{list-style:disc}.post ol{list-style:decimal}
.post li{margin:.5rem 0;padding-left:.2rem}
.post li::marker{color:#059669;font-weight:700}
.post a{color:#047857;font-weight:600;text-decoration:underline;text-underline-offset:3px}
.post a:hover{color:#065f46}
.post strong{color:#111827}
@media(prefers-reduced-motion:reduce){*{transition:none!important}.lift:hover,.lift-t:hover{transform:none!important}.js .rv{opacity:1;transform:none}main,footer{animation:none}body.leaving main,body.leaving footer{opacity:1;transform:none}}
'''

JS='''
(function(){
  try{ if('scrollRestoration' in history) history.scrollRestoration='manual'; }catch(e){}
  function toTop(){
    if(location.hash) return;
    try{ window.scrollTo(0,0); document.documentElement.scrollTop=0; document.body.scrollTop=0;
      var t=document.getElementById('top'); if(t&&t.scrollIntoView) t.scrollIntoView({block:'start'}); }catch(e){}
  }
  toTop();
  document.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('a[href]');
    if(!a||e.defaultPrevented||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||e.button) return;
    var h=a.getAttribute('href');
    if(!h||h.charAt(0)==='#'||/^[a-z][a-z0-9+.-]*:/i.test(h)||a.target==='_blank'||a.hasAttribute('download')) return;
    document.body.classList.add('leaving');
  });
  window.addEventListener('pageshow',function(){document.body.classList.remove('leaving');});
  window.addEventListener('load',toTop);
  window.addEventListener('pageshow',toTop);
  try{ if(window.lucide) lucide.createIcons(); }catch(e){}
  var els=[].slice.call(document.querySelectorAll('.rv'));
  function show(el){el.classList.add('in');setTimeout(function(){el.classList.add('done');},1100);}
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){show(e.target);io.unobserve(e.target);}});},{threshold:.08,rootMargin:'0px 0px -40px 0px'});
    els.forEach(function(el){io.observe(el);});
    setTimeout(function(){els.forEach(function(el){if(!el.classList.contains('in'))show(el);});},2500);
  } else { els.forEach(show); }
  var b=document.getElementById('mbtn'),m=document.getElementById('mpanel');
  if(b&&m){b.addEventListener('click',function(){var h=m.hidden;m.hidden=!h;b.setAttribute('aria-expanded',String(h));});}
  document.querySelectorAll('[data-copy]').forEach(function(btn){
    btn.addEventListener('click',function(){
      var t=btn.getAttribute('data-copy'),old=btn.textContent;
      try{navigator.clipboard.writeText(t).then(function(){btn.textContent='Copiado';setTimeout(function(){btn.textContent=old;},1500);},function(){btn.textContent='Selecione o texto';});}
      catch(e){btn.textContent='Selecione o texto';}
    });
  });
  var tg=document.querySelectorAll('.tgl');
  if(tg.length){
    var notes={m:'Valor por condomínio, até 150 unidades. Sem fidelidade e sem taxa de saída.',a:'Pague 11 mensalidades e use 12. Cobrança uma vez por ano por condomínio, até 150 unidades. Sem fidelidade.'};
    tg.forEach(function(b){b.addEventListener('click',function(){
      var c=b.getAttribute('data-cycle');
      tg.forEach(function(x){var on=x===b;x.setAttribute('aria-pressed',String(on));x.className='tgl px-4 py-2 rounded-full '+(on?'bg-emerald-600 text-white':'text-gray-700');});
      document.querySelectorAll('[data-m]').forEach(function(el){el.querySelector('.num').textContent=el.getAttribute(c==='m'?'data-m':'data-a');var p=el.parentNode.querySelector('.per');if(p)p.textContent=c==='m'?'por condomínio ao mês':'por condomínio ao ano';});
      document.getElementById('price-note').textContent=notes[c];
    });});
  }
  var f=document.getElementById('msg-form');
  if(f){
    var C=window.CF_FORM||{};
    var svc=((C.provider==='formspree'&&C.endpoint)||(C.provider==='web3forms'&&C.accessKey))?C.provider:'';
    var btn=f.querySelector('button[type=submit]');
    var hint=document.getElementById('send-hint');
    if(svc&&hint) hint.textContent='Ao enviar, a mensagem segue por e-mail para a CondoFluxo e o WhatsApp abre com o texto pronto.';
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var v=function(id){return (document.getElementById(id).value||'').trim();};
      var st=document.getElementById('send-status');
      if(v('f-hp')) return;
      var nome=v('f-nome'),ret=v('f-ret');
      if(!nome){st.textContent='Informe o seu nome para enviar.';document.getElementById('f-nome').focus();return;}
      if(!ret){st.textContent='Informe um e-mail ou WhatsApp para retorno.';document.getElementById('f-ret').focus();return;}
      var papel=v('f-papel'),cond=v('f-cond'),cid=v('f-cid'),qtd=v('f-qtd'),int=v('f-int'),msg=v('f-msg');
      var t='Olá! Meu nome é '+nome+' e sou '+papel+(cond?' do condomínio '+cond:'')+(cid?', em '+cid:'')+'.\\n\\nContato para retorno: '+ret+'.'+(qtd?'\\n\\nQuantidade de condomínios: '+qtd+'.':'')+'\\n\\nTenho interesse em: '+int+'.\\n\\n'+msg+'\\n\\nObrigado!';
      var wa='https://wa.me/5551996117922?text='+encodeURIComponent(t);
      var mail='mailto:condofluxo@condofluxo.com.br?subject='+encodeURIComponent('Contato pelo site CondoFluxo')+'&body='+encodeURIComponent(t);
      document.getElementById('wa-send').href=wa;
      document.getElementById('mail-link').href=mail;
      document.getElementById('out-wrap').hidden=false;
      try{window.open(wa,'_blank','noopener');}catch(x){}
      if(!svc){
        st.textContent='Abrimos o WhatsApp e o seu programa de e-mail com a mensagem pronta. Confirme o envio em cada um.';
        try{window.location.href=mail;}catch(x){}
        return;
      }
      st.textContent='Enviando...'; btn.disabled=true;
      var data={name:nome,contato:ret,perfil:papel,condominio:cond,cidade:cid,quantidade:qtd,interesse:int,mensagem:t};
      if(/@/.test(ret)) data.email=ret;
      var url,body;
      if(svc==='formspree'){url=C.endpoint;body=Object.assign({_subject:'Contato pelo site CondoFluxo'},data);}
      else{url='https://api.web3forms.com/submit';body=Object.assign({access_key:C.accessKey,subject:'Contato pelo site CondoFluxo',from_name:'Site CondoFluxo',message:t},data);}
      fetch(url,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(body)})
        .then(function(r){return r.json().catch(function(){return {};}).then(function(j){return r.ok&&(svc==='formspree'||j.success===true);});})
        .catch(function(){return false;})
        .then(function(ok){
          btn.disabled=false;
          st.textContent=ok?'Recebemos a sua mensagem por e-mail. Abrimos também o WhatsApp com o texto pronto: é só confirmar o envio por lá.':'Não conseguimos enviar o e-mail automaticamente. Abrimos o WhatsApp com a mensagem pronta e, se preferir, use o link abaixo para enviar por e-mail.';
        });
    });
  }
})();
'''

LOGO='<img src="assets/logo-condofluxo.png" alt="CondoFluxo" class="h-9 w-auto" width="140" height="37">'
WORD=''

LINKS=[('gestao.html','Convivus'),('comunicacao.html','Comunicação'),('blog.html','Blog'),('sobre.html','Sobre')]

PORTAL_URL='https://portalconvivus.condofluxo.com.br'

def nav(cur):
    a=''.join(f'<a href="{h}" class="{"text-emerald-700" if h==cur else "text-gray-600"} hover:text-emerald-600 transition-colors">{t}</a>' for h,t in LINKS)
    m=''.join(f'<a href="{h}" class="py-2 text-gray-700">{t}</a>' for h,t in LINKS)
    a+=f'<a href="{PORTAL_URL}" target="_blank" rel="noopener" class="inline-flex items-center gap-1.5 border border-emerald-600 text-emerald-700 px-4 py-2 rounded-full hover:bg-emerald-50 transition-colors whitespace-nowrap"><i data-lucide="log-in" class="w-4 h-4"></i>Acesse o Portal Convivus</a>'
    m+=f'<a href="{PORTAL_URL}" target="_blank" rel="noopener" class="mt-2 inline-flex items-center justify-center gap-2 border border-emerald-600 text-emerald-700 px-4 py-3 rounded-full text-center"><i data-lucide="log-in" class="w-4 h-4"></i>Acesse o Portal Convivus</a>'
    return f'''<nav class="fixed top-0 w-full z-50 glass-effect" style="padding-top:env(safe-area-inset-top,0px)">
 <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="flex items-center justify-between h-16">
  <a href="index.html" class="flex items-center gap-2">{LOGO}{WORD}</a>
  <div class="hidden lg:flex items-center gap-6 xl:gap-8 text-sm font-medium">{a}<a href="contato.html" class="bg-emerald-600 text-white px-4 py-2 rounded-full hover:bg-emerald-700 transition-colors">Falar conosco</a></div>
  <button id="mbtn" class="lg:hidden text-sm font-semibold border border-gray-300 rounded-full px-4 py-2" aria-expanded="false" aria-controls="mpanel" type="button">Menu</button>
 </div>
 <div id="mpanel" class="lg:hidden pb-4 flex flex-col text-sm font-medium" hidden>{m}<a href="contato.html" class="mt-2 bg-emerald-600 text-white px-4 py-3 rounded-full text-center">Falar conosco</a></div></div></nav>'''

WA_SVG='<svg viewBox="0 0 24 24" class="{c}" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>'
IG_SVG='<svg viewBox="0 0 24 24" class="{c}" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".6" fill="currentColor"/></svg>'
def wa(c): return WA_SVG.replace('{c}',c)
def ig(c): return IG_SVG.replace('{c}',c)
WA_LINK='https://wa.me/5551996117922'
IG_LINK='https://www.instagram.com/condofluxo'
def walink(msg): return WA_LINK+'?text='+quote(msg)
SITE='https://www.condofluxo.com.br'

FOOT=f'''<footer class="border-t border-stone-200 bg-white/60"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 grid gap-8 md:grid-cols-3">
 <div><a href="index.html" class="flex items-center gap-2">{LOGO}{WORD}</a><p class="mt-4 text-sm text-gray-600 max-w-xs">Sob o mesmo teto: gestão do condomínio e comunicação com os moradores, numa só marca.</p></div>
 <div class="text-sm"><p class="font-semibold mb-3">Páginas</p><div class="flex flex-col gap-2 text-gray-600"><a href="gestao.html" class="hover:text-emerald-700">Convivus</a><a href="gestao.html#valores" class="hover:text-emerald-700">Valores</a><a href="comunicacao.html" class="hover:text-emerald-700">Comunicação</a><a href="blog.html" class="hover:text-emerald-700">Blog</a><a href="sobre.html" class="hover:text-emerald-700">Sobre</a><a href="contato.html" class="hover:text-emerald-700">Contato</a><a href="manutencao-predial-normativa.html" class="hover:text-emerald-700">Guia: manutenção predial</a><a href="ppci-avcb-guia.html" class="hover:text-emerald-700">Guia: PPCI e AVCB</a></div></div>
 <div class="text-sm"><p class="font-semibold mb-3">Contato</p><div class="flex flex-col gap-2 text-gray-600">
  <a href="{WA_LINK}" target="_blank" rel="noopener" class="flex items-center gap-2 hover:text-emerald-700">{wa('w-4 h-4 shrink-0 text-emerald-600')}+55 51 99611-7922</a>
  <span class="flex items-center gap-2 break-all"><i data-lucide="mail" class="w-4 h-4 shrink-0 text-emerald-600"></i>condofluxo@condofluxo.com.br</span>
  <a href="{IG_LINK}" target="_blank" rel="noopener" class="flex items-center gap-2 hover:text-emerald-700">{ig('w-4 h-4 shrink-0 text-emerald-600')}@condofluxo</a>
  <a href="https://www.condofluxo.com.br/gestao" target="_blank" rel="noopener" class="flex items-center gap-2 hover:text-emerald-700 break-all"><i data-lucide="globe" class="w-4 h-4 shrink-0 text-emerald-600"></i>www.condofluxo.com.br/gestao</a></div></div>
 </div><div class="border-t border-stone-200 py-5 text-center text-xs text-gray-500">© 2026 CondoFluxo. Todos os direitos reservados.</div></footer>'''

import shutil
shutil.copytree(os.path.join(HERE,'assets_src'),os.path.join(OUT,'assets'),dirs_exist_ok=True)

def cp(f):
    return '' if f=='index.html' else (f[:-5] if f.endswith('.html') else f)

def metas(title,desc,fname,ld,img=None):
    url=SITE+'/'+cp(fname)
    d=html.escape(desc,quote=True); t=html.escape(title,quote=True)
    m=f'<meta name="description" content="{d}"><meta name="theme-color" content="#065f46"><meta property="og:type" content="website"><meta property="og:locale" content="pt_BR"><meta property="og:site_name" content="CondoFluxo"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/{img or "assets/fachada-verde.jpg"}"><meta name="twitter:card" content="summary_large_image">'
    if ld:
        m+='<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@graph":ld},ensure_ascii=False).replace('</','<\\/')+'</script>'
    return m

def page(fname,title,cur,main,full,desc='',wamsg='Olá! Vim pelo site da CondoFluxo e gostaria de conversar.',ld=None,img=None,extra_head=''):
    fab=f'<a href="{walink(wamsg)}" target="_blank" rel="noopener" class="wa-fab" aria-label="Conversar pelo WhatsApp">{wa("")}</a>'
    body=f'<div id="top" style="position:absolute;top:0;left:0;width:1px;height:1px" aria-hidden="true"></div>{nav(cur)}\n<main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-28 pb-20 lg:pt-32">{main}</main>\n{FOOT}\n{fab}\n<script>{JS}</script>'
    pre='<script>document.documentElement.classList.add("js")</script>'
    mt=metas(title,desc,fname,ld,img) if desc else ''
    if full:
        doc=f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>{title}</title>{extra_head}{mt}{HEAD}<style>{CSS}</style>{pre}</head><body>{body}</body></html>'
    else:
        doc=f'<title>{title}</title>{extra_head}{mt}{HEAD}<style>{CSS}</style>{pre}\n{body}'
    open(os.path.join(OUT,fname),'w').write(doc)

def pill(icon,text):
    return f'<div class="inline-flex items-center gap-2 bg-emerald-50 text-emerald-700 px-3 py-1 rounded-full text-sm font-medium mb-6"><i data-lucide="{icon}" class="w-4 h-4"></i>{text}</div>'

def head(icon,pilltxt,h1a,h1b,p):
    return f'''<div class="max-w-3xl mb-14 rv">{pill(icon,pilltxt)}<h1 class="text-4xl sm:text-5xl lg:text-6xl leading-[1] font-medium tracking-tight font-serif">{h1a}<br><span class="font-light italic text-emerald-700">{h1b}</span></h1><p class="text-lg text-gray-600 mt-6 leading-relaxed">{p}</p></div>'''

def cta(t1,t2,btn,href='contato.html'):
    ext=' target="_blank" rel="noopener"' if href.startswith('http') else ''
    return f'''<div class="text-center mt-24 rv">{pill('shield-check','Sem compromisso')}<h2 class="font-serif text-3xl font-medium mb-4">{t1}</h2><p class="text-gray-600 mb-8 max-w-md mx-auto">{t2}</p><a href="{href}"{ext} class="gradient-border inline-block px-8 py-4 rounded-full font-semibold text-emerald-700 hover:shadow-lg transition-all duration-300 hover:scale-105">{btn}</a></div>'''

def small(icon,ibg,itx,t1,t2,desc,extra='',cls='bg-white border border-gray-100'):
    return f'''<div class="rounded-3xl {cls} p-6 flex flex-col gap-4 shadow-lg hover:shadow-xl transition-shadow duration-300 group lift rv"><div class="w-10 h-10 {ibg} rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform duration-300"><i data-lucide="{icon}" class="w-5 h-5 {itx}"></i></div><h3 class="font-serif text-xl font-medium leading-tight">{t1} <span class="italic font-light text-emerald-700">{t2}</span></h3><p class="text-sm text-gray-600 leading-relaxed">{desc}</p>{extra}</div>'''

def faq(items):
    return '<div class="grid gap-3 max-w-3xl">'+''.join(f'<details class="lift-s rounded-2xl bg-white border border-gray-100 shadow-sm p-5 rv"><summary class="font-semibold cursor-pointer">{q}</summary><p class="mt-3 text-gray-600 leading-relaxed">{a}</p></details>' for q,a in items)+'</div>'

def faq_ld(items):
    return {"@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in items]}

Q_PRECO=('Quanto custa o Convivus?','O valor é por condomínio e cai conforme a quantidade: R$ 119 por mês até 3 condomínios, R$ 109 de 4 a 7 e R$ 99 a partir de 8, para condomínios de até 150 unidades. No plano anual você paga 11 mensalidades e usa 12. Não há módulo pago à parte.')
Q_FID=('Tem fidelidade ou taxa de saída?','Não. Você cancela quando quiser, sem aviso prévio e sem taxa de saída.')
Q_ADM=('O Convivus substitui o sistema financeiro da administradora?','Não. O Convivus não é um sistema financeiro. Ele cuida da conformidade e da rotina do condomínio: manutenção ligada às normas, PPCI e AVCB, documentos com auditoria, avisos e chamados. Boletos e contabilidade seguem no sistema que o condomínio já usa.')
Q_APP=('Preciso instalar algum aplicativo?','Não. O Convivus abre no navegador do computador, do tablet e do celular.')
Q_PERF=('Quem acessa e o que cada pessoa vê?','Cada pessoa entra com um perfil definido por papel: Síndico, Subsíndico, Conselho, Morador, Zeladoria, Portaria, entre outros.')
Q_LGPD=('Como fica a LGPD?','O portal pede o consentimento de cada usuário no primeiro acesso.')
Q_LAUDO=('O portal emite laudos ou faz vistorias?','Não. O portal organiza prazos e registros, e o laudo fica anexado ao item de manutenção. Laudos e vistorias continuam com profissionais habilitados.')
Q_MULTI=('Serve para quem administra mais de um condomínio?','Sim. Uma conta reúne vários condomínios, com perfis de acesso por função, e o valor de cada um cai conforme a quantidade. Acima de 150 unidades somam-se R$ 25 por mês a cada bloco de 50, até 400 unidades. Acima disso, e para administradoras com muitos condomínios, o valor é sob consulta.')
Q_PPCI=('O controle de PPCI vale para qualquer estado?','O controle de APPCI e AVCB é feito por estado e já vem preenchido para o Rio Grande do Sul.')
FAQ_HOME=[Q_PRECO,Q_ADM,Q_APP,Q_FID]
FAQ_GESTAO=[Q_PRECO,Q_FID,Q_ADM,Q_APP,Q_PERF,Q_MULTI,Q_PPCI,Q_LAUDO,Q_LGPD]

SEM='''<div class="bg-white rounded-2xl p-4 shadow-sm text-gray-900 w-full max-w-sm">
<p class="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-3">Painel do síndico</p>
<div class="flex items-center gap-3 py-2 border-t border-gray-100 first-of-type:border-0"><span class="sem-dot bg-emerald-500"></span><span class="text-sm flex-1">Limpeza dos reservatórios</span><span class="text-xs font-bold text-emerald-700">Em dia</span></div>
<div class="flex items-center gap-3 py-2 border-t border-gray-100"><span class="sem-dot bg-amber-500"></span><span class="text-sm flex-1">Recarga dos extintores</span><span class="text-xs font-bold text-amber-700">A vencer</span></div>
<div class="flex items-center gap-3 py-2 border-t border-gray-100"><span class="sem-dot bg-red-600"></span><span class="text-sm flex-1">Ensaio do SPDA</span><span class="text-xs font-bold text-red-700">Vencido</span></div></div>'''

DAY=[('08h','layout-dashboard','bg-emerald-100','text-emerald-600','Painel do dia','O painel mostra o que está em dia, a vencer e vencido. PPCI e AVCB avisam antes da renovação.'),
('11h','megaphone','bg-rose-100','text-rose-600','Aviso para o bloco','Um comunicado sai para todo o condomínio ou só para um bloco, e o relatório mostra quem leu.'),
('15h','message-square-warning','bg-violet-100','text-violet-600','Chamado do morador','O morador abre o chamado pelo celular e acompanha o status até a resolução.'),
('18h','file-check-2','bg-blue-100','text-blue-600','Laudo no arquivo','O laudo é anexado ao item de manutenção, com o histórico de quem enviou, consultou e alterou.')]
day_cards=''.join(f'<div class="group lift rounded-3xl bg-white border border-gray-100 shadow-lg p-6 flex flex-col gap-4 rv {d}"><div class="flex items-center justify-between"><span class="font-serif text-3xl text-emerald-700 leading-none transition-all duration-300 group-hover:text-emerald-500 group-hover:translate-x-1">{h}</span><div class="w-10 h-10 {ib} rounded-xl flex items-center justify-center transition-transform duration-300 group-hover:scale-110 group-hover:-rotate-6"><i data-lucide="{ic}" class="w-5 h-5 {it}"></i></div></div><h3 class="font-semibold">{t}</h3><p class="text-sm text-gray-600 leading-relaxed">{p}</p></div>' for (h,ic,ib,it,t,p),d in zip(DAY,['','d2','d3','d4']))
day_html=f'''<section class="mt-24"><div class="max-w-3xl mb-8 rv">{pill('clock','Na prática')}<h2 class="font-serif text-3xl lg:text-4xl font-medium leading-tight">Um dia com o <span class="italic font-light text-emerald-700">Convivus</span></h2><p class="text-lg text-gray-600 mt-4">Da primeira checagem da manhã ao laudo arquivado no fim do dia, tudo no mesmo lugar.</p></div><div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">{day_cards}</div></section>'''

# ================= HOME =================
home=f'''
<div class="relative rounded-3xl overflow-hidden shadow-xl mb-12">
 <img src="assets/banner-portal.jpg" alt="" width="1800" height="670" class="absolute inset-0 w-full h-full object-cover object-right" fetchpriority="high">
 <div class="absolute inset-0 bg-white/85 lg:hidden"></div>
 <div class="absolute inset-0 hidden lg:block bg-gradient-to-r from-white/95 from-0% via-white/80 via-45% to-transparent to-80%"></div>
 <div class="relative flex flex-col gap-8 lg:flex-row lg:items-start lg:justify-between p-6 sm:p-10 lg:p-12">
 <div class="max-w-2xl rv">{pill('house','Sob o mesmo teto')}
  <h1 class="sm:text-5xl lg:text-6xl xl:text-7xl leading-[0.95] text-4xl font-medium tracking-tight font-serif">Gestão e convívio<br><span class="font-light italic text-emerald-700">do seu condomínio</span></h1>
  <p class="text-lg text-gray-600 mt-6 leading-relaxed max-w-lg">O CondoFluxo reúne duas frentes numa só marca: o portal de gestão Convivus, que mantém o condomínio em dia com as normas, e materiais de comunicação claros para os moradores.</p>
  <div class="mt-8 flex flex-wrap items-center gap-3"><a href="{walink('Olá! Quero agendar uma demonstração do Convivus.')}" target="_blank" rel="noopener" class="bg-emerald-600 text-white px-6 py-3 rounded-full font-medium hover:bg-emerald-700 transition-colors">Agendar demonstração</a><a href="gestao.html" class="px-6 py-3 rounded-full font-medium border border-gray-300 hover:border-emerald-600 hover:text-emerald-700 transition-colors">Conhecer o portal</a><a href="comunicacao.html" class="px-3 py-3 font-medium text-gray-600 hover:text-emerald-700 transition-colors">Ver comunicação</a></div>
  <p class="mt-5 text-sm text-gray-600 flex flex-wrap items-center gap-x-2 gap-y-1"><i data-lucide="badge-dollar-sign" class="w-4 h-4 text-emerald-600"></i><span>Convivus de <b>R$ 99</b> a <b>R$ 119</b> por condomínio ao mês, sem fidelidade.</span><a href="gestao.html#valores" class="font-semibold text-emerald-700 underline underline-offset-2">Ver valores</a></p></div>
 <div class="flex flex-col gap-4 lg:items-end rv d2"><div class="p-5 bg-white rounded-2xl shadow-sm border border-gray-100 flex flex-col gap-3 text-sm font-medium">
  <div class="flex items-center gap-3"><i data-lucide="globe" class="w-5 h-5 text-emerald-600"></i>Sem aplicativo para instalar</div>
  <div class="flex items-center gap-3"><i data-lucide="lock" class="w-5 h-5 text-emerald-600"></i>Consentimento LGPD no primeiro acesso</div></div></div>
</div></div>

<section class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-12 gap-4 auto-rows-auto">
 <div class="col-span-2 md:col-span-4 lg:col-span-5 lift-t rv"><div class="relative rounded-3xl overflow-hidden shadow-2xl h-full min-h-[420px] bg-emerald-900 p-6 lg:p-8 flex flex-col justify-between gap-8"><img src="assets/fachada-verde.jpg" alt="Fachada de um edifício residencial com detalhes em verde" class="absolute inset-0 w-full h-full object-cover" fetchpriority="high"><div class="absolute inset-0 bg-gradient-to-t from-black/40 via-black/10 to-black/30"></div>
  <div class="relative z-10 flex justify-center lg:justify-start">{SEM}</div>
  <div class="relative z-10 glass-effect p-4 lg:p-5 rounded-2xl shadow-xl lg:max-w-xs"><div class="flex items-start gap-3"><div class="w-10 h-10 bg-emerald-100 rounded-xl flex items-center justify-center shrink-0"><i data-lucide="clipboard-check" class="w-5 h-5 text-emerald-600"></i></div><div><h3 class="font-serif text-lg font-medium leading-tight">Prazo, responsável <span class="italic font-light text-emerald-700">e prova</span></h3><p class="text-sm text-gray-600 mt-2 leading-relaxed">Cada item de manutenção tem periodicidade, responsável e o laudo anexado.</p></div></div></div></div></div>

 <div class="col-span-2 md:col-span-2 lg:col-span-4 lift-t rv d2"><div class="h-full rounded-3xl bg-gradient-to-br from-emerald-800 to-emerald-900 text-white p-6 lg:p-8 relative overflow-hidden shadow-2xl flex flex-col justify-between gap-6">
  <div class="absolute inset-0 opacity-10"><div class="absolute top-4 right-4 w-24 h-24 rounded-full bg-white/10"></div><div class="absolute bottom-4 left-4 w-16 h-16 rounded-full bg-white/5"></div></div>
  <div class="relative z-10"><div class="flex items-center gap-3 mb-4"><div class="w-10 h-10 bg-white/20 rounded-xl flex items-center justify-center"><i data-lucide="book-open-check" class="w-5 h-5 text-emerald-200"></i></div><div class="px-3 py-1 bg-white/20 rounded-full text-xs font-medium">Normas ABNT</div></div>
   <h3 class="font-serif text-xl lg:text-2xl font-medium leading-tight mb-4">Normas no calendário <span class="italic font-light">do síndico</span></h3>
   <ul class="space-y-2 text-sm"><li class="flex gap-3"><i data-lucide="check" class="w-4 h-4 text-emerald-300 shrink-0 mt-0.5"></i>NBR 5674, manutenção</li><li class="flex gap-3"><i data-lucide="check" class="w-4 h-4 text-emerald-300 shrink-0 mt-0.5"></i>NBR 15575, desempenho</li><li class="flex gap-3"><i data-lucide="check" class="w-4 h-4 text-emerald-300 shrink-0 mt-0.5"></i>NBR 17170, garantias</li><li class="flex gap-3"><i data-lucide="check" class="w-4 h-4 text-emerald-300 shrink-0 mt-0.5"></i>NBR 16747, inspeção predial</li></ul></div>
  <div class="relative z-10 flex items-center justify-between gap-3"><span class="text-xs text-emerald-200">Mais de 39 itens cadastrados</span><a href="gestao.html" class="bg-white/20 hover:bg-white/30 px-3 py-2 rounded-full text-sm font-medium transition-colors">Ver Convivus</a></div></div></div>

 <div class="col-span-2 md:col-span-2 lg:col-span-3 lift-t rv d3"><div class="h-full rounded-3xl bg-white p-6 flex flex-col justify-between gap-4 shadow-lg hover:shadow-xl transition-shadow duration-300 border border-gray-100 group"><div><div class="w-10 h-10 bg-amber-100 rounded-xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform duration-300"><i data-lucide="key-round" class="w-5 h-5 text-amber-600"></i></div><h3 class="font-serif text-lg font-medium leading-tight mb-2">Controle de <span class="italic font-light text-emerald-700">acesso</span></h3><p class="text-sm text-gray-600 leading-relaxed">Perfis definidos por papel dentro do sistema: Síndico, Subsíndico, Conselho, Morador, Zeladoria, Portaria, entre outros.</p></div></div></div>

 <div class="col-span-2 md:col-span-2 lg:col-span-4 lift-t rv"><div class="h-full rounded-3xl bg-gradient-to-br from-stone-100 to-stone-50 p-6 flex flex-col justify-between gap-4 shadow-lg hover:shadow-xl transition-shadow duration-300 group"><div><div class="w-10 h-10 bg-emerald-600 rounded-xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform duration-300"><i data-lucide="flame" class="w-5 h-5 text-white"></i></div><h3 class="font-serif text-xl font-medium leading-tight mb-3">PPCI e <span class="italic font-light text-emerald-700">licença</span></h3><p class="text-sm text-gray-600 leading-relaxed mb-4">Licença do corpo de bombeiros do seu estado, com aviso antes da renovação. Já preenchido para o Rio Grande do Sul.</p><div class="flex items-center gap-2 text-sm font-medium text-emerald-700"><i data-lucide="circle-check-big" class="w-4 h-4"></i>CBMRS · APPCI · AVCB</div></div></div></div>

 <div class="col-span-2 md:col-span-2 lg:col-span-4 lift-t rv d2"><div class="h-full rounded-3xl bg-gradient-to-br from-blue-50 to-indigo-50 p-6 flex flex-col justify-between gap-4 shadow-lg hover:shadow-xl transition-shadow duration-300 group"><div><div class="w-10 h-10 bg-blue-100 rounded-xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform duration-300"><i data-lucide="file-check-2" class="w-5 h-5 text-blue-600"></i></div><h3 class="font-serif text-xl font-medium leading-tight mb-3">Documentos com <span class="italic font-light text-blue-700">auditoria</span></h3><p class="text-sm text-gray-600 leading-relaxed mb-4">Laudos, ARTs e licenças guardados com histórico de quem enviou, consultou e alterou.</p><div class="flex items-center gap-2 text-sm font-medium text-blue-700"><i data-lucide="history" class="w-4 h-4"></i>Livro de Ocorrências só recebe novos registros</div></div></div></div>

 <div class="col-span-2 md:col-span-4 lg:col-span-4 lift-t rv d3"><div class="relative rounded-3xl overflow-hidden shadow-xl h-full min-h-[260px] bg-teal-900 text-white p-6 flex flex-col justify-end"><img src="assets/morador-tablet.jpg" alt="Morador consultando o portal no tablet, na sala de casa" loading="lazy" class="absolute inset-0 w-full h-full object-cover"><div class="absolute inset-0 bg-gradient-to-t from-emerald-950/90 via-emerald-950/40 to-transparent"></div><div class="relative z-10"><h3 class="font-serif text-xl font-medium mb-2">CondoFluxo Comunicação</h3><p class="text-sm text-white/90 mb-4">Manual de Convivência, comunicados visuais e sites informativos para os moradores.</p><a href="comunicacao.html" class="inline-block bg-white/20 hover:bg-white/30 px-4 py-2 rounded-full text-sm font-medium transition-colors">Ver comunicação</a></div></div></div>
</section>

{day_html}
<section class="mt-24 grid gap-5 md:grid-cols-2">
 <div class="rounded-3xl bg-white border border-gray-100 shadow-lg p-8 flex flex-col gap-4 lift rv"><p class="text-xs font-semibold uppercase tracking-widest text-emerald-700">Produto · assinatura</p><img src="assets/logo-convivus.png" alt="Convivus" class="h-12 w-auto self-start"><p class="text-gray-600">Convivus, o portal para síndicos e moradores. Reúne a operação e a conformidade do condomínio num portal web, sem aplicativo para instalar.</p><a href="gestao.html" class="mt-auto inline-flex items-center gap-2 font-semibold text-emerald-700 hover:gap-3 transition-all">Conhecer o portal <i data-lucide="arrow-right" class="w-4 h-4"></i></a></div>
 <div class="rounded-3xl bg-white border border-gray-100 shadow-lg p-8 flex flex-col gap-4 lift rv d2"><p class="text-xs font-semibold uppercase tracking-widest text-emerald-700">Serviço · sob demanda</p><img src="assets/logo-condofluxo.png" alt="CondoFluxo" class="h-12 w-auto self-start"><p class="text-gray-600">Materiais de comunicação claros e profissionais que substituem o grupo de WhatsApp e os papéis soltos na portaria.</p><a href="comunicacao.html" class="mt-auto inline-flex items-center gap-2 font-semibold text-emerald-700 hover:gap-3 transition-all">Ver os materiais <i data-lucide="arrow-right" class="w-4 h-4"></i></a></div>
</section>
<section class="mt-24"><div class="max-w-3xl mb-8 rv">{pill('circle-help','Perguntas rápidas')}<h2 class="font-serif text-3xl lg:text-4xl font-medium leading-tight">O que síndicos <span class="italic font-light text-emerald-700">perguntam primeiro</span></h2></div>{faq(FAQ_HOME)}<p class="mt-5 text-sm text-gray-600 rv"><a href="gestao.html#perguntas" class="font-semibold text-emerald-700 underline underline-offset-2">Ver todas as perguntas</a></p></section>
{cta('Pronto para organizar o seu condomínio?','Conte como é o seu condomínio e receba retorno por WhatsApp, telefone ou e-mail.','Agendar demonstração',walink('Olá! Quero agendar uma demonstração do Convivus.'))}
'''
page('index.html','CondoFluxo','',home,os.environ.get('CF_FULL')=='1',
     desc='A CondoFluxo reúne o portal Convivus, que mantém o condomínio em dia com as normas, e materiais de comunicação para os moradores. Valores públicos e sem fidelidade.',
     ld=[{"@type":"Organization","name":"CondoFluxo","url":SITE,"logo":SITE+"/assets/logo-condofluxo.png","email":"condofluxo@condofluxo.com.br","telephone":"+55 51 99611-7922","sameAs":[IG_LINK]}])

def tier(name,m,a):
    return f'''<div class="plan lift rounded-3xl bg-white border border-gray-100 shadow-lg p-6 flex flex-col gap-2 rv"><p class="pt text-sm font-semibold text-gray-500">{name}</p><p class="pn font-serif text-4xl font-medium text-gray-900" data-m="{m}" data-a="{a}"><span class="ps text-base font-sans font-medium text-gray-500">R$</span> <span class="num">{m}</span></p><p class="ps text-xs text-gray-500 per">por condomínio ao mês</p></div>'''

TERMS=[('shield-check','Sem fidelidade','Cancele quando quiser, sem aviso prévio e sem taxa de saída.'),
('calendar-check','Plano anual','Pague 11 mensalidades e use 12. A cobrança é feita uma vez por ano, por condomínio.'),
('file-pen-line','Contratação','O serviço pode ser contratado por CNPJ ou por CPF.')]
terms_html=''.join(f'<div class="rounded-3xl bg-white border border-gray-100 shadow-lg p-6 flex gap-4 lift rv"><div class="w-10 h-10 bg-emerald-100 rounded-xl flex items-center justify-center shrink-0"><i data-lucide="{i}" class="w-5 h-5 text-emerald-600"></i></div><div><h3 class="font-semibold mb-1">{t}</h3><p class="text-sm text-gray-600 leading-relaxed">{d}</p></div></div>' for i,t,d in TERMS)
feat=''.join(f'<li class="flex gap-3"><i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0 mt-1"></i><span>{x}</span></li>' for x in ['Manutenção preventiva ancorada em ABNT NBR, com semáforo','Controle de PPCI e AVCB com alerta de renovação','Inspeção predial (NBR 16747)','Trilha de auditoria e Livro de Ocorrências que só recebe novos registros','Mural de avisos com confirmação de leitura por bloco','Chamados com controle de status','Canal do Morador e repositório de documentos','Vários condomínios e perfis de acesso','Suporte por e-mail'])
PRICING=f'''<section id="valores" class="mt-24 scroll-mt-24">
 <div class="max-w-3xl mb-10 rv">{pill('badge-dollar-sign','Valores')}<h2 class="font-serif text-4xl lg:text-5xl font-medium leading-tight">Um plano, <span class="italic font-light text-emerald-700">completo.</span></h2><p class="text-lg text-gray-600 mt-4">Sem módulo pago escondido. Quanto mais condomínios você administra, menor o valor de cada um.</p></div>
 <div class="grid gap-4 lg:grid-cols-5">
  <div class="lg:col-span-2 rounded-3xl bg-white border border-gray-100 shadow-lg p-8 rv"><h3 class="font-serif text-2xl font-medium mb-1">Plano <span class="italic font-light text-emerald-700">Compliance</span></h3><p class="text-sm text-gray-500 mb-5">Tudo o que está nesta página.</p><ul class="space-y-3 text-sm text-gray-700">{feat}</ul></div>
  <div class="lg:col-span-3 flex flex-col gap-4">
   <div class="flex flex-wrap items-center justify-between gap-3 rv"><div class="inline-flex rounded-full border border-gray-300 bg-white p-1 text-sm font-semibold" role="group" aria-label="Ciclo de cobrança"><button type="button" data-cycle="m" aria-pressed="true" class="tgl px-4 py-2 rounded-full bg-emerald-600 text-white">Mensal</button><button type="button" data-cycle="a" aria-pressed="false" class="tgl px-4 py-2 rounded-full text-gray-700">Anual · 1 mês grátis</button></div><p id="price-note" class="text-xs text-gray-500 max-w-xs">Valor por condomínio, até 150 unidades. Sem fidelidade e sem taxa de saída.</p></div>
   <div class="grid gap-4 sm:grid-cols-3">{tier('Até 3 condomínios','119','1.309')}{tier('4 a 7 condomínios','109','1.199')}{tier('8 ou mais','99','1.089')}</div>
   <div class="rounded-3xl bg-gradient-to-br from-stone-100 to-stone-50 shadow-lg p-6 rv text-sm text-gray-700 leading-relaxed"><p class="font-semibold mb-1">Condomínios maiores</p><p>Acima de 150 unidades, somam-se R$ 25 por mês a cada bloco de 50 unidades, até 400 unidades. Acima disso, o valor é sob consulta, assim como para administradoras com muitos condomínios.</p></div>
   <div class="flex flex-wrap items-center gap-x-5 gap-y-2 rv"><a href="{walink('Olá! Quero saber mais sobre o plano do Convivus.')}" target="_blank" rel="noopener" class="bg-emerald-600 text-white px-6 py-3 rounded-full font-medium hover:bg-emerald-700 transition-colors">Falar sobre o plano</a><a href="contato.html" class="text-sm font-semibold text-emerald-700 underline underline-offset-2">ou use o formulário</a></div>
  </div></div></section>
<section class="mt-24"><div class="max-w-3xl mb-10 rv">{pill('file-text','Condições')}<h2 class="font-serif text-4xl lg:text-5xl font-medium leading-tight">Como funciona <span class="italic font-light text-emerald-700">a contratação</span></h2></div>
 <div class="grid gap-4 md:grid-cols-3">{terms_html}</div>
 </section>'''

# ================= GESTÃO =================
mods=[('wrench','bg-emerald-100','text-emerald-600','Manutenção','normativa','Plano de manutenção com cada item ligado à norma ABNT que o fundamenta, com periodicidade, responsável e próxima data.'),
('flame','bg-amber-100','text-amber-600','PPCI e','licenciamento','Controle de APPCI e AVCB por estado, com aviso antes da renovação. Já preenchido para o Rio Grande do Sul.'),
('file-check-2','bg-blue-100','text-blue-600','Documentos com','auditoria','Repositório com histórico de quem enviou, consultou e alterou cada arquivo.'),
('megaphone','bg-rose-100','text-rose-600','Mural com','confirmação','Avisos para todo o condomínio ou para um bloco, com relatório de quem leu.'),
('message-square-warning','bg-violet-100','text-violet-600','Chamados e','ocorrências','Problemas registrados e acompanhados. O Livro de Ocorrências só recebe novos registros.'),
('building-2','bg-teal-100','text-teal-600','Vários','condomínios','Uma conta para quem administra mais de um condomínio, com perfis de acesso por função.')]
cards=''.join(small(i,b,t,a,c,d) for i,b,t,a,c,d in mods)
ges='<div class="mb-8 rv"><img src="assets/logo-convivus.png" alt="Convivus" class="h-14 w-auto"></div>'+head('layout-dashboard','Portal Convivus','Conformidade não é um extra.','É o coração do portal.','A maioria dos apps de condomínio cuida do financeiro. O Convivus se ancora onde está a responsabilidade legal do síndico, sem deixar de lado a conversa entre vizinhos.')
ges+='''<section class="grid gap-4 lg:grid-cols-5 mb-16">
 <div class="lg:col-span-3 relative rounded-3xl overflow-hidden shadow-2xl min-h-[280px] lg:min-h-[420px] rv"><img src="assets/portal-notebook.jpg" alt="Portal Convivus aberto em um tablet com teclado, sobre uma mesa" loading="lazy" class="absolute inset-0 w-full h-full object-cover"><div class="absolute inset-x-0 bottom-0 p-6 bg-gradient-to-t from-black/70 to-transparent text-white"><p class="font-serif text-xl">Sem aplicativo para instalar</p><p class="text-sm text-white/85">Abre no navegador do computador, do tablet e do celular.</p></div></div>
 <div class="lg:col-span-2 relative rounded-3xl overflow-hidden shadow-xl min-h-[320px] rv d2"><img src="assets/portal-celular.jpg" alt="Mão segurando um celular com o portal do condomínio aberto, no hall do prédio" loading="lazy" class="absolute inset-0 w-full h-full object-cover"><div class="absolute inset-x-0 bottom-0 p-6 bg-gradient-to-t from-black/70 to-transparent text-white"><p class="font-serif text-xl">Avisos na mão do morador</p><p class="text-sm text-white/85">Mural, chamados e documentos no celular.</p></div></div>
</section>'''
ges=ges.replace('''<section class="grid gap-4 lg:grid-cols-5 mb-16">''','''<div class="-mt-8 mb-12 flex flex-wrap items-center gap-3 rv"><a href="'''+walink('Olá! Vi o Convivus no site e quero agendar uma demonstração.')+'''" target="_blank" rel="noopener" class="bg-emerald-600 text-white px-6 py-3 rounded-full font-medium hover:bg-emerald-700 transition-colors">Agendar demonstração</a><a href="#valores" class="px-6 py-3 rounded-full font-medium border border-gray-300 hover:border-emerald-600 hover:text-emerald-700 transition-colors">Ver valores</a><p class="w-full text-sm text-gray-600 mt-1">Valores públicos: de R$ 99 a R$ 119 por condomínio ao mês. Sem fidelidade e sem taxa de saída.</p></div>
<section class="grid gap-4 lg:grid-cols-5 mb-16">''',1)
ges+=f'<section class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">{cards}</section>'
PERSONAS=[('user-round','bg-emerald-100','text-emerald-600','Para o','síndico morador','Você mora no prédio e assumiu a síndica. Prazos, laudos e licenças num só lugar, com semáforo para saber o que está em dia, a vencer ou vencido.'),
('briefcase','bg-amber-100','text-amber-600','Para o','síndico profissional','Vários condomínios numa só conta, com perfis de acesso por função e o histórico do que foi feito em cada um. O valor de cada condomínio cai a partir do quarto.'),
('building-2','bg-blue-100','text-blue-600','Para a','administradora','Complementa o sistema financeiro que você já usa, levando manutenção, licenças e documentos de cada condomínio para o mesmo lugar. Carteiras grandes têm valor sob consulta.'),
('hard-hat','bg-stone-200','text-stone-600','Para a','construtora','Entregue o condomínio com a rotina de manutenção organizada: itens ligados às normas de referência, como NBR 5674, NBR 15575 e NBR 17170, com periodicidade e responsável.')]
pers=''.join(small(i,b,t,a,c,d) for i,b,t,a,c,d in PERSONAS)
ges+=f'<section class="mt-24"><div class="max-w-3xl mb-8 rv">{pill("users","Para quem é")}<h2 class="font-serif text-3xl lg:text-4xl font-medium leading-tight">Um portal, <span class="italic font-light text-emerald-700">quatro perfis</span></h2></div><div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">{pers}</div></section>'
ges+=f'''<section class="mt-16 grid gap-4 lg:grid-cols-5">
 <div class="lg:col-span-3 rounded-3xl bg-gradient-to-br from-emerald-900 to-teal-800 text-white p-8 shadow-2xl rv"><h2 class="font-serif text-2xl lg:text-3xl font-medium mb-3">Semáforo de <span class="italic font-light text-emerald-200">vencimentos</span></h2><p class="text-emerald-50/90 mb-6 max-w-md text-sm leading-relaxed">Cada obrigação mostra se está em dia, a vencer ou vencida, para o síndico saber o que resolver primeiro.</p>{SEM}</div>
 <div class="lg:col-span-2 rounded-3xl bg-white border border-gray-100 shadow-lg p-8 rv d2"><h2 class="font-serif text-xl font-medium mb-4">Normas de <span class="italic font-light text-emerald-700">referência</span></h2><ul class="space-y-3 text-sm text-gray-700"><li><b>NBR 5674</b> · manutenção de edificações</li><li><b>NBR 15575</b> · desempenho de edificações</li><li><b>NBR 17170</b> · garantias</li><li><b>NBR 16747</b> · inspeção predial</li><li><b>CBMRS</b> · APPCI, licença de incêndio no RS</li><li><b>LGPD</b> · consentimento no acesso</li></ul><p class="mt-5 text-xs text-gray-500">O portal organiza prazos e registros. Laudos e vistorias continuam com profissionais habilitados.</p><div class="mt-4 flex flex-col gap-2"><a href="manutencao-predial-normativa.html" class="inline-flex items-center gap-2 text-sm font-semibold text-emerald-700 hover:gap-3 transition-all">Ler o guia de manutenção predial <i data-lucide="arrow-right" class="w-4 h-4"></i></a><a href="ppci-avcb-guia.html" class="inline-flex items-center gap-2 text-sm font-semibold text-emerald-700 hover:gap-3 transition-all">Ler o guia de PPCI e AVCB <i data-lucide="arrow-right" class="w-4 h-4"></i></a></div></div>
</section>'''
CMP=[('Vencimentos','Dependem de alguém lembrar.','Semáforo mostra o que está em dia, a vencer e vencido. PPCI e AVCB têm alerta de renovação.'),
('Norma','Itens sem norma de referência.','Cada item de manutenção ligado à norma ABNT que o fundamenta.'),
('Prova','Laudo perdido entre e-mails e pastas.','Laudos, ARTs e licenças com histórico de quem enviou, consultou e alterou.'),
('Ocorrências','Mensagens que podem ser apagadas.','Livro de Ocorrências que só recebe novos registros.'),
('Avisos','Ninguém sabe quem leu.','Mural com confirmação de leitura, por bloco ou para todos.'),
('Quem acessa','Quem recebe a planilha vê tudo.','Perfis por papel: Síndico, Subsíndico, Conselho, Morador, Zeladoria, Portaria.'),
('Troca de gestão','O histórico some junto com a planilha.','O histórico fica no portal, e não com uma pessoa.')]
cmp_rows=''.join(f'<div class="grid md:grid-cols-[1fr_1.2fr_1.6fr] border-t border-gray-100 transition-colors duration-300 hover:bg-emerald-50/60"><div class="px-5 pt-4 md:py-4 font-semibold">{a}</div><div class="px-5 py-1 md:py-4 text-sm text-gray-600"><span class="md:hidden font-medium text-gray-500">Planilha e grupo: </span>{b}</div><div class="px-5 pb-4 pt-1 md:py-4 text-sm text-gray-800 flex gap-2"><i data-lucide="check" class="w-4 h-4 text-emerald-600 shrink-0 mt-0.5"></i><span><span class="md:hidden font-medium text-emerald-700">Convivus: </span>{c}</span></div></div>' for a,b,c in CMP)
COMPARE=f'''<section class="mt-24"><div class="max-w-3xl mb-8 rv">{pill('scale','Comparativo')}<h2 class="font-serif text-3xl lg:text-4xl font-medium leading-tight">Planilha e grupo de mensagens <span class="italic font-light text-emerald-700">ou Convivus?</span></h2></div>
<div class="rounded-3xl bg-white border border-gray-100 shadow-lg overflow-hidden rv"><div class="hidden md:grid grid-cols-[1fr_1.2fr_1.6fr] bg-stone-100 text-xs font-semibold uppercase tracking-widest text-gray-600"><div class="p-4"></div><div class="p-4">Planilha e grupo de mensagens</div><div class="p-4 text-emerald-700">Convivus</div></div>{cmp_rows}</div></section>'''
FAQ_G=f'''<section id="perguntas" class="mt-24 scroll-mt-24"><div class="max-w-3xl mb-8 rv">{pill('circle-help','Perguntas frequentes')}<h2 class="font-serif text-3xl lg:text-4xl font-medium leading-tight">Antes de <span class="italic font-light text-emerald-700">contratar</span></h2></div>{faq(FAQ_GESTAO)}</section>'''
ges+=COMPARE+PRICING+FAQ_G+cta('Quer ver o portal funcionando?','Agende uma demonstração e veja o Convivus na prática.','Agendar demonstração',walink('Olá! Vi o Convivus no site e quero agendar uma demonstração.'))
page('gestao.html','Convivus | CondoFluxo','gestao.html',ges,True,
     desc='Convivus: portal web para síndicos e moradores, com manutenção ligada às normas ABNT, controle de PPCI e AVCB, documentos com auditoria e avisos. De R$ 99 a R$ 119 por condomínio ao mês, sem fidelidade.',
     wamsg='Olá! Vi o Convivus no site e quero agendar uma demonstração.',
     ld=[{"@type":"SoftwareApplication","name":"Convivus","applicationCategory":"BusinessApplication","operatingSystem":"Web","url":SITE+"/gestao","description":"Portal web para síndicos e moradores com manutenção ligada às normas ABNT, controle de PPCI e AVCB, documentos com auditoria, avisos e chamados.","offers":{"@type":"AggregateOffer","priceCurrency":"BRL","lowPrice":"99","highPrice":"119","offerCount":"3"},"publisher":{"@type":"Organization","name":"CondoFluxo"}},faq_ld(FAQ_GESTAO)])

# ================= COMUNICAÇÃO =================
com=head('palette','CondoFluxo Comunicação','Clara e profissional,','para todo o condomínio','Produzimos os materiais que substituem o grupo de WhatsApp e os papéis soltos na portaria. Serviço sob demanda, feito com a identidade do seu condomínio.')
c3=''.join(small(i,b,t,a,c,d) for i,b,t,a,c,d in [
('book-open','bg-emerald-100','text-emerald-600','Manual de','Convivência','Regras do condomínio explicadas de forma simples, com a identidade visual do seu prédio.'),
('layout-template','bg-amber-100','text-amber-600','Comunicados','visuais','Modelos padronizados para os avisos que se repetem, fáceis de ler no elevador e no celular.'),
('globe','bg-blue-100','text-blue-600','Sites','informativos','Uma página para os moradores encontrarem regras, contatos e documentos num só endereço.')])
com+='''<section class="relative rounded-3xl overflow-hidden shadow-2xl min-h-[300px] lg:min-h-[440px] mb-4 rv"><img src="assets/morador-tablet.jpg" alt="Morador lendo comunicados do condomínio no tablet" loading="lazy" class="absolute inset-0 w-full h-full object-cover object-center"><div class="absolute inset-x-0 bottom-0 p-6 lg:p-8 bg-gradient-to-t from-black/70 to-transparent text-white"><p class="font-serif text-2xl">Informação que o morador realmente lê</p></div></section>'''
com+=f'<section class="grid gap-4 md:grid-cols-3">{c3}</section>'
com+='''<section class="mt-16 rounded-3xl bg-gradient-to-br from-teal-700 to-emerald-900 text-white p-8 lg:p-12 shadow-2xl rv grid gap-6 lg:grid-cols-2 items-center"><h2 class="font-serif text-2xl lg:text-4xl font-medium leading-tight">Mais informação para o morador. <span class="italic font-light text-emerald-200">Mais controle para a gestão.</span></h2><p class="text-emerald-50/90 leading-relaxed">Quando o aviso é claro e fica registrado, o grupo de mensagens deixa de ser o único lugar onde as coisas acontecem. Quer o controle completo? O portal Convivus faz esse registro com confirmação de leitura.</p></section>'''
com+=cta('Precisa de um material para o seu condomínio?','Descreva o que precisa e retornamos com a proposta.','Pedir orçamento')
page('comunicacao.html','Comunicação | CondoFluxo','comunicacao.html',com,True,
     desc='Manual de Convivência, comunicados visuais e sites informativos para condomínios, com a identidade visual do seu prédio. Serviço sob demanda.',
     wamsg='Olá! Quero um orçamento de materiais de comunicação para o meu condomínio.')

# ================= SOBRE =================
sob=head('users','Sobre o Convivus','Nascemos da rotina','de quem vive em condomínio','O Convivus surgiu da experiência com falhas de comunicação, manutenções sem acompanhamento e documentos sem controle em condomínios.')
sob+='''<section class="mb-16 grid gap-8 lg:grid-cols-5 rv"><h2 class="lg:col-span-2 font-serif text-3xl lg:text-4xl font-medium leading-tight">Por que a CondoFluxo existe</h2><div class="lg:col-span-3 grid gap-4 text-lg text-gray-700 leading-relaxed">
<p>Quem administra um condomínio precisa fazer duas coisas andarem juntas: manter os moradores bem informados e garantir que o condomínio esteja em dia com normas, manutenções e obrigações legais.</p>
<p>O mercado oferece ferramentas para finanças, portaria e comunicação, mas na prática a informação fica espalhada e a gestão das obrigações depende de planilhas, papéis e grupos de mensagens.</p>
<p>O CondoFluxo nasce dessa lacuna. A ideia vem da experiência de mais de 15 anos de Ana Fernandes na construção civil e na administração de condomínios, onde se repetiam falhas de comunicação, manutenções sem acompanhamento, PPCI e licenças sem controle central e informações importantes sem histórico ou comprovação.</p>
<p>Por isso o CondoFluxo conecta comunicação, manutenção e conformidade em um só fluxo: moradores sabem o que precisam, e a gestão tem clareza do que fazer, quando fazer e como comprovar.</p>
<p>Daí nasce o Convivus, o portal que reúne o que o morador precisa saber e o que o condomínio precisa controlar.</p>
<p class="font-serif text-2xl text-emerald-800 pt-2">Mais informação para o morador. Mais controle para a gestão. Mais segurança para o condomínio.</p></div></section>
'''
sob+=f'''<section class="grid gap-4 lg:grid-cols-5">
 <div class="lg:col-span-2 rounded-3xl bg-white border border-gray-100 shadow-lg p-8 flex flex-col items-start gap-4 rv"><img src="assets/ana-fernandes.jpg" alt="Ana Fernandes, fundadora do Convivus" loading="lazy" class="w-full aspect-[4/5] rounded-2xl object-cover object-top"><div><h2 class="font-serif text-2xl font-medium">Ana Fernandes</h2><p class="text-sm text-emerald-700 font-medium">Fundadora do Convivus</p></div><p class="text-sm text-gray-600 leading-relaxed">Com mais de 15 anos de experiência na construção civil, atuando na gestão da qualidade, processos de entrega e relacionamento com síndicos, fornecedores e clientes. Sua trajetória também inclui sólida experiência nas áreas administrativa e fiscal de condomínios, unindo conhecimento técnico, visão de gestão e foco em resultados.</p></div>
 <div class="lg:col-span-3 grid gap-4">
  {small('eye','bg-emerald-100','text-emerald-600','Clareza antes da','tecnologia','A ferramenta serve para o morador entender o que está acontecendo, não o contrário.')}
  {small('shield-check','bg-amber-100','text-amber-600','Conformidade na','gestão','Manutenção e licenças fazem parte do dia a dia do síndico, e não de um extra.')}
  {small('workflow','bg-blue-100','text-blue-600','Um fluxo','único','Morador, síndico e condomínio no mesmo caminho, com registro de ponta a ponta.')}
 </div></section>
<section class="mt-16 relative rounded-3xl overflow-hidden shadow-2xl min-h-[300px] lg:min-h-[420px] rv"><img src="assets/fachada-entrada.jpg" alt="Entrada de um edifício residencial com jardim e marquise verde" loading="lazy" class="absolute inset-0 w-full h-full object-cover"><div class="absolute inset-x-0 bottom-0 p-6 lg:p-8 bg-gradient-to-t from-black/70 to-transparent text-white"><p class="font-serif text-2xl">Sob o mesmo teto</p></div></section>
<section class="mt-4 rounded-3xl bg-white border border-gray-100 shadow-lg p-8 rv grid gap-4 md:grid-cols-2 text-sm text-gray-700"><div><p class="font-semibold mb-1">O nome</p><p class="text-gray-600">Convivus vem do latim convivere, viver junto.</p></div><div><p class="font-semibold mb-1">Contratação</p><p class="text-gray-600">O serviço pode ser contratado por CNPJ ou por CPF.</p></div></section>'''+cta('Vamos conversar?','Conte como é o seu condomínio.','Falar conosco')
page('sobre.html','Sobre o Convivus | CondoFluxo','sobre.html',sob,True,
     desc='A história do Convivus e da CondoFluxo e a experiência de Ana Fernandes em construção civil e na administração de condomínios.')

# ================= CONTATO =================
ct=head('mail','Contato','Conte como é','o seu condomínio','Respondemos por WhatsApp, telefone ou e-mail. Preencha abaixo e clique em Enviar: abrimos o WhatsApp e o e-mail com a mensagem pronta.')
ct+='''<script src="config.js"></script><section class="grid gap-4 lg:grid-cols-5">
 <div class="lg:col-span-2 rounded-3xl bg-gradient-to-br from-emerald-800 to-emerald-900 text-white p-8 shadow-2xl flex flex-col gap-5 rv">
  <div class="flex gap-4 items-start"><span class="w-10 h-10 rounded-full bg-white/15 flex items-center justify-center shrink-0">@@WA@@</span><div class="min-w-0"><p class="text-xs uppercase tracking-widest text-emerald-200 mb-1">WhatsApp</p><p class="font-medium">+55 51 99611-7922</p><div class="mt-2 flex flex-wrap gap-2"><a href="@@WALINK@@" target="_blank" rel="noopener" class="text-xs font-semibold bg-white text-emerald-800 rounded-full px-3 py-1 hover:bg-emerald-50">Abrir conversa</a><button type="button" data-copy="+55 51 99611-7922" class="text-xs font-semibold border border-white/40 rounded-full px-3 py-1 hover:bg-white/10">Copiar</button></div></div></div>
  <div class="flex gap-4 items-start"><span class="w-10 h-10 rounded-full bg-white/15 flex items-center justify-center shrink-0"><i data-lucide="mail" class="w-5 h-5 text-white"></i></span><div class="min-w-0"><p class="text-xs uppercase tracking-widest text-emerald-200 mb-1">E-mail</p><p class="font-medium break-all">condofluxo@condofluxo.com.br</p><button type="button" data-copy="condofluxo@condofluxo.com.br" class="mt-2 text-xs font-semibold border border-white/40 rounded-full px-3 py-1 hover:bg-white/10">Copiar</button></div></div>
  <div class="flex gap-4 items-start"><span class="w-10 h-10 rounded-full bg-white/15 flex items-center justify-center shrink-0">@@IG@@</span><div class="min-w-0"><p class="text-xs uppercase tracking-widest text-emerald-200 mb-1">Instagram</p><a href="@@IGLINK@@" target="_blank" rel="noopener" class="font-medium underline">@condofluxo</a></div></div>
  <div class="flex gap-4 items-start"><span class="w-10 h-10 rounded-full bg-white/15 flex items-center justify-center shrink-0"><i data-lucide="globe" class="w-5 h-5 text-white"></i></span><div class="min-w-0"><p class="text-xs uppercase tracking-widest text-emerald-200 mb-1">Site do portal</p><a href="https://www.condofluxo.com.br/gestao" target="_blank" rel="noopener" class="font-medium underline break-all">www.condofluxo.com.br/gestao</a></div></div></div>
 <div class="lg:col-span-3 rounded-3xl bg-white border border-gray-100 shadow-lg p-8 rv d2">
  <form id="msg-form" class="grid gap-4 sm:grid-cols-2" novalidate>
   <div><label class="lbl" for="f-nome">Seu nome</label><input class="fld" id="f-nome" type="text" autocomplete="name"></div>
   <div><label class="lbl" for="f-papel">Você é</label><select class="fld" id="f-papel"><option>síndico</option><option>síndico profissional</option><option>da administradora</option><option>da construtora ou incorporadora</option><option>morador</option><option>interessado no serviço</option></select></div>
   <div><label class="lbl" for="f-cond">Condomínio</label><input class="fld" id="f-cond" type="text"></div>
   <div><label class="lbl" for="f-cid">Cidade</label><input class="fld" id="f-cid" type="text" value="Porto Alegre"></div>
   <div><label class="lbl" for="f-qtd">Quantos condomínios</label><select class="fld" id="f-qtd"><option>1 condomínio</option><option>2 a 3 condomínios</option><option>4 a 7 condomínios</option><option>8 ou mais condomínios</option></select></div>
   <div><label class="lbl" for="f-int">Interesse</label><select class="fld" id="f-int"><option>Agendar demonstração do Convivus</option><option>Convivus (portal de gestão)</option><option>Materiais de comunicação</option><option>Convivus e comunicação, os dois</option><option>Outro assunto</option></select></div>
   <div class="sm:col-span-2"><label class="lbl" for="f-ret">Seu e-mail ou WhatsApp para retorno</label><input class="fld" id="f-ret" type="text" autocomplete="email" placeholder="voce@exemplo.com.br ou (51) 90000-0000"></div>
   <div style="position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden" aria-hidden="true"><label for="f-hp">Não preencha este campo</label><input id="f-hp" type="text" tabindex="-1" autocomplete="off"></div>
   <div class="sm:col-span-2"><label class="lbl" for="f-msg">O que você precisa</label><textarea class="fld" id="f-msg" rows="4">Quero conhecer e entender como funciona a contratação.</textarea></div>
   <div class="sm:col-span-2 flex flex-wrap items-center gap-4"><button type="submit" class="bg-emerald-600 text-white px-8 py-3 rounded-full font-medium hover:bg-emerald-700 transition-colors">Enviar</button><p id="send-hint" class="text-xs text-gray-500 max-w-sm">Ao enviar, abrimos o WhatsApp e o seu programa de e-mail com a mensagem pronta.</p></div>
   <p id="send-status" class="sm:col-span-2 text-sm text-gray-700" role="status"></p>
  </form>
  <div id="out-wrap" class="mt-2 flex flex-wrap items-center gap-x-5 gap-y-2 text-sm" hidden><span class="text-gray-500">Não abriu?</span><a id="wa-send" href="#" target="_blank" rel="noopener" class="font-semibold text-emerald-700 underline">Enviar pelo WhatsApp</a><a id="mail-link" href="#" class="font-semibold text-emerald-700 underline">Enviar por e-mail</a></div>
 </div></section>'''
ct=ct.replace('@@WA@@',wa('w-5 h-5 text-white')).replace('@@IG@@',ig('w-5 h-5 text-white')).replace('@@WALINK@@',WA_LINK).replace('@@IGLINK@@',IG_LINK)
page('contato.html','Contato | CondoFluxo','contato.html',ct,True,
     desc='Fale com a CondoFluxo pelo WhatsApp, e-mail ou Instagram, ou monte a sua mensagem e peça uma demonstração do Convivus.')

# ================= GUIA: MANUTENÇÃO PREDIAL NORMATIVA =================
GFAQ=[('O que é a NBR 5674?','É a norma da ABNT sobre manutenção de edificações. Ela trata a manutenção como um sistema organizado, com programa de atividades e periodicidade, responsáveis definidos, previsão de recursos e registro de tudo o que foi feito.'),
('O que é a NBR 15575?','É a norma de desempenho de edificações habitacionais. Ela define a vida útil de projeto dos sistemas do edifício e condiciona esse desempenho ao cumprimento do manual de uso, operação e manutenção.'),
('O síndico é responsável pela manutenção predial?','A gestão do condomínio responde por organizar a manutenção e por conseguir comprovar que ela foi feita. A execução pode ficar com o zelador, uma empresa contratada ou um responsável técnico. Em caso de dúvida sobre responsabilidades, consulte um advogado.'),
('Com que frequência a manutenção deve ser feita?','Depende do sistema e do manual da edificação. O plano de manutenção define a periodicidade de cada item. Alguns exemplos: limpeza semestral dos reservatórios, manutenção mensal dos elevadores e verificação anual do SPDA.'),
('O que precisa ficar registrado?','A data da execução, a evidência (laudo, relatório ou foto), o responsável e a data da próxima manutenção. É esse histórico que comprova o cumprimento do plano.')]
g=f'''<div class="max-w-4xl mb-14 rv">{pill('book-open','Guia para síndicos')}<h1 class="text-3xl sm:text-4xl lg:text-5xl leading-[1.08] font-medium tracking-tight font-serif">Manutenção predial normativa:<br><span class="font-light italic text-emerald-700">o que a NBR 5674 e a NBR 15575 exigem do seu condomínio</span></h1><p class="text-lg text-gray-600 mt-6 leading-relaxed max-w-3xl">Manutenção predial é obrigação com norma técnica, periodicidade definida e necessidade de comprovação. A execução cabe à gestão do condomínio, e este guia mostra como organizar prazos, registros e provas.</p></div>

<section><div class="max-w-3xl mb-8 rv"><h2 class="font-serif text-3xl lg:text-4xl font-medium">As duas <span class="italic font-light text-emerald-700">normas</span></h2></div>
<div class="grid gap-4 md:grid-cols-3">
{small('clipboard-list','bg-emerald-100','text-emerald-600','NBR','5674','Manutenção de edificações. Exige um sistema organizado: programa de atividades com periodicidade, previsão orçamentária, responsáveis definidos e registro documentado. Manutenção corretiva improvisada não atende à norma.')}
{small('hourglass','bg-amber-100','text-amber-600','NBR','15575','Desempenho de edificações habitacionais. Define a vida útil de projeto dos sistemas do edifício e condiciona esse desempenho ao cumprimento do manual de uso, operação e manutenção.')}
{small('search-check','bg-blue-100','text-blue-600','NBR','16747','Referência para a inspeção predial, que avalia o estado da edificação e classifica as anomalias por grau de risco.')}
</div></section>

<section class="mt-24"><div class="max-w-3xl mb-8 rv"><h2 class="font-serif text-3xl lg:text-4xl font-medium">Como montar o plano <span class="italic font-light text-emerald-700">em 4 passos</span></h2></div>
<ol class="grid gap-4 md:grid-cols-2">
<li class="rounded-3xl bg-white border border-gray-100 shadow-lg p-6 flex gap-4 lift rv"><span class="font-serif text-3xl text-emerald-600 leading-none">1</span><div><h3 class="font-semibold mb-1">Levantar os sistemas</h3><p class="text-sm text-gray-600 leading-relaxed">Use o manual entregue pela construtora. Se ele não existir, faça o inventário dos sistemas do prédio e dos fornecedores de cada um.</p></div></li>
<li class="rounded-3xl bg-white border border-gray-100 shadow-lg p-6 flex gap-4 lift rv d2"><span class="font-serif text-3xl text-emerald-600 leading-none">2</span><div><h3 class="font-semibold mb-1">Definir periodicidade e responsável</h3><p class="text-sm text-gray-600 leading-relaxed">Cada item precisa de uma frequência e de um responsável, que pode ser o zelador, uma empresa contratada ou um responsável técnico.</p></div></li>
<li class="rounded-3xl bg-white border border-gray-100 shadow-lg p-6 flex gap-4 lift rv"><span class="font-serif text-3xl text-emerald-600 leading-none">3</span><div><h3 class="font-semibold mb-1">Controlar os vencimentos legais</h3><p class="text-sm text-gray-600 leading-relaxed">PPCI, AVCB, laudos, seguro obrigatório e inspeção predial têm prazo próprio. Acompanhe todos com aviso antecipado.</p></div></li>
<li class="rounded-3xl bg-white border border-gray-100 shadow-lg p-6 flex gap-4 lift rv d2"><span class="font-serif text-3xl text-emerald-600 leading-none">4</span><div><h3 class="font-semibold mb-1">Registrar e guardar a prova</h3><p class="text-sm text-gray-600 leading-relaxed">Para cada execução, guarde a data, a evidência (laudo, relatório ou foto) e o responsável.</p></div></li>
</ol></section>

<section class="mt-24"><div class="max-w-3xl mb-8 rv"><h2 class="font-serif text-3xl lg:text-4xl font-medium">Checklist <span class="italic font-light text-emerald-700">de sistemas</span></h2></div>
<div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
{small('flame','bg-rose-100','text-rose-600','Combate a','incêndio','Inspeções periódicas de extintores, hidrantes, alarme e iluminação de emergência. Controle da renovação de PPCI e AVCB.','<a href="ppci-avcb-guia.html" class="mt-auto inline-flex items-center gap-2 text-sm font-semibold text-emerald-700 hover:gap-3 transition-all">Guia de PPCI e AVCB <i data-lucide="arrow-right" class="w-4 h-4"></i></a>')}
{small('building','bg-stone-200','text-stone-600','Estrutura e','fachada','Inspeções visuais periódicas e inspeção predial conforme a NBR 16747.')}
{small('droplets','bg-blue-100','text-blue-600','Instalações','hidráulicas','Limpeza semestral dos reservatórios, verificação de bombas e prumadas e prevenção de vazamentos.')}
{small('zap','bg-amber-100','text-amber-600','Elétrica e','SPDA','Inspeção de quadros e medições. Verificação anual do sistema de proteção contra descargas atmosféricas.')}
{small('arrow-up-down','bg-violet-100','text-violet-600','','Elevadores','Manutenção mensal por empresa habilitada e relatório anual arquivado.')}
{small('umbrella','bg-teal-100','text-teal-600','Impermeabilização e','cobertura','Verificação de lajes, calhas e telhados, com atenção ao fim da vida útil prevista.')}
</div></section>

<section class="mt-24"><div class="max-w-3xl mb-8 rv"><h2 class="font-serif text-3xl lg:text-4xl font-medium">Perguntas <span class="italic font-light text-emerald-700">frequentes</span></h2></div>
{faq(GFAQ)}</section>

<section class="mt-24 rounded-3xl bg-gradient-to-br from-emerald-900 to-teal-800 text-white p-8 lg:p-12 shadow-2xl rv grid gap-6 lg:grid-cols-2 items-center">
<div><img src="assets/logo-convivus.png" alt="Convivus" class="h-10 w-auto bg-white rounded-xl p-2 mb-5"><h2 class="font-serif text-2xl lg:text-3xl font-medium leading-tight">Cada rotina ligada à norma, <span class="italic font-light text-emerald-200">com prazo e prova</span></h2></div>
<div class="grid gap-5"><p class="text-emerald-50/90 leading-relaxed">No Convivus, cada item de manutenção vem vinculado à norma, com periodicidade, responsável, aviso de vencimento e histórico de execução.</p><div class="flex flex-wrap gap-3"><a href="gestao.html" class="bg-white text-emerald-800 px-6 py-3 rounded-full font-semibold hover:bg-emerald-50 transition-colors">Ver o Convivus</a><a href="contato.html" class="border border-white/50 px-6 py-3 rounded-full font-semibold hover:bg-white/10 transition-colors">Fale conosco</a></div></div>
</section>
<p class="mt-8 text-xs text-gray-500 max-w-3xl rv">Este guia é informativo e não substitui a orientação de um profissional habilitado nem de um advogado.</p>
'''
page('manutencao-predial-normativa.html','Manutenção predial normativa | CondoFluxo','',g,True,
     desc='O que a NBR 5674 e a NBR 15575 exigem do condomínio: como montar o plano de manutenção, controlar vencimentos e registrar a prova.',
     ld=[faq_ld(GFAQ)])

# ================= GUIA: PPCI E AVCB =================
PFAQ=[('PPCI, APPCI e AVCB são a mesma coisa?','Não. PPCI é o plano com as medidas de segurança contra incêndio da edificação. APPCI é o alvará emitido no Rio Grande do Sul a partir desse plano. AVCB é o nome da licença em estados como São Paulo. O nome do documento, o prazo e as exigências mudam de estado para estado.'),
('Quem responde pela licença de incêndio no condomínio?','A gestão do condomínio organiza a regularização e a renovação, e a execução técnica fica com profissionais habilitados. Em caso de dúvida sobre responsabilidades, consulte um advogado.'),
('Quando devo renovar a licença?','Antes do fim da validade indicada no documento. O prazo de validade e a antecedência para pedir a renovação variam por estado e por tipo de edificação, então confirme com o Corpo de Bombeiros do seu estado.'),
('O que fazer se a licença venceu?','Procure o Corpo de Bombeiros do seu estado para saber como regularizar e, se necessário, um profissional habilitado. Consulte um advogado sobre as consequências para o condomínio.')]
p=f'''<div class="max-w-4xl mb-14 rv">{pill('flame','Guia para síndicos')}<h1 class="text-3xl sm:text-4xl lg:text-5xl leading-[1.08] font-medium tracking-tight font-serif">PPCI e AVCB:<br><span class="font-light italic text-emerald-700">o que o síndico precisa acompanhar</span></h1><p class="text-lg text-gray-600 mt-6 leading-relaxed max-w-3xl">A licença de incêndio do condomínio tem nome e regras que mudam de estado para estado. Este guia mostra o que acompanhar e como organizar a renovação para o prazo não vencer sem ninguém perceber.</p></div>

<section><div class="max-w-3xl mb-8 rv"><h2 class="font-serif text-3xl lg:text-4xl font-medium">Os três <span class="italic font-light text-emerald-700">nomes</span></h2></div>
<div class="grid gap-4 md:grid-cols-3">
{small('file-text','bg-emerald-100','text-emerald-600','','PPCI','Plano de Prevenção e Proteção Contra Incêndio. Reúne as medidas de segurança da edificação, como extintores, hidrantes, alarme, iluminação de emergência e saídas sinalizadas.')}
{small('badge-check','bg-amber-100','text-amber-600','','APPCI','Alvará de PPCI, a licença emitida no Rio Grande do Sul pelo Corpo de Bombeiros (CBMRS) para a edificação regularizada. Tem validade e precisa ser renovado.')}
{small('stamp','bg-blue-100','text-blue-600','','AVCB','Auto de Vistoria do Corpo de Bombeiros, nome da licença em estados como São Paulo. Em cada estado, o documento, o prazo e as exigências têm regras próprias.')}
</div></section>

<section class="mt-24"><div class="max-w-3xl mb-8 rv"><h2 class="font-serif text-3xl lg:text-4xl font-medium">O que <span class="italic font-light text-emerald-700">acompanhar</span></h2><p class="text-gray-600 mt-3">Os sistemas exigidos dependem do projeto aprovado para o seu prédio. Esta lista mostra o que costuma entrar no controle.</p></div>
<div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
{small('calendar-clock','bg-rose-100','text-rose-600','Validade da','licença','Confira a data no documento e programe a renovação com antecedência.')}
{small('flame-kindling','bg-amber-100','text-amber-600','','Extintores','Mantenha os equipamentos dentro do prazo e nos locais indicados no projeto.')}
{small('droplets','bg-blue-100','text-blue-600','Hidrantes e','mangueiras','Verifique o estado dos equipamentos e o acesso a eles.')}
{small('bell-ring','bg-violet-100','text-violet-600','Alarme e','detecção','Acompanhe o funcionamento e os registros de manutenção do sistema.')}
{small('lightbulb','bg-yellow-100','text-yellow-600','Iluminação de','emergência','Teste e mantenha os pontos de luz previstos no projeto.')}
{small('door-open','bg-teal-100','text-teal-600','Saídas e','sinalização','Rotas desobstruídas, portas e sinalização de saída conforme o projeto aprovado.')}
</div></section>

<section class="mt-24"><div class="max-w-3xl mb-8 rv"><h2 class="font-serif text-3xl lg:text-4xl font-medium">Como organizar <span class="italic font-light text-emerald-700">em 4 passos</span></h2></div>
<ol class="grid gap-4 md:grid-cols-2">
<li class="rounded-3xl bg-white border border-gray-100 shadow-lg p-6 flex gap-4 lift rv"><span class="font-serif text-3xl text-emerald-600 leading-none">1</span><div><h3 class="font-semibold mb-1">Localizar a licença atual</h3><p class="text-sm text-gray-600 leading-relaxed">Encontre o documento vigente e anote a data de validade. Se ninguém sabe onde está, esse é o primeiro problema a resolver.</p></div></li>
<li class="rounded-3xl bg-white border border-gray-100 shadow-lg p-6 flex gap-4 lift rv d2"><span class="font-serif text-3xl text-emerald-600 leading-none">2</span><div><h3 class="font-semibold mb-1">Conferir o projeto aprovado</h3><p class="text-sm text-gray-600 leading-relaxed">Veja quais sistemas o prédio precisa manter. É o projeto aprovado que define a lista, e não um modelo genérico.</p></div></li>
<li class="rounded-3xl bg-white border border-gray-100 shadow-lg p-6 flex gap-4 lift rv"><span class="font-serif text-3xl text-emerald-600 leading-none">3</span><div><h3 class="font-semibold mb-1">Programar manutenção e laudos</h3><p class="text-sm text-gray-600 leading-relaxed">Para cada sistema, defina responsável, periodicidade e data da próxima execução, com a evidência guardada.</p></div></li>
<li class="rounded-3xl bg-white border border-gray-100 shadow-lg p-6 flex gap-4 lift rv d2"><span class="font-serif text-3xl text-emerald-600 leading-none">4</span><div><h3 class="font-semibold mb-1">Antecipar a renovação</h3><p class="text-sm text-gray-600 leading-relaxed">Confirme com o Corpo de Bombeiros do seu estado o prazo e os documentos exigidos, e comece antes do vencimento.</p></div></li>
</ol></section>

<section class="mt-24"><div class="max-w-3xl mb-8 rv"><h2 class="font-serif text-3xl lg:text-4xl font-medium">Perguntas <span class="italic font-light text-emerald-700">frequentes</span></h2></div>
{faq(PFAQ)}</section>

<section class="mt-24 rounded-3xl bg-gradient-to-br from-emerald-900 to-teal-800 text-white p-8 lg:p-12 shadow-2xl rv grid gap-6 lg:grid-cols-2 items-center">
<div><img src="assets/logo-convivus.png" alt="Convivus" class="h-10 w-auto bg-white rounded-xl p-2 mb-5"><h2 class="font-serif text-2xl lg:text-3xl font-medium leading-tight">Licença de incêndio <span class="italic font-light text-emerald-200">com aviso antes de vencer</span></h2></div>
<div class="grid gap-5"><p class="text-emerald-50/90 leading-relaxed">O Convivus controla APPCI e AVCB por estado, com aviso antes da renovação. Já vem preenchido para o Rio Grande do Sul.</p><div class="flex flex-wrap gap-3"><a href="gestao.html" class="bg-white text-emerald-800 px-6 py-3 rounded-full font-semibold hover:bg-emerald-50 transition-colors">Ver o Convivus</a><a href="gestao.html#valores" class="border border-white/50 px-6 py-3 rounded-full font-semibold hover:bg-white/10 transition-colors">Ver valores</a></div></div>
</section>
<p class="mt-8 text-xs text-gray-500 max-w-3xl rv">Este guia é informativo e não substitui a orientação do Corpo de Bombeiros, de um profissional habilitado nem de um advogado.</p>
'''
page('ppci-avcb-guia.html','PPCI e AVCB: guia para síndicos | CondoFluxo','',p,True,
     desc='Guia para síndicos sobre PPCI, APPCI e AVCB: o que significa cada documento, o que acompanhar e como organizar a renovação da licença de incêndio.',
     ld=[faq_ld(PFAQ)])

# ================= BLOG =================
sys.path.insert(0,HERE)
from blog_posts import POSTS
MESES=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
def data_br(iso):
    a,m,d=iso.split('-'); return f'{int(d)} de {MESES[int(m)-1]} de {a}'
POSTS=sorted(POSTS,key=lambda x:x['date'],reverse=True)
def purl(po): return f"blog-{po['slug']}.html"

def card_post(po):
    cover=f"""<div class="-m-6 mb-0 overflow-hidden rounded-t-3xl"><img src="assets/{po['image']}" alt="{po.get('image_alt','')}" width="1600" height="893" loading="lazy" class="w-full h-auto block group-hover:scale-105 transition-transform duration-500"></div>""" if po.get('image') else f"""<div class="w-10 h-10 bg-emerald-100 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform duration-300"><i data-lucide="{po['icon']}" class="w-5 h-5 text-emerald-600"></i></div>"""
    return f"""<a href="{purl(po)}" class="rounded-3xl bg-white border border-gray-100 p-6 flex flex-col gap-4 shadow-lg hover:shadow-xl transition-shadow duration-300 group lift rv overflow-hidden">{cover}<div class="flex flex-wrap items-center gap-x-3 gap-y-1 text-xs font-semibold text-gray-500"><span class="text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-full">{po['cat']}</span><time datetime="{po['date']}">{data_br(po['date'])}</time><span>{po['read']} min de leitura</span></div><h2 class="font-serif text-xl font-medium leading-tight">{po['title']}</h2><p class="text-sm text-gray-600 leading-relaxed">{po['desc']}</p><span class="mt-auto inline-flex items-center gap-2 text-sm font-semibold text-emerald-700 group-hover:gap-3 transition-all">Ler artigo <i data-lucide="arrow-right" class="w-4 h-4"></i></span></a>"""

if POSTS:
    lista='<div class="grid gap-4 md:grid-cols-2 lg:grid-cols-3">'+''.join(card_post(po) for po in POSTS)+'</div>'
else:
    lista='<p class="text-gray-600">Os primeiros artigos chegam em breve.</p>'
bl=head('newspaper','Blog','Condomínio sem improviso:','guias e boas práticas','Artigos curtos para síndicos, conselheiros e administradoras sobre manutenção, normas, documentos e convivência.')+lista+cta('Quer o condomínio com prazo e prova?','O Convivus organiza manutenção, licenças e documentos num só lugar.','Falar conosco')
page('blog.html','Blog | CondoFluxo','blog.html',bl,True,
     desc='Artigos para síndicos, conselheiros e administradoras: manutenção predial, normas ABNT, PPCI e AVCB, documentos e convivência em condomínios.',
     ld=[{"@type":"Blog","name":"Blog CondoFluxo","url":SITE+"/blog","inLanguage":"pt-BR","publisher":{"@type":"Organization","name":"CondoFluxo","url":SITE}}])

for po in POSTS:
    fq=po.get('faq') or []
    fq_html=f"""<section class="mt-16 max-w-3xl"><div class="mb-6 rv"><h2 class="font-serif text-2xl lg:text-3xl font-medium">Perguntas <span class="italic font-light text-emerald-700">frequentes</span></h2></div>{faq(fq)}</section>""" if fq else ''
    cover_html=f"""<figure class="max-w-4xl mb-12 rv"><img src="assets/{po['image']}" alt="{po.get('image_alt','')}" width="1600" height="893" class="w-full h-auto rounded-3xl shadow-xl border border-gray-100"></figure>""" if po.get('image') else ''
    outros=[x for x in POSTS if x['slug']!=po['slug']][:3]
    outros_html=('<section class="mt-20"><div class="max-w-3xl mb-6 rv"><h2 class="font-serif text-2xl lg:text-3xl font-medium">Continue <span class="italic font-light text-emerald-700">lendo</span></h2></div><div class="grid gap-4 md:grid-cols-2 lg:grid-cols-3">'+''.join(card_post(x) for x in outros)+'</div></section>') if outros else ''
    art=f"""<a href="blog.html" class="inline-flex items-center gap-2 text-sm font-semibold text-emerald-700 hover:gap-3 transition-all mb-8 rv"><i data-lucide="arrow-left" class="w-4 h-4"></i>Todos os artigos</a>
<header class="max-w-3xl mb-10 rv">{pill(po['icon'],po['cat'])}<h1 class="text-3xl sm:text-4xl lg:text-5xl leading-[1.1] font-medium tracking-tight font-serif">{po['title']}</h1><p class="text-lg text-gray-600 mt-5 leading-relaxed">{po['desc']}</p><p class="mt-5 text-sm text-gray-500 flex flex-wrap items-center gap-x-4 gap-y-1"><span class="inline-flex items-center gap-1.5"><i data-lucide="calendar" class="w-4 h-4 text-emerald-600"></i><time datetime="{po['date']}">{data_br(po['date'])}</time></span><span class="inline-flex items-center gap-1.5"><i data-lucide="clock" class="w-4 h-4 text-emerald-600"></i>{po['read']} min de leitura</span><span class="inline-flex items-center gap-1.5"><i data-lucide="user" class="w-4 h-4 text-emerald-600"></i>Equipe CondoFluxo</span></p></header>
{cover_html}<article class="post max-w-3xl rv">{po['body']}</article>
{fq_html}
<section class="mt-20 rounded-3xl bg-gradient-to-br from-emerald-900 to-teal-800 text-white p-8 lg:p-12 shadow-2xl rv grid gap-6 lg:grid-cols-2 items-center">
<div><img src="assets/logo-convivus.png" alt="Convivus" class="h-10 w-auto bg-white rounded-xl p-2 mb-5"><h2 class="font-serif text-2xl lg:text-3xl font-medium leading-tight">Prazo, responsável <span class="italic font-light text-emerald-200">e prova, num só lugar</span></h2></div>
<div class="grid gap-5"><p class="text-emerald-50/90 leading-relaxed">O Convivus reúne manutenção ligada às normas, licenças com aviso de renovação, documentos com histórico e mural com confirmação de leitura.</p><div class="flex flex-wrap gap-3"><a href="gestao.html" class="bg-white text-emerald-800 px-6 py-3 rounded-full font-semibold hover:bg-emerald-50 transition-colors">Ver o Convivus</a><a href="contato.html" class="border border-white/50 px-6 py-3 rounded-full font-semibold hover:bg-white/10 transition-colors">Fale conosco</a></div></div>
</section>
{outros_html}
<p class="mt-8 text-xs text-gray-500 max-w-3xl rv">Este artigo é informativo e não substitui a orientação de um profissional habilitado nem de um advogado.</p>"""
    ld=[{"@type":"BlogPosting","headline":po['title'],"description":po['desc'],"datePublished":po['date'],"dateModified":po.get('updated',po['date']),"inLanguage":"pt-BR","mainEntityOfPage":SITE+"/"+cp(purl(po)),"author":{"@type":"Organization","name":"CondoFluxo"},"publisher":{"@type":"Organization","name":"CondoFluxo","url":SITE,"logo":{"@type":"ImageObject","url":SITE+"/assets/logo-condofluxo.png"}},"image":SITE+"/assets/"+po.get("image_og",po.get("image",""))  if po.get("image") else SITE+"/assets/fachada-verde.jpg"}]
    if fq: ld.append(faq_ld(fq))
    page(purl(po),po['title']+' | CondoFluxo','blog.html',art,True,desc=po['desc'],ld=ld,img=('assets/'+po.get('image_og',po['image'])) if po.get('image') else None)

# ================= PÁGINA 404 =================
# Cloudflare Pages, Netlify e GitHub Pages usam o 404.html da raiz quando o endereço não existe.
# O <base href="/"> garante que links e imagens funcionem mesmo em endereços com subpastas.
NF=f"""<section class="grid gap-10 lg:grid-cols-2 lg:gap-14 items-center">
<div class="rv">{pill('search-x','Erro 404 · Página não encontrada')}<h1 class="text-4xl sm:text-5xl lg:text-6xl leading-[1.1] font-medium tracking-tight font-serif">Nada está no lugar,<br><span class="text-emerald-700">nem esta página</span></h1><p class="text-lg text-gray-600 mt-6 leading-relaxed max-w-xl">O endereço pode ter sido digitado errado ou a página mudou de lugar. Enquanto você volta, repare neste condomínio: sem prazo, sem responsável e sem prova, é assim que a rotina fica.</p>
<div class="mt-8 flex flex-wrap gap-3"><a href="index.html" class="bg-emerald-600 text-white px-7 py-3 rounded-full font-semibold hover:bg-emerald-700 transition-colors">Voltar para o início</a><a href="gestao.html" class="gradient-border inline-block px-7 py-3 rounded-full font-semibold text-emerald-700 hover:shadow-lg transition-all">Conhecer o Convivus</a></div>
<p class="mt-6 text-sm text-gray-500">Ou vá direto para <a href="comunicacao.html" class="text-emerald-700 font-medium hover:underline">Comunicação</a>, <a href="blog.html" class="text-emerald-700 font-medium hover:underline">Blog</a> ou <a href="contato.html" class="text-emerald-700 font-medium hover:underline">Falar conosco</a>.</p></div>
<figure class="rv"><img src="assets/condominio-desorganizado.svg" alt="Ilustração de um condomínio desorganizado: lixeiras transbordando, correspondência espalhada, avisos tortos no mural, extintor vencido, vazamento na parede e fios soltos." width="960" height="640" class="w-full h-auto rounded-3xl shadow-xl border border-gray-100 bg-white"></figure>
</section>"""
page('404.html','Página não encontrada | CondoFluxo','',NF,True,extra_head='<base href="/"><meta name="robots" content="noindex">')

CONFIG_JS='''// Configuração do envio de e-mail do formulário de contato.
// Enquanto estiver em branco, o botão Enviar abre o WhatsApp e o programa de e-mail do visitante.
//
// Opção 1 - Formspree (formspree.io):
//   provider: 'formspree'
//   endpoint: 'https://formspree.io/f/SEU_CODIGO'
// Opção 2 - Web3Forms (web3forms.com):
//   provider: 'web3forms'
//   accessKey: 'SUA_CHAVE_DE_ACESSO'
window.CF_FORM = {
  provider: '',
  endpoint: '',
  accessKey: ''
};
'''
W3KEY=os.environ.get('CF_WEB3_KEY','26e2bc49-3639-4a82-84eb-eab2796f7334').strip()
if W3KEY:
    CONFIG_JS=CONFIG_JS.replace("  provider: '',","  provider: 'web3forms',").replace("  accessKey: ''","  accessKey: '"+W3KEY+"'")
    CONFIG_JS=CONFIG_JS.replace("// Enquanto estiver em branco,","// Envio por e-mail ativo via Web3Forms (a chave de acesso é pública por desenho).\n// Se ficar em branco,")
open(os.path.join(OUT,'config.js'),'w').write(CONFIG_JS)

# ================= ARQUIVOS DE SEO (só no build local) =================
if os.environ.get('CF_FULL')=='1':
    pages=['index.html','gestao.html','comunicacao.html','blog.html','sobre.html','contato.html','manutencao-predial-normativa.html','ppci-avcb-guia.html']+[purl(po) for po in POSTS]
    sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{SITE}/{cp(f)}</loc></url>\n' for f in pages)+'</urlset>\n'
    open(os.path.join(OUT,'sitemap.xml'),'w').write(sm)
    open(os.path.join(OUT,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
    BLOG_LLMS=''.join(f"- [{po['title']}]({SITE}/{cp(purl(po))}): {po['desc']}\n" for po in POSTS).rstrip('\n')
    open(os.path.join(OUT,'llms.txt'),'w').write(f"""# CondoFluxo

> A CondoFluxo reúne duas frentes: o Convivus, portal web de gestão e conformidade para condomínios, e materiais de comunicação para os moradores. Site em português do Brasil.

## Convivus (portal de gestão)
- [Convivus]({SITE}/gestao): manutenção preventiva ligada às normas ABNT (NBR 5674, 15575, 17170, 16747), controle de PPCI/APPCI e AVCB com aviso de renovação, documentos com auditoria, mural com confirmação de leitura, chamados, perfis de acesso por papel. Não é um sistema financeiro.
- Valores públicos, por condomínio ao mês, para até 150 unidades: R$ 119 (até 3 condomínios), R$ 109 (4 a 7), R$ 99 (8 ou mais). Plano anual: pague 11 mensalidades e use 12. Sem fidelidade e sem taxa de saída. Acima de 150 unidades, somam-se R$ 25 por mês a cada bloco de 50, até 400 unidades.

## Comunicação
- [Comunicação]({SITE}/comunicacao): Manual de Convivência, comunicados visuais e sites informativos para condomínios, sob demanda.

## Guias
- [Manutenção predial normativa]({SITE}/manutencao-predial-normativa): NBR 5674 e NBR 15575 para síndicos.
- [PPCI e AVCB]({SITE}/ppci-avcb-guia): o que acompanhar na licença de incêndio.

## Blog
- [Blog]({SITE}/blog): artigos para síndicos sobre manutenção predial, normas, PPCI/AVCB, documentos e convivência.
{BLOG_LLMS}

## Contato
- WhatsApp: +55 51 99611-7922
- E-mail: condofluxo@condofluxo.com.br
- Instagram: {IG_LINK}
""")

print('ok')
