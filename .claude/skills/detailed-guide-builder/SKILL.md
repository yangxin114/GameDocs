---
name: detailed-guide-builder
description: Build detailed guide pages (详细攻略页面) for the dark-game website. Use when the user wants to create a new detailed guide, BD攻略, mechanism explanation, equipment guide, or any multi-section攻略 page. All detailed guide pages must have a unified sidebar navigation, header, and footer.
---

# 详细攻略页面制作指南

所有详细攻略页面必须遵循以下统一结构。

## 文件结构

每个详细攻略页面（如 `games/diablo4/xxx-guide.html`）必须包含以下**三大固定组件**：

### 1. 站点 Header（页面最顶部）

位于 `<nav class="top-nav">` 之后、侧边栏之前。统一结构，所有页面相同：

```html
<!-- 站点 Header -->
<section class="site-header-section" style="padding:5rem 0 1rem;">
  <div class="container" style="display:flex;align-items:center;justify-content:center;gap:1.5rem;flex-wrap:wrap;">
    <div style="display:flex;align-items:center;gap:0.85rem;">
      <img src="{mypic_path}" alt="看雲起雲落" style="width:40px;height:40px;border-radius:50%;object-fit:cover;border:2px solid var(--gold);box-shadow:0 0 12px rgba(212,175,55,0.3);">
      <div>
        <div style="font-family:'Cinzel',serif;font-size:1rem;font-weight:700;color:var(--gold);">看雲起雲落</div>
        <div style="font-size:0.72rem;color:var(--text-muted);margin-top:0.1rem;">一只上班狗，业余刷刷刷，随缘更新</div>
      </div>
    </div>
    <img src="{bili_path}" alt="B站二维码" style="width:48px;height:48px;border-radius:6px;cursor:pointer;transition:all 0.2s;" onclick="document.getElementById('qrPreview').classList.add('open')" title="扫码查看B站主页">
    <a href="https://space.bilibili.com/443078910" target="_blank" style="display:inline-flex;align-items:center;gap:0.35rem;padding:0.3rem 0.75rem;background:rgba(251,114,153,0.08);border:1px solid rgba(251,114,153,0.2);border-radius:100px;font-size:0.7rem;color:#fb7299;text-decoration:none;transition:all 0.2s;">
      <svg viewBox="0 0 24 24" width="12" height="12" fill="#fb7299"><path d="M17.813 4.653h.854c1.51.054 2.769.578 3.773 1.574 1.004.995 1.524 2.249 1.56 3.76v7.36c-.036 1.51-.556 2.769-1.56 3.773s-2.262 1.524-3.773 1.56H5.333c-1.51-.036-2.769-.556-3.773-1.56S.036 18.858 0 17.347v-7.36c.036-1.511.556-2.765 1.56-3.76 1.004-.996 2.262-1.52 3.773-1.574h.774l-1.174-1.12a1.234 1.234 0 0 1-.373-.906c0-.356.124-.658.373-.907l.027-.027c.267-.249.573-.373.92-.373.347 0 .653.124.92.373L9.653 3.84c.071.071.134.142.187.213h4.267a.836.836 0 0 1 .16-.213l2.853-2.747c.267-.249.573-.373.92-.373.347 0 .662.151.929.4.267.249.391.551.391.907 0 .355-.124.657-.373.906L17.813 4.653zM5.333 7.24c-.746.018-1.373.276-1.88.773-.506.498-.769 1.13-.786 1.894v7.52c.017.764.28 1.395.786 1.893.507.498 1.134.756 1.88.773h13.334c.746-.017 1.373-.275 1.88-.773.506-.498.769-1.129.786-1.893v-7.52c-.017-.765-.28-1.396-.786-1.894-.507-.497-1.134-.755-1.88-.773H5.333zM8 11.107c.373 0 .684.124.933.373.25.249.383.569.4.96v1.173c-.017.391-.15.711-.4.96-.249.25-.56.374-.933.374s-.684-.125-.933-.374c-.25-.249-.383-.569-.4-.96V12.44c.017-.391.15-.711.4-.96.249-.249.56-.373.933-.373zm8 0c.373 0 .684.124.933.373.25.249.383.569.4.96v1.173c-.017.391-.15.711-.4.96-.249.25-.56.374-.933.374s-.684-.125-.933-.374c-.25-.249-.383-.569-.4-.96V12.44c.017-.391.15-.711.4-.96.249-.249.56-.373.933.373z"/></svg>
      space.bilibili.com/443078910
    </a>
  </div>
</section>
```

### 2. 左侧导航栏（统一布局）

所有详细攻略页面**必须**有左侧导航栏，使用 `.guide-sidebar` 类名。结构统一如下：

