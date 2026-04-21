/**
 * guide-sidebar.js - 详细攻略页面侧边栏交互
 * - 移动端侧边栏切换
 * - 滚动高亮当前区块
 * - 点击平滑滚动
 * @author 看雲起雲落
 */
(function() {
  'use strict';

  /* 移动端侧边栏切换 */
  var toggle = document.querySelector('.guide-sidebar-toggle');
  var sidebar = document.querySelector('.guide-sidebar');
  if (toggle && sidebar) {
    toggle.addEventListener('click', function() {
      sidebar.classList.toggle('open');
    });
    // 点击导航项后关闭侧边栏（移动端）
    sidebar.querySelectorAll('a[href^="#"]').forEach(function(link) {
      link.addEventListener('click', function() {
        if (window.innerWidth <= 768) sidebar.classList.remove('open');
      });
    });
  }

  /* 滚动高亮当前区块 */
  var links = document.querySelectorAll('.guide-sidebar-nav a[href^="#"]');
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
})();
