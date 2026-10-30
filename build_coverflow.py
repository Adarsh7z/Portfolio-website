import re

file_path = "index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

changes = 0

# ═══════════════════════════════════════════════════════════════════════
# 1. CSS — insert before </style> (line 1040)
# ═══════════════════════════════════════════════════════════════════════
coverflow_css = r"""
    /* === 3D COVERFLOW PORTFOLIO SHOWCASE === */
    #portfolio-showcase{
      background:radial-gradient(ellipse at 30% 50%,rgba(120,20,40,.8) 0%,rgba(30,10,50,.9) 50%,#0a0a0f 100%);
      padding:6rem 2.5rem;
      text-align:center;
      overflow:hidden;
      position:relative;
    }
    .pf-label{
      font-size:.85rem;letter-spacing:3px;text-transform:uppercase;
      color:var(--fg-muted);margin-bottom:.75rem;font-weight:500;
    }
    .filter-tabs{
      display:flex;justify-content:center;gap:.75rem;
      margin-bottom:3rem;flex-wrap:wrap;
    }
    .filter-tab{
      padding:.6rem 1.5rem;border-radius:50px;border:1px solid transparent;
      background:transparent;color:var(--fg-muted);font-size:.9rem;
      font-weight:500;cursor:pointer;transition:all .3s ease;font-family:inherit;
    }
    .filter-tab.active{
      color:#fff;border-color:rgba(118,33,177,.8);
      box-shadow:0 0 15px rgba(118,33,177,.4),0 0 30px rgba(118,33,177,.15);
      background:rgba(118,33,177,.15);
    }
    .filter-tab:hover:not(.active){color:#fff;border-color:rgba(255,255,255,.2)}

    .coverflow-wrap{
      perspective:1200px;display:flex;justify-content:center;align-items:center;
      position:relative;height:520px;max-width:1000px;margin:0 auto;
    }
    .cf-card{
      position:absolute;width:200px;aspect-ratio:9/16;border-radius:20px;
      overflow:hidden;cursor:pointer;
      transition:all .7s cubic-bezier(.25,.46,.45,.94);
      box-shadow:0 20px 50px rgba(0,0,0,.6);
      border:1px solid rgba(255,255,255,.1);
    }
    .cf-card video,.cf-card img{width:100%;height:100%;object-fit:cover;display:block}
    .cf-card .cf-label{
      position:absolute;bottom:16px;left:16px;right:16px;
      color:#fff;font-size:.85rem;font-weight:600;
      text-shadow:0 2px 8px rgba(0,0,0,.9);z-index:5;text-align:left;
    }
    .cf-card::after{
      content:'';position:absolute;bottom:0;left:0;right:0;height:40%;
      background:linear-gradient(transparent,rgba(0,0,0,.7));
      pointer-events:none;z-index:4;
    }
    .cf-card.cf-center{
      transform:rotateY(0deg) translateZ(120px) scale(1.1);
      z-index:3;opacity:1;
    }
    .cf-card.cf-center:hover{
      box-shadow:0 25px 60px rgba(118,33,177,.35),0 0 30px rgba(118,33,177,.2);
      border-color:rgba(118,33,177,.5);
    }
    .cf-card.cf-left{
      transform:rotateY(-38deg) translateX(-220px) translateZ(0px) scale(.85);
      z-index:2;opacity:.75;
    }
    .cf-card.cf-right{
      transform:rotateY(38deg) translateX(220px) translateZ(0px) scale(.85);
      z-index:2;opacity:.75;
    }
    .cf-card.cf-far-left{
      transform:rotateY(-55deg) translateX(-370px) translateZ(-80px) scale(.65);
      z-index:1;opacity:.35;
    }
    .cf-card.cf-far-right{
      transform:rotateY(55deg) translateX(370px) translateZ(-80px) scale(.65);
      z-index:1;opacity:.35;
    }
    .cf-card.cf-hidden{
      transform:translateZ(-200px) scale(0);
      z-index:0;opacity:0;pointer-events:none;
    }

    /* Carousel Nav Arrows (mobile) */
    .cf-arrows{display:none;justify-content:center;gap:1rem;margin-top:2rem}
    .cf-arrow{
      width:48px;height:48px;border-radius:50%;
      background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.2);
      color:#fff;font-size:1.2rem;cursor:pointer;
      display:flex;align-items:center;justify-content:center;
      transition:all .3s;font-family:inherit;
    }
    .cf-arrow:hover{background:var(--purple);border-color:var(--purple);transform:scale(1.1)}

    /* Dot Indicators */
    .cf-dots{display:flex;justify-content:center;gap:8px;margin-top:1.5rem}
    .cf-dot{
      width:8px;height:8px;border-radius:50%;
      background:rgba(255,255,255,.2);border:none;cursor:pointer;
      transition:all .3s;padding:0;
    }
    .cf-dot.active{background:rgba(118,33,177,.9);transform:scale(1.3);box-shadow:0 0 8px rgba(118,33,177,.5)}

    /* Vimeo Lightbox */
    .vimeo-lb{
      display:none;position:fixed;z-index:3000;top:0;left:0;width:100%;height:100%;
      background:rgba(0,0,0,.92);backdrop-filter:blur(8px);
      justify-content:center;align-items:center;flex-direction:column;
    }
    .vimeo-lb.active{display:flex}
    .vimeo-lb-inner{width:90%;max-width:900px;aspect-ratio:16/9;position:relative}
    .vimeo-lb-inner iframe{width:100%;height:100%;border:none;border-radius:16px}
    .vimeo-lb-x{
      position:absolute;top:20px;right:30px;font-size:2rem;color:#fff;
      cursor:pointer;z-index:3001;transition:color .3s;background:none;
      border:none;font-family:inherit;
    }
    .vimeo-lb-x:hover{color:var(--purple)}

    /* Mobile Responsive — Coverflow */
    @media(max-width:768px){
      #portfolio-showcase{padding:4rem 1.25rem}
      .coverflow-wrap{height:400px}
      .cf-card{width:170px}
      .cf-card.cf-far-left,.cf-card.cf-far-right{opacity:0;pointer-events:none}
      .cf-card.cf-left{transform:rotateY(-20deg) translateX(-130px) translateZ(0) scale(.78)}
      .cf-card.cf-right{transform:rotateY(20deg) translateX(130px) translateZ(0) scale(.78)}
      .cf-arrows{display:flex}
    }
    @media(max-width:480px){
      .coverflow-wrap{height:370px}
      .cf-card{width:155px}
      .cf-card.cf-left{transform:rotateY(-15deg) translateX(-105px) translateZ(0) scale(.75);opacity:.55}
      .cf-card.cf-right{transform:rotateY(15deg) translateX(105px) translateZ(0) scale(.75);opacity:.55}
    }
"""

