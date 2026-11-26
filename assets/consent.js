(function(){
  var C=window.CF_GA||{}, ID=String(C.id||'').trim(), KEY='cf_consent_v1';
  var box=document.getElementById('cc'), st=document.getElementById('cc-st'), fab=document.querySelector('.wa-fab');
  // Acesso interno: abrir o site com ?interno=1 marca este navegador (e ?interno=0 desmarca).
  // Navegadores marcados enviam traffic_type=internal ao Analytics, que o filtro "Internal Traffic" exclui.
  var INT=false;
  try{
    var mi=/[?&]interno=([01])(?:&|#|$)/.exec(location.search);
    if(mi){ if(mi[1]==='1') localStorage.setItem('cf_internal','1'); else localStorage.removeItem('cf_internal'); }
    INT=localStorage.getItem('cf_internal')==='1';
  }catch(e){}
  window.cfTrack=function(n,p){ try{ if(ID&&typeof window.gtag==='function'&&!window['ga-disable-'+ID]) window.gtag('event',n,p||{}); }catch(e){} };
  document.addEventListener('click',function(e){
    var a=e.target&&e.target.closest?e.target.closest('a[href*="wa.me/"]'):null;
    if(a) window.cfTrack('whatsapp_click',{link_location:a.classList.contains('wa-fab')?'botao_flutuante':'pagina'});
  },true);
  var wraps=document.querySelectorAll('[data-cc-wrap]');
  if(!box||(!ID&&!C.preview)){ for(var i=0;i<wraps.length;i++) wraps[i].hidden=true; return; }
  function get(){ try{ return localStorage.getItem(KEY); }catch(e){ return null; } }
  function put(v){ try{ localStorage.setItem(KEY,v); }catch(e){} }
  var loaded=false;
  function load(){
    if(!ID) return;
    window['ga-disable-'+ID]=false;
    if(loaded) return; loaded=true;
    window.dataLayer=window.dataLayer||[];
    window.gtag=function(){ window.dataLayer.push(arguments); };
    gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'granted'});
    gtag('js',new Date());
    var cfg={allow_google_signals:false,allow_ad_personalization_signals:false};
    if(INT) cfg.traffic_type='internal';
    gtag('config',ID,cfg);
    var s=document.createElement('script'); s.async=true;
    s.src='https://www.googletagmanager.com/gtag/js?id='+encodeURIComponent(ID);
    document.head.appendChild(s);
  }
  function wipe(){
    if(ID) window['ga-disable-'+ID]=true;
    var parts=location.hostname.split('.'), doms=[''], k;
    for(k=0;k<parts.length-1;k++) doms.push('.'+parts.slice(k).join('.'));
    var list=document.cookie?document.cookie.split(';'):[];
    list.forEach(function(c){
      var n=c.split('=')[0].trim();
      if(n==='_ga'||n.indexOf('_ga_')===0||n==='_gid'||n.indexOf('_gat')===0){
        doms.forEach(function(d){ document.cookie=n+'=; Max-Age=0; path=/'+(d?'; domain='+d:''); });
      }
    });
  }
  function place(){
    if(!fab) return;
    if(box.hidden){ fab.classList.remove('cc-up'); document.documentElement.style.removeProperty('--ccH'); }
    else { document.documentElement.style.setProperty('--ccH',box.offsetHeight+'px'); fab.classList.add('cc-up'); }
  }
  function show(manual){
    var cur=get();
    if(manual&&cur){ st.hidden=false; st.textContent='Sua escolha atual: '+(cur==='granted'?'cookies de medição aceitos.':'cookies de medição recusados.'); }
    else { st.hidden=true; }
    box.hidden=false; place();
    if(manual){ var b=box.querySelector('.cc-ok'); if(b&&b.focus) b.focus(); }
  }
  function choose(v){
    put(v);
    if(v==='granted') load(); else wipe();
    box.hidden=true; place();
  }
  var cur=get();
  if(cur==='granted') load(); else if(cur!=='denied') show(false);
  box.addEventListener('click',function(e){
    var b=e.target.closest?e.target.closest('[data-cc]'):null;
    if(b) choose(b.getAttribute('data-cc'));
  });
  document.addEventListener('click',function(e){
    var t=e.target.closest?e.target.closest('[data-cookie-pref]'):null;
    if(t){ e.preventDefault(); show(true); }
  });
  window.addEventListener('resize',place);
})();
