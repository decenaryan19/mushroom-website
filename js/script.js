document.addEventListener('DOMContentLoaded', () => {
  initHeroCarousel();
  initMobileMenu();
  initBackToTop();
  initSmoothNavClose();
  initProductPage();
  initSampleForm();
  initContactForm();
});

function initHeroCarousel() {
  const slides = document.querySelectorAll('.hero-slide');
  const dots = document.querySelectorAll('.hero-dot');
  if (!slides.length) return;

  let current = 0;
  let intervalId = null;

  function goToSlide(index) {
    slides[current].classList.remove('active');
    dots[current]?.classList.remove('active');
    current = index;
    slides[current].classList.add('active');
    dots[current]?.classList.add('active');
  }

  function nextSlide() {
    goToSlide((current + 1) % slides.length);
  }

  dots.forEach((dot) => {
    dot.addEventListener('click', () => {
      goToSlide(Number(dot.dataset.slide));
      resetInterval();
    });
  });

  function resetInterval() {
    clearInterval(intervalId);
    intervalId = setInterval(nextSlide, 6000);
  }

  resetInterval();
}

function initMobileMenu() {
  const btn = document.getElementById('mobile-menu-btn');
  const menu = document.getElementById('mobile-menu');
  if (!btn || !menu) return;

  btn.addEventListener('click', () => {
    const isOpen = !menu.classList.contains('hidden');
    menu.classList.toggle('hidden');
    btn.setAttribute('aria-expanded', String(!isOpen));
  });
}

function initBackToTop() {
  const btn = document.getElementById('back-to-top');
  if (!btn) return;

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

function initSmoothNavClose() {
  const menu = document.getElementById('mobile-menu');
  const btn = document.getElementById('mobile-menu-btn');
  if (!menu) return;

  menu.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      menu.classList.add('hidden');
      btn?.setAttribute('aria-expanded', 'false');
    });
  });
}

function initProductPage() {
  initQuantitySelector();
  initProductTabs();
  initImageLightbox();
  initProductForm();
}

function initQuantitySelector() {
  const input = document.getElementById('qty-input');
  const minus = document.getElementById('qty-minus');
  const plus = document.getElementById('qty-plus');
  if (!input || !minus || !plus) return;

  minus.addEventListener('click', () => {
    const val = Math.max(1, parseInt(input.value, 10) - 1);
    input.value = val;
  });

  plus.addEventListener('click', () => {
    const val = Math.min(99, parseInt(input.value, 10) + 1);
    input.value = val;
  });

  input.addEventListener('change', () => {
    let val = parseInt(input.value, 10);
    if (isNaN(val) || val < 1) val = 1;
    if (val > 99) val = 99;
    input.value = val;
  });
}

function initProductTabs() {
  const tabs = document.querySelectorAll('.product-tab');
  if (!tabs.length) return;

  tabs.forEach((tab) => {
    tab.addEventListener('click', () => {
      const target = tab.dataset.tab;

      tabs.forEach((t) => {
        t.classList.remove('active');
        t.setAttribute('aria-selected', 'false');
      });
      tab.classList.add('active');
      tab.setAttribute('aria-selected', 'true');

      document.querySelectorAll('.product-tab-panel').forEach((panel) => {
        const isActive = panel.id === `tab-${target}`;
        panel.classList.toggle('active', isActive);
        panel.hidden = !isActive;
      });
    });
  });
}

function initImageLightbox() {
  const lightbox = document.getElementById('image-lightbox');
  const expandBtn = document.getElementById('expand-image-btn');
  const closeBtn = document.getElementById('lightbox-close');
  const mainImage = document.getElementById('product-main-image');
  if (!lightbox || !expandBtn || !mainImage) return;

  expandBtn.addEventListener('click', () => {
    lightbox.querySelector('img').src = mainImage.src;
    lightbox.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
  });

  function closeLightbox() {
    lightbox.classList.add('hidden');
    document.body.style.overflow = '';
  }

  closeBtn?.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) closeLightbox();
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !lightbox.classList.contains('hidden')) closeLightbox();
  });
}

function initProductForm() {
  const form = document.getElementById('product-form');
  const packageSelect = document.getElementById('package-select');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!packageSelect?.value) {
      packageSelect?.focus();
      return;
    }
    alert('Thank you! Your order has been added to cart.');
  });
}

function initSampleForm() {
  const form = document.getElementById('sample-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    alert('Thank you! Your free sample request has been submitted. We will contact you shortly.');
    form.reset();
  });
}

function initContactForm() {
  const form = document.getElementById('contact-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    alert('Thank you for your message! We will get back to you soon.');
    form.reset();
  });
}