css_anchor = "  </style>"
if "3D COVERFLOW" not in content:
    content = content.replace(css_anchor, coverflow_css + "\n" + css_anchor, 1)
    changes += 1
    print("1. Added Coverflow CSS")
else:
    print("SKIP: Coverflow CSS already present")


# ═══════════════════════════════════════════════════════════════════════
# 2. HTML SECTION — between Experience </section> and Skills comment
# ═══════════════════════════════════════════════════════════════════════
showcase_html = """
<!-- ======= 3D COVERFLOW PORTFOLIO SHOWCASE ======= -->
<section id="portfolio-showcase">
  <p class="pf-label fade-el">SELECTED WORK</p>
  <h2 class="section-heading hg fade-el">Portfolio Showcase</h2>

  <div class="filter-tabs fade-el d1">
    <button class="filter-tab active" data-filter="all">All</button>
    <button class="filter-tab" data-filter="video">Video Editing</button>
    <button class="filter-tab" data-filter="web">Web Design</button>
    <button class="filter-tab" data-filter="marketing">Marketing</button>
  </div>

  <div class="coverflow-wrap" id="coverflow-carousel">
    <!-- Cards built by JS -->
  </div>

  <div class="cf-dots" id="cf-dots"></div>

  <div class="cf-arrows">
    <button class="cf-arrow" id="cf-prev" aria-label="Previous card">
      <i class="fa-solid fa-chevron-left"></i>
    </button>
    <button class="cf-arrow" id="cf-next" aria-label="Next card">
      <i class="fa-solid fa-chevron-right"></i>
    </button>
  </div>
</section>

"""

