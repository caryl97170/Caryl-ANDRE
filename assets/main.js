(function(){
  document.body.classList.add('js-enabled');
  const menuButton=document.querySelector('.menu-toggle');
  const nav=document.querySelector('.main-nav');
  if(menuButton&&nav){menuButton.addEventListener('click',()=>{const expanded=menuButton.getAttribute('aria-expanded')==='true';menuButton.setAttribute('aria-expanded',String(!expanded));nav.classList.toggle('open',!expanded)});nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');menuButton.setAttribute('aria-expanded','false')}));}
  const filterButtons=[...document.querySelectorAll('[data-filter]')];
  const projectCards=[...document.querySelectorAll('[data-category]')];
  filterButtons.forEach(b=>b.addEventListener('click',()=>{const filter=b.dataset.filter;filterButtons.forEach(x=>x.setAttribute('aria-pressed',String(x===b)));projectCards.forEach(c=>c.hidden=filter!=='tous'&&!c.dataset.category.split(' ').includes(filter))}));
  const items=document.querySelectorAll('.reveal');
  if('IntersectionObserver' in window){const obs=new IntersectionObserver(entries=>{for(const entry of entries){if(entry.isIntersecting){entry.target.classList.add('visible');obs.unobserve(entry.target)}}},{threshold:.1,rootMargin:'0px 0px -30px 0px'});items.forEach(i=>obs.observe(i));}
  else items.forEach(i=>i.classList.add('visible'));
  // Lightbox : accessible au clavier ; lien image conservé sans JS.
  const lightbox=document.getElementById('media-lightbox');
  if(lightbox&&typeof lightbox.showModal==='function'){
    const preview=lightbox.querySelector('img');
    const closer=lightbox.querySelector('.lightbox-close');
    document.querySelectorAll('[data-lightbox]').forEach(anchor=>{
      anchor.addEventListener('click',(event)=>{
        event.preventDefault();
        const small=anchor.querySelector('img');
        preview.src=anchor.getAttribute('href');
        preview.alt=small?.alt||'Photographie de projet';
        lightbox.showModal();
      });
    });
    closer?.addEventListener('click',()=>lightbox.close());
    lightbox.addEventListener('click',event=>{if(event.target===lightbox)lightbox.close()});
  }

})();
