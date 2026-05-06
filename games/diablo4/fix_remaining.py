with open('games/diablo4/horadric-cube-guide.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix nav - replace old 3 entries with simulator
old = """      <li><a href="#sec-modify"><span class="nav-icon">&#x1F527;</span><span class="nav-text">装备改造配方</span><span class="nav-step">CH 2</span></a></li>
      <li><a href="#sec-convert"><span class="nav-icon">&#x1F504;</span><span class="nav-text">物品塑形配方</span><span class="nav-step">CH 3</span></a></li>
      <li><a href="#sec-charms"><span class="nav-icon">&#x1F48E;</span><span class="nav-text">护身符&神符配方</span><span class="nav-step">CH 4</span></a></li>"""
new = """      <li><a href="#sec-simulator"><span class="nav-icon">&#x1F52E;</span><span class="nav-text">配方模拟器</span><span class="nav-step">CH 2</span></a></li>"""
content = content.replace(old, new)

# 2. Fix broken CH numbers (CH 7, CH 8 -> CH 3, CH 4)
content = content.replace('<span class="nav-step">CH 7</span>', '<span class="nav-step">CH 3</span>')
content = content.replace('<span class="nav-step">CH 8</span>', '<span class="nav-step">CH 4</span>')

# 3. Fix remaining "魔方" -> "魔盒"
content = content.replace('赫拉迪姆魔方界面', '赫拉迪姆魔盒界面')

# 4. Remove old recipe-card CSS
old_css = """    /* Recipe card */
    .recipe-card {
      background: var(--bg-dark);
      border: 1px solid rgba(58,32,40,0.5);
      border-radius: 14px;
      overflow: hidden;
      margin-bottom: 2rem;
      transition: all 0.3s;
    }

    .recipe-card:hover {
      border-color: rgba(218,165,32,0.3);
      box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    }

    .recipe-header {
      padding: 1.25rem 1.5rem;
      background: rgba(139,0,0,0.08);
      border-bottom: 1px solid rgba(58,32,40,0.4);
      display: flex;
      align-items: center;
      gap: 1rem;
      cursor: pointer;
      user-select: none;
    }

    .recipe-header:hover {
      background: rgba(139,0,0,0.12);
    }

    .recipe-name {
      font-family: 'Cinzel', serif;
      font-size: 1.05rem;
      font-weight: 600;
      color: #f0e8e0;
    }

    .recipe-name-en {
      font-size: 0.72rem;
      color: #554444;
      margin-left: 0.5rem;
    }

    .recipe-toggle {
      margin-left: auto;
      font-size: 0.8rem;
      color: #665555;
      transition: transform 0.3s;
    }

    .recipe-card.open .recipe-toggle {
      transform: rotate(180deg);
      color: var(--gold);
    }

    .recipe-body {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.5s cubic-bezier(0.4,0,0.2,1);
    }

    .recipe-card.open .recipe-body {
      max-height: 3000px;
    }

    .recipe-content {
      padding: 1.5rem;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
    }

    .recipe-info p {
      color: #b0a098;
      font-size: 0.88rem;
      line-height: 1.8;
      margin-bottom: 0.75rem;
    }

    .recipe-desc-en {
      font-style: italic;
      color: #665555;
      font-size: 0.82rem;
      line-height: 1.7;
      padding: 0.75rem 1rem;
      background: rgba(0,0,0,0.2);
      border-left: 3px solid var(--gold-dim);
      border-radius: 0 8px 8px 0;
      margin-bottom: 1rem;
    }

    .recipe-materials {
      list-style: none;
      padding: 0;
      margin: 0;
    }

    .recipe-materials li {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.4rem 0;
      font-size: 0.85rem;
      color: #b0a098;
      border-bottom: 1px solid rgba(58,32,40,0.2);
    }

    .recipe-materials li:last-child { border-bottom: none; }

    .mat-icon {
      font-size: 1rem;
      flex-shrink: 0;
    }

    .recipe-image {
      display: flex;
      align-items: flex-start;
      justify-content: center;
    }

    .recipe-image img {
      max-width: 100%;
      max-height: 400px;
      object-fit: contain;
      border-radius: 10px;
      border: 1px solid rgba(58,32,40,0.4);
      cursor: zoom-in;
      transition: all 0.3s;
    }

    .recipe-image img:hover {
      border-color: rgba(218,165,32,0.4);
      box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }

    .recipe-tip {
      display: flex;
      align-items: flex-start;
      gap: 0.5rem;
      padding: 0.65rem 1rem;
      background: rgba(39,174,96,0.06);
      border: 1px solid rgba(39,174,96,0.2);
      border-radius: 8px;
      margin-top: 0.75rem;
    }

    .recipe-tip p {
      font-size: 0.82rem;
      color: #6dbf8a;
      line-height: 1.6;
      margin: 0;
    }

    /* Warning */
    .recipe-warning {
      display: flex;
      align-items: flex-start;
      gap: 0.5rem;
      padding: 0.75rem 1rem;
      background: rgba(231,76,60,0.08);
      border: 1px solid rgba(231,76,60,0.25);
      border-radius: 8px;
      margin-top: 0.75rem;
    }

    .recipe-warning .warn-icon {
      font-size: 1rem;
      flex-shrink: 0;
      margin-top: 0.1rem;
    }

    .recipe-warning p {
      font-size: 0.82rem;
      color: #e07060;
      line-height: 1.6;
      margin: 0;
    }
"""
if old_css in content:
    content = content.replace(old_css, '')
    print("Old recipe-card CSS removed")

# 5. Also remove responsive rules for old cards
old_resp = """    @media (max-width: 900px) {
      .cube-page { padding: 0 1.5rem 3rem; }
      .recipe-content { grid-template-columns: 1fr; }
      .recipe-image { order: -1; }
    }"""
new_resp = """    @media (max-width: 900px) {
      .cube-page { padding: 0 1.5rem 3rem; }
    }"""
content = content.replace(old_resp, new_resp)

with open('games/diablo4/horadric-cube-guide.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("All fixes applied!")