html_anchor = "</section>\r\n\r\n<!-- ======= SKILLS (CORE COMPETENCIES) ======= -->"
if "portfolio-showcase" not in content:
    content = content.replace(html_anchor, "</section>\r\n" + showcase_html + "<!-- ======= SKILLS (CORE COMPETENCIES) ======= -->", 1)
    changes += 1
    print("2. Added Portfolio Showcase HTML section")
else:
    print("SKIP: Portfolio Showcase HTML already present")


# ═══════════════════════════════════════════════════════════════════════
# 3. VIMEO LIGHTBOX HTML — before GSAP libraries
# ═══════════════════════════════════════════════════════════════════════
vimeo_lb_html = """
<!-- ======= VIMEO LIGHTBOX ======= -->
<div class="vimeo-lb" id="vimeo-lb">
  <button class="vimeo-lb-x" id="vimeo-lb-x" aria-label="Close video">&times;</button>
  <div class="vimeo-lb-inner">
    <iframe id="vimeo-lb-iframe" src="" title="Portfolio Video" allow="fullscreen; picture-in-picture" allowfullscreen></iframe>
  </div>
</div>

"""

gsap_anchor = "  <!-- GSAP & ScrollTrigger Libraries -->"
if "vimeo-lb" not in content:
    content = content.replace(gsap_anchor, vimeo_lb_html + gsap_anchor, 1)
    changes += 1
    print("3. Added Vimeo Lightbox HTML")
else:
    print("SKIP: Vimeo Lightbox already present")


