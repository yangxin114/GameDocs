/**
 * main.js - 公共交互功能
 * @author 看雲起雲落
 */

// 导航栏滚动效果
(function() {
  const nav = document.querySelector('.top-nav');
  if (!nav) return;

  window.addEventListener('scroll', function() {
    nav.classList.toggle('scrolled', window.scrollY > 10);
  }, { passive: true });
})();

// 卡片滚动显示动画
(function() {
  const cards = document.querySelectorAll('.guide-card');
  if (!cards.length) return;

  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.05, rootMargin: '0px 0px -30px 0px' });

  cards.forEach(function(card, i) {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'opacity 0.5s ease ' + (i * 0.08) + 's, transform 0.5s ease ' + (i * 0.08) + 's';
    observer.observe(card);
  });
})();

// 返回顶部按钮
(function() {
  const btn = document.createElement('button');
  btn.className = 'back-to-top';
  btn.innerHTML = '&#x2191;';
  btn.setAttribute('aria-label', '返回顶部');
  document.body.appendChild(btn);

  window.addEventListener('scroll', function() {
    btn.classList.toggle('visible', window.scrollY > 400);
  }, { passive: true });

  btn.addEventListener('click', function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
})();

// 页面加载完成动画
(function() {
  document.body.style.opacity = '0';
  document.body.style.transition = 'opacity 0.4s ease';
  window.addEventListener('load', function() {
    document.body.style.opacity = '1';
  });
})();

// 图片灯箱功能
(function() {
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightbox-img');
  if (!lightbox || !lightboxImg) return;

  // 点击图片预览区域打开灯箱
  document.querySelectorAll('.img-preview').forEach(function(preview) {
    preview.addEventListener('click', function(e) {
      const img = this.querySelector('img');
      if (img && img.src) {
        lightboxImg.src = img.src;
        lightbox.classList.add('open');
        e.preventDefault();
      }
    });
  });

  // 点击遮罩关闭
  lightbox.addEventListener('click', function(e) {
    if (e.target === lightbox) {
      lightbox.classList.remove('open');
    }
  });

  // ESC键关闭
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      lightbox.classList.remove('open');
    }
  });
})();