```html
<!-- ====== 左侧导航栏 ====== -->
<aside class="guide-sidebar" id="guideSidebar">
  <div class="guide-sidebar-title">目录导航</div>
  <ul class="guide-sidebar-nav">
    <li><a href="#sec-hero" class="active"><span class="nav-icon">&#x1F3E0;</span><span class="nav-text">封面</span><span class="nav-step">TOP</span></a></li>
    <li><a href="#sec-xxx"><span class="nav-icon">&#x1F4D6;</span><span class="nav-text">章节一</span><span class="nav-step">STEP 1</span></a></li>
    <li><a href="#sec-yyy"><span class="nav-icon">&#x2B50;</span><span class="nav-text">章节二</span><span class="nav-step">STEP 2</span></a></li>
    <!-- 可添加 .guide-sidebar-divider 分隔线 -->
    <li><a href="#sec-bonus"><span class="nav-icon">&#x1F48E;</span><span class="nav-text">附录</span><span class="nav-step">BONUS</span></a></li>
  </ul>
  <div class="guide-sidebar-footer">
    <a href="index.html">&#x2190; 返回{游戏名}首页</a>
  </div>
</aside>

<!-- 移动端侧边栏切换按钮 -->
<button class="guide-sidebar-toggle" id="sidebarToggle" aria-label="切换导航">
  <svg viewBox="0 0 24 24" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <line x1="3" y1="6" x2="21" y2="6"/>
    <line x1="3" y1="12" x2="21" y2="12"/>
    <line x1="3" y1="18" x2="21" y2="18"/>
  </svg>
</button>

<!-- ====== 主内容区域 ====== -->
<main class="guide-content">
  <!-- 页面内容 -->
</main>
```

**导航规范：**
- `.nav-icon`: emoji 字符（如 &#x1F4D6;），宽度 18px
- `.nav-text`: 导航文字（不超过 6 个汉字）
- `.nav-step`: 步骤标识（TOP, STEP 1, BONUS 等），可选
- 使用 `.guide-sidebar-divider` 分隔主要内容和附录
- 第一个导航项添加 `class="active"` 作为默认高亮

### 3. 站点 Footer（页面最底部）

位于 `</main>` 之前、内容之后。统一结构：

```html
<!-- Footer -->
<footer class="footer">
  <div class="container">
    <div style="display:flex;flex-direction:column;align-items:center;gap:0.6rem;">
      <a href="https://space.bilibili.com/443078910" target="_blank" style="display:inline-flex;align-items:center;gap:0.4rem;padding:0.35rem 0.85rem;background:rgba(251,114,153,0.1);border:1px solid rgba(251,114,153,0.2);border-radius:100px;font-size:0.75rem;color:#fb7299;text-decoration:none;transition:all 0.2s;">
        <svg viewBox="0 0 24 24" width="14" height="14" fill="#fb7299"><path d="M17.813 4.653h.854c1.51.054 2.769.578 3.773 1.574 1.004.995 1.524 2.249 1.56 3.76v7.36c-.036 1.51-.556 2.769-1.56 3.773s-2.262 1.524-3.773 1.56H5.333c-1.51-.036-2.769-.556-3.773-1.56S.036 18.858 0 17.347v-7.36c.036-1.511.556-2.765 1.56-3.76 1.004-.996 2.262-1.52 3.773-1.574h.774l-1.174-1.12a1.234 1.234 0 0 1-.373-.906c0-.356.124-.658.373-.907l.027-.027c.267-.249.573-.373.92-.373.347 0 .653.124.92.373L9.653 3.84c.071.071.134.142.187.213h4.267a.836.836 0 0 1 .16-.213l2.853-2.747c.267-.249.573-.373.92-.373.347 0 .662.151.929.4.267.249.391.551.391.907 0 .355-.124.657-.373.906L17.813 4.653zM5.333 7.24c-.746.018-1.373.276-1.88.773-.506.498-.769 1.13-.786 1.894v7.52c.017.764.28 1.395.786 1.893.507.498 1.134.756 1.88.773h13.334c.746-.017 1.373-.275 1.88-.773.506-.498.769-1.129.786-1.893v-7.52c-.017-.765-.28-1.396-.786-1.894-.507-.497-1.134-.755-1.88-.773H5.333zM8 11.107c.373 0 .684.124.933.373.25.249.383.569.4.96v1.173c-.017.391-.15.711-.4.96-.249.25-.56.374-.933.374s-.684-.125-.933-.374c-.25-.249-.383-.569-.4-.96V12.44c.017-.391.15-.711.4-.96.249-.249.56-.373.933-.373zm8 0c.373 0 .684.124.933.373.25.249.383.569.4.96v1.173c-.017.391-.15.711-.4.96-.249.25-.56.374-.933.374s-.684-.125-.933-.374c-.25-.249-.383-.569-.4-.96V12.44c.017-.391.15-.711.4-.96.249-.249.56-.373.933-.373z"/></svg>
        B站: @看雲起雲落
      </a>
      <img src="{bili_path}" alt="B站二维码" class="footer-qr" onclick="document.getElementById('qrPreview').classList.add('open')">
      <p style="font-size:0.65rem;color:#4a5568;">扫码查看B站主页</p>
      <p style="font-size:0.72rem;color:#4a5568;margin-top:0.5rem;">&copy; 2026 看雲起雲落</p>
    </div>
  </div>
</footer>

<!-- QR Code Preview -->
<div class="qr-preview-overlay" id="qrPreview" onclick="this.classList.remove('open')">
  <img src="{bili_path}" alt="B站二维码大图">
</div>
```