# ═══════════════════════════════════════════════════════════════════════
# 4. JAVASCRIPT — functions before initMonitorScrollTrigger
# ═══════════════════════════════════════════════════════════════════════
coverflow_js = r"""
/* ─── 3D COVERFLOW CAROUSEL ────────────────────────────────────────── */
const PORTFOLIO_DATA = [
  /* ── Video Editing ─────────────────────────────────────────────── */
  {
    category: 'video',
    title: 'Brand Anthem',
    poster: 'https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?w=400&h=711&fit=crop&crop=center',
    videoSrc: '',   /* Replace with your Vimeo MP4 preview URL */
    vimeoUrl: ''    /* Replace with https://player.vimeo.com/video/XXXXX */
  },
  {
    category: 'video',
    title: 'Product Launch Film',
    poster: 'https://images.unsplash.com/photo-1574717024453-354056aafa98?w=400&h=711&fit=crop&crop=center',
    videoSrc: '',
    vimeoUrl: ''
  },
  /* ── Web Design ────────────────────────────────────────────────── */
  {
    category: 'web',
    title: 'E-Commerce Redesign',
    poster: 'https://images.unsplash.com/photo-1547658719-da2b51169166?w=400&h=711&fit=crop&crop=center',
    videoSrc: '',
    vimeoUrl: ''
  },
  {
    category: 'web',
    title: 'SaaS Dashboard',
    poster: 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400&h=711&fit=crop&crop=center',
    videoSrc: '',
    vimeoUrl: ''
  },
  /* ── Marketing ─────────────────────────────────────────────────── */
  {
    category: 'marketing',
    title: 'Social Media Campaign',
    poster: 'https://images.unsplash.com/photo-1611162616305-c69b3fa7fbe0?w=400&h=711&fit=crop&crop=center',
    videoSrc: '',
    vimeoUrl: ''
  },
  {
    category: 'marketing',
    title: 'Growth Analytics',
    poster: 'https://images.unsplash.com/photo-1533750516457-a7f992034fec?w=400&h=711&fit=crop&crop=center',
    videoSrc: '',
    vimeoUrl: ''
  }
];

function initCoverflowCarousel() {
  const container = document.getElementById('coverflow-carousel');
  const dotsWrap  = document.getElementById('cf-dots');
  if (!container) return;

  let filteredItems = [...PORTFOLIO_DATA];
  let currentIndex  = 0;
  let autoTimer     = null;

  /* ── Build Cards ─────────────────────────────────────────────── */
  function buildCards() {
    container.innerHTML = '';
    if (dotsWrap) dotsWrap.innerHTML = '';

    filteredItems.forEach((item, i) => {
      const card = document.createElement('div');
      card.className = 'cf-card cf-hidden';
      card.dataset.index = i;

      if (item.videoSrc) {
        const v = document.createElement('video');
        v.poster = item.poster; v.autoplay = true; v.muted = true;
        v.loop = true; v.playsInline = true; v.loading = 'lazy';
        v.setAttribute('playsinline', '');
        const src = document.createElement('source');
        src.src = item.videoSrc; src.type = 'video/mp4';
        v.appendChild(src);
        card.appendChild(v);
      } else {
        const img = document.createElement('img');
        img.src = item.poster; img.alt = item.title;
        img.loading = 'lazy'; img.decoding = 'async';
        card.appendChild(img);
      }

      const label = document.createElement('span');
      label.className = 'cf-label';
      label.textContent = item.title;
      card.appendChild(label);

      card.addEventListener('click', () => onCardClick(i));
      container.appendChild(card);

      /* Dot */
      if (dotsWrap) {
        const dot = document.createElement('button');
        dot.className = 'cf-dot' + (i === 0 ? ' active' : '');
        dot.setAttribute('aria-label', 'Go to ' + item.title);
        dot.addEventListener('click', () => { currentIndex = i; updatePositions(); resetAuto(); });
        dotsWrap.appendChild(dot);
      }
    });

    currentIndex = 0;
    updatePositions();
  }

  /* ── Position Cards ──────────────────────────────────────────── */
  function updatePositions() {
    const cards = container.querySelectorAll('.cf-card');
    const total = filteredItems.length;
    if (total === 0) return;

    cards.forEach((card, i) => {
      /* Remove all position classes */
      card.className = 'cf-card';

      let offset = i - currentIndex;
      if (total > 2) {
        if (offset > Math.floor(total / 2)) offset -= total;
        if (offset < -Math.floor(total / 2)) offset += total;
      }

      if      (offset ===  0) card.classList.add('cf-center');
      else if (offset === -1) card.classList.add('cf-left');
      else if (offset ===  1) card.classList.add('cf-right');
      else if (offset === -2) card.classList.add('cf-far-left');
      else if (offset ===  2) card.classList.add('cf-far-right');
      else                    card.classList.add('cf-hidden');

      /* Play/pause videos */
      const vid = card.querySelector('video');
      if (vid) {
        if (offset === 0) vid.play().catch(() => {});
        else vid.pause();
      }
    });

    /* Update dots */
    if (dotsWrap) {
      dotsWrap.querySelectorAll('.cf-dot').forEach((d, i) => {
        d.classList.toggle('active', i === currentIndex);
      });
    }
  }

  /* ── Click Handler ───────────────────────────────────────────── */
  function onCardClick(index) {
    if (index === currentIndex) {
      const item = filteredItems[index];
      if (item.vimeoUrl) openVimeoLB(item.vimeoUrl);
      return;
    }
    currentIndex = index;
    updatePositions();
    resetAuto();
  }

  /* ── Auto-rotation ───────────────────────────────────────────── */
  function advance()  { currentIndex = (currentIndex + 1) % filteredItems.length; updatePositions(); }
  function goBack()   { currentIndex = (currentIndex - 1 + filteredItems.length) % filteredItems.length; updatePositions(); }
  function resetAuto(){ clearInterval(autoTimer); autoTimer = setInterval(advance, 3000); }

  /* ── Filter Tabs ─────────────────────────────────────────────── */
  document.querySelectorAll('.filter-tab').forEach(tab => {
    tab.addEventListener('click', () => {
      document.querySelector('.filter-tab.active')?.classList.remove('active');
      tab.classList.add('active');
      const f = tab.dataset.filter;
      filteredItems = f === 'all' ? [...PORTFOLIO_DATA] : PORTFOLIO_DATA.filter(it => it.category === f);
      currentIndex = 0;
      buildCards();
      resetAuto();
    });
  });

  /* ── Nav Arrows ──────────────────────────────────────────────── */
  const prev = document.getElementById('cf-prev');
  const next = document.getElementById('cf-next');
  if (prev) prev.addEventListener('click', () => { goBack(); resetAuto(); });
  if (next) next.addEventListener('click', () => { advance(); resetAuto(); });

  /* ── Pause auto-rotate on hover ──────────────────────────────── */
  container.addEventListener('mouseenter', () => clearInterval(autoTimer));
  container.addEventListener('mouseleave', () => resetAuto());

  /* ── Touch swipe support ─────────────────────────────────────── */
  let touchStartX = 0;
  container.addEventListener('touchstart', e => { touchStartX = e.changedTouches[0].clientX; }, { passive: true });
  container.addEventListener('touchend', e => {
    const dx = e.changedTouches[0].clientX - touchStartX;
    if (Math.abs(dx) > 40) { dx > 0 ? goBack() : advance(); resetAuto(); }
  }, { passive: true });

  /* ── Deferred init via IntersectionObserver ───────────────────── */
  const section = document.getElementById('portfolio-showcase');
  if (!section) return;
  const obs = new IntersectionObserver((entries, observer) => {
    if (entries[0].isIntersecting) {
      buildCards();
      resetAuto();
      observer.disconnect();
    }
  }, { rootMargin: '200px 0px' });
  obs.observe(section);
}

/* ── Vimeo Lightbox Helpers ──────────────────────────────────────── */
function openVimeoLB(url) {
  const lb = document.getElementById('vimeo-lb');
  const fr = document.getElementById('vimeo-lb-iframe');
  if (!lb || !fr) return;
  fr.src = url;
  lb.classList.add('active');
  document.body.style.overflow = 'hidden';
}
function closeVimeoLB() {
  const lb = document.getElementById('vimeo-lb');
  const fr = document.getElementById('vimeo-lb-iframe');
  if (!lb || !fr) return;
  lb.classList.remove('active');
  fr.src = '';
  document.body.style.overflow = '';
}

"""

