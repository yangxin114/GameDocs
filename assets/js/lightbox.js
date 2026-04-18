// lightbox.js - 图片灯箱功能
function showLightbox(src) {
  const lightbox = document.getElementById('lightbox');
  const img = document.getElementById('lightbox-img');
  if (lightbox && img) {
    img.src = src;
    lightbox.classList.add('open');
  }
}

function hideLightbox() {
  const lightbox = document.getElementById('lightbox');
  if (lightbox) {
    lightbox.classList.remove('open');
  }
}

// 点击遮罩关闭
document.addEventListener('click', function(e) {
  if (e.target.id === 'lightbox') {
    hideLightbox();
  }
});

// ESC关闭
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    hideLightbox();
  }
});