## 必须引入的文件

```html
<link rel="stylesheet" href="../../assets/css/base.css">
<link rel="stylesheet" href="../../assets/css/components.css">
<link rel="stylesheet" href="../../assets/css/theme-{gamename}.css">
<link rel="stylesheet" href="../../assets/css/guide-sidebar.css">
<script src="../../assets/js/guide-sidebar.js"></script>
```

路径根据页面深度调整：
- `games/{game}/index.html` → `../../` 前缀
- `games/{game}/{page}.html` → `../../` 前缀

图片路径：
- `{mypic_path}` = `../../mypic.jpg`
- `{bili_path}` = `../../assets/images/my-bili-2pic.png`

## 页面骨架模板

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{攻略标题} - {游戏名}</title>
  <link rel="stylesheet" href="../../assets/css/base.css">
  <link rel="stylesheet" href="../../assets/css/components.css">
  <link rel="stylesheet" href="../../assets/css/theme-{gamename}.css">
  <link rel="stylesheet" href="../../assets/css/guide-sidebar.css">
</head>
<body>
  <!-- 顶部导航 -->
  <nav class="top-nav">
    <div class="nav-inner">
      <a href="index.html" class="nav-back">&#x2190; 返回{游戏简称}</a>
      <span class="nav-game-name">{攻略名称}</span>
      <span class="nav-breadcrumb">首页 &gt; {游戏名} &gt; {攻略名}</span>
    </div>
  </nav>

  <!-- 站点 Header -->
  <section class="site-header-section" style="padding:5rem 0 1rem;">
    <!-- header 内容，见上方 -->
  </section>

  <!-- 左侧导航栏 -->
  <aside class="guide-sidebar" id="guideSidebar">
    <!-- 导航内容，见上方 -->
  </aside>

  <!-- 移动端切换 -->
  <button class="guide-sidebar-toggle">
    <!-- toggle 内容，见上方 -->
  </button>

  <!-- 主内容 -->
  <main class="guide-content">
    <!-- 各 section 内容 -->
    <section id="sec-xxx">
      <!-- 内容 -->
    </section>

    <!-- Footer -->
    <footer class="footer">
      <!-- footer 内容，见上方 -->
    </footer>

    <!-- QR Code Preview -->
    <div class="qr-preview-overlay" id="qrPreview" onclick="this.classList.remove('open')">
      <img src="../../assets/images/my-bili-2pic.png" alt="B站二维码大图">
    </div>
  </main>

  <script src="../../assets/js/guide-sidebar.js"></script>
</body>
</html>
```

## 严格规则

1. **必须有 Header**：站点 Header 在 top-nav 之后、侧边栏之前，所有攻略页面统一
2. **必须有 Footer**：使用统一 footer 结构（B站链接 + QR 二维码 + 版权），替换旧的 game-specific footer
3. **必须有侧边栏导航**：使用 `.guide-sidebar` 结构，包含目录导航 + 返回链接
4. **使用共享组件**：引入 `guide-sidebar.css` 和 `guide-sidebar.js`，不自行编写侧边栏 CSS/JS
5. **section 使用 id**：每个内容区块必须有 `id="sec-xxx"`，与侧边栏导航的 `href="#sec-xxx"` 对应
6. **导航项结构统一**：每个导航项必须有 `.nav-icon` + `.nav-text`，可选 `.nav-step`
7. **路径正确**：mypic.jpg 和 my-bili-2pic.png 使用相对于当前页面的正确路径
8. **不允许重复 footer**：页面中只能有一个 `.footer`，不能保留旧的 game-specific footer

## 参考页面

- `games/diablo4/horadric-charms.html` — 完整的详细攻略页面示例（多章节、Tab 切换）
- `games/diablo4/warlock-build.html` — BD 类攻略示例（sidebar 布局不同，注意区分）
