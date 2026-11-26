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
    if(svc&&hint) hint.textContent='Ao enviar, a mensagem segue por e-mail para o Convivus e o WhatsApp abre com o texto pronto.';
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var v=function(id){return (document.getElementById(id).value||'').trim();};
      var st=document.getElementById('send-status');
      if(v('f-hp')) return;
      var nome=v('f-nome'),ret=v('f-ret');
      if(!nome){st.textContent='Informe o seu nome para enviar.';document.getElementById('f-nome').focus();return;}
      if(!ret){st.textContent='Informe um e-mail ou WhatsApp para retorno.';document.getElementById('f-ret').focus();return;}
      var papel=v('f-papel'),cond=v('f-cond'),cid=v('f-cid'),qtd=v('f-qtd'),int=v('f-int'),msg=v('f-msg');
      try{ if(window.cfTrack) cfTrack('generate_lead',{form_name:'contato',interesse:int,quantidade_condominios:qtd}); }catch(x){}
      var t='Olá! Meu nome é '+nome+' e sou '+papel+(cond?' do condomínio '+cond:'')+(cid?', em '+cid:'')+'.\n\nContato para retorno: '+ret+'.'+(qtd?'\n\nQuantidade de condomínios: '+qtd+'.':'')+'\n\nTenho interesse em: '+int+'.\n\n'+msg+'\n\nObrigado!';
      var wa='https://wa.me/5551996117922?text='+encodeURIComponent(t);
      var mail='mailto:convivus@convivus.com.br?subject='+encodeURIComponent('Contato pelo site Convivus')+'&body='+encodeURIComponent(t);
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
      if(svc==='formspree'){url=C.endpoint;body=Object.assign({_subject:'Contato pelo site Convivus'},data);}
      else{url='https://api.web3forms.com/submit';body=Object.assign({access_key:C.accessKey,subject:'Contato pelo site Convivus',from_name:'Site Convivus',message:t},data);}
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