js_anchor = "/* ─── GSAP MONITOR SCROLLTRIGGER ANIMATION ───────────────────────────── */"
if "initCoverflowCarousel" not in content:
    content = content.replace(js_anchor, coverflow_js + js_anchor, 1)
    changes += 1
    print("4. Added Coverflow JS functions")
else:
    print("SKIP: Coverflow JS already present")


# ═══════════════════════════════════════════════════════════════════════
# 5. INIT CALL — add after initMonitorScrollTrigger();
# ═══════════════════════════════════════════════════════════════════════
init_anchor = "initMonitorScrollTrigger();\r\n"
init_new = """initMonitorScrollTrigger();
initCoverflowCarousel();

/* Vimeo lightbox close handlers */
document.getElementById('vimeo-lb-x')?.addEventListener('click', closeVimeoLB);
document.getElementById('vimeo-lb')?.addEventListener('click', function(e) { if (e.target === this) closeVimeoLB(); });
document.addEventListener('keydown', function(e) { if (e.key === 'Escape') closeVimeoLB(); });
"""

if "initCoverflowCarousel" not in content.split(init_anchor.strip())[1] if init_anchor.strip() in content else True:
    content = content.replace(init_anchor, init_new, 1)
    changes += 1
    print("5. Added init call + lightbox close handlers")
else:
    print("SKIP: Init call already present")


# ═══════════════════════════════════════════════════════════════════════
# WRITE
# ═══════════════════════════════════════════════════════════════════════
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"\nDone — {changes}/5 changes applied.")
