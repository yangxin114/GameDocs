// charms-interactions.js - 护身符系统前瞻页交互行为
// 著作: 看雲起雲落
(function() {
  'use strict';

  /* ====== 滚动进度条 ====== */
  function updateScrollProgress() {
    var fill = document.getElementById('scrollProgressFill');
    if (!fill) return;
    var scrolled = window.pageYOffset;
    var total = document.documentElement.scrollHeight - window.innerHeight;
    fill.style.width = total > 0 ? (scrolled / total * 100) + '%' : '0%';
  }

  /* ====== 返回顶部 ====== */
  function toggleBackToTop() {
    var btn = document.getElementById('backToTop');
    if (!btn) return;
    btn.classList.toggle('visible', window.pageYOffset > window.innerHeight);
  }

  function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  /* ====== 封面视差 ====== */
  function updateParallax() {
    var bg = document.querySelector('.charm-hero-bg');
    if (!bg) return;
    var y = window.pageYOffset;
    bg.style.transform = 'translate(' + (y * 0.02) + 'px, ' + (y * 0.05) + 'px)';
  }

  /* ====== 封面标题逐字动画 ====== */
  function animateTitle() {
    var el = document.getElementById('charmHeroTitle');
    if (!el || el.dataset.done) return;
    var text = el.textContent;
    el.innerHTML = '';
    for (var i = 0; i < text.length; i++) {
      var s = document.createElement('span');
      s.className = 'char';
      s.textContent = text[i] === ' ' ? ' ' : text[i];
      s.style.animationDelay = (i * 0.07) + 's';
      el.appendChild(s);
    }
    el.dataset.done = '1';
  }

  /* ====== 引导箭头 ====== */
  function scrollToCube() {
    var sec = document.getElementById('sec-cube');
    if (sec) sec.scrollIntoView({ behavior: 'smooth' });
  }

  /* ====== 配方解锁动画 ====== */
  function unlockRecipes() {
    var items = document.querySelectorAll('.recipe-item');
    items.forEach(function(item, i) {
      setTimeout(function() { item.classList.add('unlocked'); }, 300 + i * 180);
    });
  }

  /* ====== 封印卡片联动 ====== */
  function initSealCards() {
    var cards = document.querySelectorAll('.seal-card');
    cards.forEach(function(card) {
      card.addEventListener('mouseenter', function() {
        cards.forEach(function(o) { if (o !== card) o.style.opacity = '0.6'; });
      });
      card.addEventListener('mouseleave', function() {
        cards.forEach(function(o) { o.style.opacity = ''; });
      });
    });
  }

  /* ====== 套装Tab 筛选与切换 ====== */
  function initSetTabs() {
    var tabs = document.querySelectorAll('.set-tab');
    var panels = document.querySelectorAll('.set-panel');
    var currentFilter = 'all';

    function switchPanel(setName) {
      tabs.forEach(function(t) { t.classList.remove('active'); });
      panels.forEach(function(p) { p.classList.remove('active'); });

      var targetTab = document.querySelector('.set-tab[data-set="' + setName + '"]');
      if (targetTab) targetTab.classList.add('active');

      var targetPanel = document.getElementById('panel-' + setName);
      if (targetPanel) targetPanel.classList.add('active');
    }

    tabs.forEach(function(tab) {
      tab.addEventListener('click', function() {
        switchPanel(tab.dataset.set);
      });
    });

    window._switchSetPanel = switchPanel;

    // ====== 套装职业筛选 ======
    var filterBar = document.getElementById('setFilterBar');
    var tabsContainer = document.getElementById('setTabs');
    if (!filterBar || !tabsContainer) return;

    filterBar.addEventListener('click', function(e) {
      var btn = e.target.closest('.set-filter-btn');
      if (!btn) return;

      currentFilter = btn.dataset.filter;
      filterBar.querySelectorAll('.set-filter-btn').forEach(function(b) { b.classList.remove('active'); });
      btn.classList.add('active');

      // 筛选 tabs
      var allTabs = tabsContainer.querySelectorAll('.set-tab');
      var firstVisible = null;
      var activeTabVisible = false;

      allTabs.forEach(function(tab) {
        var show = currentFilter === 'all' || tab.dataset.class === currentFilter;
        tab.classList.toggle('hidden-by-filter', !show);
        if (show && !firstVisible) firstVisible = tab.dataset.set;
        if (show && tab.classList.contains('active')) activeTabVisible = true;
      });

      // 筛选 panels - 用 CSS class 控制，不用 style.display
      var allPanels = document.querySelectorAll('.set-panel');
      var activePanelVisible = false;

      allPanels.forEach(function(p) {
        var pClass = p.getAttribute('data-class') || '';
        var show = currentFilter === 'all' || pClass === currentFilter;
        p.classList.toggle('hidden-by-filter', !show);
        if (show && p.classList.contains('active')) activePanelVisible = true;
      });

      // 如果当前激活的 panel 被隐藏，切换到第一个可见的
      if (!activePanelVisible && firstVisible) {
        switchPanel(firstVisible);
      }
    });
  }

  /* ====== 套装卡片悬停 ====== */
  function initSetHover() {
    var cards = document.querySelectorAll('.set-charm-card');
    cards.forEach(function(card) {
      card.addEventListener('mouseenter', function() {
        var group = card.closest('.set-charms');
        if (group) {
          group.querySelectorAll('.set-charm-card').forEach(function(c) {
            if (c !== card) c.classList.add('dimmed');
          });
        }
        var bonus = card.dataset.bonus;
        if (bonus) {
          var panel = card.closest('.set-panel');
          if (panel) {
            panel.querySelectorAll('.set-bonus-item').forEach(function(b) { b.classList.remove('highlight'); });
            var items = panel.querySelectorAll('.set-bonus-item');
            if (items[bonus - 1]) items[bonus - 1].classList.add('highlight');
          }
        }
      });
      card.addEventListener('mouseleave', function() {
        var group = card.closest('.set-charms');
        if (group) group.querySelectorAll('.set-charm-card').forEach(function(c) { c.classList.remove('dimmed'); });
        var panel = card.closest('.set-panel');
        if (panel) panel.querySelectorAll('.set-bonus-item').forEach(function(b) { b.classList.remove('highlight'); });
      });
    });
  }

  /* ====== 祈唤符文悬停联动 ====== */
  function initRuneLinkage() {
    var rituals = document.querySelectorAll('.rune-card.mystery');
    var summons = document.querySelectorAll('.rune-card[data-pair]');
    rituals.forEach(function(r) {
      r.addEventListener('mouseenter', function() {
        var pair = r.dataset.rune;
        summons.forEach(function(s) {
          if (s.dataset.pair === pair) s.classList.add('linked');
        });
      });
      r.addEventListener('mouseleave', function() {
        summons.forEach(function(s) { s.classList.remove('linked'); });
      });
    });
  }

  /* ====== 符文之语模拟器 ====== */
  function initRuneSim() {
    var ritualSlot = document.getElementById('simRitual');
    var summonSlot = document.getElementById('simSummon');
    var result = document.getElementById('simResult');
    if (!ritualSlot || !summonSlot || !result) return;

    document.querySelectorAll('.rune-card.mystery').forEach(function(r) {
      r.addEventListener('click', function() {
        var name = r.querySelector('.rune-name')?.textContent || '';
        ritualSlot.innerHTML = '<div class="sim-label">仪式符文</div><div class="sim-val">' + name + '</div>';
        ritualSlot.classList.add('filled');
        checkResult();
      });
    });

    document.querySelectorAll('.rune-card:not(.mystery)').forEach(function(r) {
      r.addEventListener('click', function() {
        var name = r.querySelector('.rune-name')?.textContent || '';
        summonSlot.innerHTML = '<div class="sim-label">祈唤符文</div><div class="sim-val">' + name + '</div>';
        summonSlot.classList.add('filled');
        checkResult();
      });
    });

    function checkResult() {
      var rn = ritualSlot.querySelector('.sim-val')?.textContent || '';
      var sn = summonSlot.querySelector('.sim-val')?.textContent || '';
      if (rn && sn) {
        result.innerHTML = '<strong>' + rn + '</strong> + <strong>' + sn + '</strong><br><span style="color:#8a7a70;">效果将在 4月28日 正式上线后揭晓</span>';
      }
    }
  }

  /* ====== 稀有护身符筛选 ====== */
  function initRareFilters() {
    var filters = document.querySelectorAll('.rare-filter');
    var cards = document.querySelectorAll('.rare-card');
    filters.forEach(function(filter) {
      filter.addEventListener('click', function() {
        filters.forEach(function(f) { f.classList.remove('active'); });
        filter.classList.add('active');
        var type = filter.dataset.type;
        cards.forEach(function(card) {
          var show = type === 'all' || card.dataset.type === type;
          if (show) {
            card.style.display = '';
            card.classList.add('fade-in');
            setTimeout(function() { card.classList.remove('fade-in'); }, 400);
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }

  /* ====== 收藏功能 ====== */
  function initFavorites() {
    var KEY = 'charm-favorites-v2';
    var saved = [];
    try { saved = JSON.parse(localStorage.getItem(KEY) || '[]'); } catch(e) {}

    saved.forEach(function(id) {
      var star = document.querySelector('.fav-star[data-id="' + id + '"]');
      if (star) star.classList.add('active');
    });

    document.querySelectorAll('.fav-star').forEach(function(star) {
      star.addEventListener('click', function(e) {
        e.stopPropagation();
        var id = star.dataset.id;
        try {
          var arr = JSON.parse(localStorage.getItem(KEY) || '[]');
          if (star.classList.contains('active')) {
            star.classList.remove('active');
            arr = arr.filter(function(s) { return s !== id; });
          } else {
            star.classList.add('active');
            arr.push(id);
          }
          localStorage.setItem(KEY, JSON.stringify(arr));
        } catch(e) {}
      });
    });
  }

  /* ====== 一键复制 ====== */
  function initCopy() {
    var btn = document.getElementById('copyAccountBtn');
    if (!btn) return;
    btn.addEventListener('click', function() {
      var id = document.querySelector('.footer-account-id')?.textContent || '';
      navigator.clipboard.writeText(id.trim()).then(function() {
        showToast('已复制，4月28日不见不散');
      }).catch(function() {
        showToast('复制失败，请手动复制');
      });
    });
  }

  /* ====== 邮件订阅 ====== */
  function initSubscribe() {
    var form = document.getElementById('subscribeForm');
    if (!form) return;
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      var input = form.querySelector('input[type="email"]');
      var email = input ? input.value : '';
      if (email && email.includes('@')) {
        showToast('我们会在 DLC 上线时邮件通知你');
        input.value = '';
      } else {
        showToast('请输入有效的邮箱地址');
      }
    });
  }

  /* ====== Toast ====== */
  function showToast(msg) {
    var el = document.getElementById('toast');
    if (!el) return;
    el.textContent = msg;
    el.classList.add('show');
    setTimeout(function() { el.classList.remove('show'); }, 3000);
  }

  /* ====== 键盘快捷键 ====== */
  function initKeys() {
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        document.getElementById('lightboxOverlay')?.classList.remove('open');
      }
      if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
        var tabs = document.querySelectorAll('.set-tab');
        if (!tabs.length) return;
        var active = document.querySelector('.set-tab.active');
        var idx = Array.from(tabs).indexOf(active);
        if (e.key === 'ArrowRight') idx = (idx + 1) % tabs.length;
        else idx = (idx - 1 + tabs.length) % tabs.length;
        tabs[idx].click();
      }
    });
  }

  /* ====== 滚动触发动画 ====== */
  function initReveal() {
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08 });

    document.querySelectorAll('.charm-section').forEach(function(s) {
      observer.observe(s);
    });
  }

  /* ====== 侧边栏导航 ====== */
  function initSidebar() {
    // 移动端切换
    var toggle = document.getElementById('sidebarToggle');
    var sidebar = document.getElementById('charmSidebar');
    if (toggle && sidebar) {
      toggle.addEventListener('click', function() {
        sidebar.classList.toggle('open');
      });
      // 点击导航链接后关闭侧边栏
      sidebar.querySelectorAll('a[href^="#"]').forEach(function(a) {
        a.addEventListener('click', function() {
          sidebar.classList.remove('open');
        });
      });
    }

    // 滚动高亮当前区块
    var links = document.querySelectorAll('.charm-sidebar-nav a[href^="#"]');
    if (!links.length) return;

    var sections = [];
    links.forEach(function(link) {
      var id = link.getAttribute('href').replace('#', '');
      var sec = document.getElementById(id);
      if (sec) sections.push({ link: link, el: sec });
    });

    function updateActive() {
      var scrollY = window.pageYOffset + 150;
      var current = null;
      sections.forEach(function(s) {
        if (s.el.offsetTop <= scrollY) current = s.link;
      });
      links.forEach(function(l) { l.classList.remove('active'); });
      if (current) current.classList.add('active');
    }

    window.addEventListener('scroll', updateActive, { passive: true });
    updateActive();
  }

  /* ====== 初始化 ====== */
  function init() {
    window.addEventListener('scroll', function() {
      updateScrollProgress();
      toggleBackToTop();
      updateParallax();
    }, { passive: true });

    document.getElementById('scrollArrow')?.addEventListener('click', scrollToCube);
    document.getElementById('backToTop')?.addEventListener('click', scrollToTop);

    initSetTabs();
    initSetHover();
    initSealCards();
    initRuneLinkage();
    initRuneSim();
    initRareFilters();
    initFavorites();
    initCopy();
    initSubscribe();
    initKeys();
    initReveal();
    initSidebar();

    setTimeout(animateTitle, 400);
    setTimeout(unlockRecipes, 700);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
