with open('games/diablo4/horadric-cube-guide.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ===== 1. "魔方" → "魔盒" (in visible text only) =====
lines = content.split('\n')
new_lines = []
for line in lines:
    if 'href=' in line or 'src=' in line or 'data-' in line:
        new_lines.append(line)
    else:
        new_lines.append(line.replace('魔方', '魔盒'))
content = '\n'.join(new_lines)
print("Step 1 done: 魔方→魔盒")

# ===== 2. 移除"配方分类一览"表格区块 =====
start_marker = '<h3 style="font-family:\'Cinzel\',serif;font-size:1rem;color:#f0e8e0;margin-bottom:1rem;">配方分类一览</h3>'
if start_marker in content:
    start_idx = content.index(start_marker)
    search_from = start_idx + len(start_marker)
    end_idx = content.index('</section>\n</section>', search_from) + len('</section>\n</section>')
    content = content[:start_idx] + content[end_idx:]
    print("Step 2 done: 移除配方分类一览")
else:
    print("WARNING: 配方分类一览 not found!")

# ===== 3. 将"解锁流程"移到QA末尾 =====
unlock_start = '<!-- ====== 解锁流程 ====== -->'
unlock_end = '<!-- ====== 核心机制详解 ====== -->'

if unlock_start in content:
    u_start = content.index(unlock_start)
    u_end = content.index(unlock_end)
    unlock_html = content[u_start:u_end]
    content = content[:u_start] + content[u_end:]
    print("Step 3a: 提取解锁流程")
else:
    print("WARNING: unlock section not found!")
    unlock_html = ""

qa_insert_marker = '<!-- 护身符终极配置 -->'
if qa_insert_marker in content and unlock_html:
    unlock_qa = '''        <div class="qa-item">
          <div class="qa-q">&#x2753; 如何解锁魔盒？开荒流程怎么安排？</div>
          <div class="qa-a">
            <div class="highlight-box warn" style="margin-top:0;margin-bottom:1rem;">
              <strong>&#x26A0;&#xFE0F; 前置条件：</strong>必须拥有《憎恨之王》资料片。
            </div>
            <ol class="step-list" style="margin-bottom:1rem;">
              <li>新建赛季角色后，<strong>勾选"跳过剧情"</strong>以直接进入DLC区域。</li>
              <li>全力推进资料片主线，当任务进行到击败<strong>"督军泽尔坎"</strong>后即可解锁。</li>
              <li>抵达泰米斯与魔盒互动一次，即可<strong>账号全角色共享</strong>。</li>
            </ol>
            <p><strong>开荒时间节点：</strong></p>
            <ul>
              <li><strong>1-45级：</strong>核心目标是<strong style="color:var(--gold);">疯狂推进DLC主线</strong>。路上掉落的装备全部拆解，以积累基础材料。</li>
              <li><strong>约45级：</strong>魔盒正式解锁。此时已积累了大量原始之尘，立刻给开荒角色<strong style="color:var(--gold);">打造第一套质变装备</strong>，体验碾压同级的快感。</li>
            </ul>
          </div>
        </div>

        <!-- 护身符终极配置 -->'''
    content = content.replace('<!-- 护身符终极配置 -->', unlock_qa)
    print("Step 3b: 解锁流程移到QA末尾")
else:
    print("WARNING: QA insert failed!")

# ===== 4. 去掉九宫格，左侧放说明 =====
old_sim_body = """            <div class="sim-cube-grid" id="simCubeGrid">
                <div class="sim-slot" data-idx="0"><span class="slot-icon">&#x25A1;</span><span class="slot-label">空位</span></div>
                <div class="sim-slot" data-idx="1"><span class="slot-icon">&#x25A1;</span><span class="slot-label">空位</span></div>
                <div class="sim-slot" data-idx="2"><span class="slot-icon">&#x25A1;</span><span class="slot-label">空位</span></div>
                <div class="sim-slot" data-idx="3"><span class="slot-icon">&#x25A1;</span><span class="slot-label">空位</span></div>
                <div class="sim-slot" data-idx="4"><span class="slot-icon">&#x25A1;</span><span class="slot-label">空位</span></div>
                <div class="sim-slot" data-idx="5"><span class="slot-icon">&#x25A1;</span><span class="slot-label">空位</span></div>
                <div class="sim-slot" data-idx="6"><span class="slot-icon">&#x25A1;</span><span class="slot-label">空位</span></div>
                <div class="sim-slot" data-idx="7"><span class="slot-icon">&#x25A1;</span><span class="slot-label">空位</span></div>
                <div class="sim-slot" data-idx="8"><span class="slot-icon">&#x25A1;</span><span class="slot-label">空位</span></div>
              </div>

              <div class="sim-buttons">
                <button class="sim-btn clear" id="simClearBtn">清除</button>
                <button class="sim-btn transmute" id="simTransmuteBtn">重塑</button>
              </div>

              <div class="sim-detail-fade" id="simDetail">
                <div class="sim-recipe-title" id="simRecipeTitle">添加词缀</div>
                <div class="sim-recipe-desc-en" id="simRecipeDescEn">Adds a random Affix to an Item.</div>
                <div class="sim-recipe-desc" id="simRecipeDesc"></div>
                <div class="sim-materials-title">所需材料</div>
                <ul class="sim-materials" id="simMaterials">
                  <li>请选择右侧配方查看详情</li>
                </ul>
                <div id="simWarning" style="display:none;"></div>
              </div>"""

new_sim_body = """            <div class="sim-detail" id="simDetail">
                <div class="sim-recipe-title" id="simRecipeTitle">添加词缀</div>
                <div class="sim-recipe-desc-en" id="simRecipeDescEn">Adds a random Affix to an Item.</div>
                <div class="sim-section-label">配方说明</div>
                <div class="sim-recipe-desc" id="simRecipeDesc">请选择右侧配方查看详情</div>
                <div class="sim-section-label">所需材料</div>
                <ul class="sim-materials" id="simMaterials">
                  <li>请选择右侧配方查看详情</li>
                </ul>
                <div id="simWarning" style="display:none;"></div>
              </div>"""

if old_sim_body in content:
    content = content.replace(old_sim_body, new_sim_body)
    print("Step 4 done: 去掉九宫格，替换为说明区")
else:
    print("WARNING: sim body not found!")

# ===== 5. 配方列表只展示分类和配方名称 =====
old_js = "i.innerHTML = '<div class=\"r-name\">' + r.name + '</div><div class=\"r-desc\">' + r.desc + '</div>';"
new_js = "i.innerHTML = '<div class=\"r-name\">' + r.name + '</div>';"
if old_js in content:
    content = content.replace(old_js, new_js)
    print("Step 5 done: 配方列表只展示名称")
else:
    print("WARNING: JS item template not found!")

# Clean up unused CSS
content = content.replace("""    .sim-cube-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 0.75rem;
      margin-bottom: 1.5rem;
    }

    .sim-slot {
      aspect-ratio: 1/1;
      background: rgba(0,0,0,0.3);
      border: 2px solid rgba(58,32,40,0.4);
      border-radius: 8px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      transition: all 0.3s;
      min-height: 64px;
    }

    .sim-slot .slot-label {
      font-size: 0.6rem;
      color: #554444;
      text-align: center;
      line-height: 1.3;
      pointer-events: none;
    }

    .sim-slot .slot-icon {
      font-size: 1.2rem;
      margin-bottom: 0.2rem;
      opacity: 0.4;
    }

    .sim-slot.filled {
      border-color: rgba(218,165,32,0.3);
      background: rgba(139,0,0,0.15);
    }

    .sim-slot.filled .slot-label { color: var(--gold); }
    .sim-slot.filled .slot-icon { opacity: 0.8; }

    .sim-buttons {
      display: flex;
      gap: 1rem;
      margin-bottom: 1.5rem;
    }

    .sim-btn {
      flex: 1;
      padding: 0.7rem 1rem;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 600;
      transition: all 0.2s;
      border: 1px solid rgba(58,32,40,0.5);
      background: rgba(26,15,20,0.8);
      color: #b0a098;
      cursor: pointer;
      text-align: center;
    }

    .sim-btn:hover {
      transform: translateY(-1px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }

    .sim-btn.clear {
      background: linear-gradient(135deg, rgba(139,0,0,0.2), rgba(218,165,32,0.15));
      border-color: var(--gold-dim);
      color: var(--gold);
    }

    .sim-btn.transmute {
      background: linear-gradient(135deg, rgba(0,80,0,0.2), rgba(46,139,87,0.15));
      border-color: rgba(46,139,87,0.4);
      color: #5ab87a;
    }

    .sim-btn.transmute:hover {
      background: linear-gradient(135deg, rgba(0,100,0,0.25), rgba(46,139,87,0.2));
    }

""", "")

content = content.replace("""    @media (max-width: 600px) {
      .sim-cube-grid { gap: 0.5rem; }
      .sim-slot { min-height: 48px; }
      .sim-slot .slot-label { font-size: 0.5rem; }
    }""", "")

# Add the .sim-section-label CSS
content = content.replace("""    .sim-recipe-title {""", """    .sim-section-label {
      font-size: 0.85rem;
      color: var(--gold);
      font-weight: 600;
      margin: 1rem 0 0.5rem;
      padding-bottom: 0.35rem;
      border-bottom: 1px solid rgba(58,32,40,0.3);
    }
    .sim-recipe-title {""")

# Remove unused JS references (simClearBtn, simTransmuteBtn, simCubeGrid)
# Also update nav - remove unlock from nav
old_nav = """      <li><a href="#sec-hero" class="active"><span class="nav-icon">&#x1F3E0;</span><span class="nav-text">封面与配方总览</span><span class="nav-step">TOP</span></a></li>
      <li><a href="#sec-unlock"><span class="nav-icon">&#x1F513;</span><span class="nav-text">解锁流程</span><span class="nav-step">CH 1</span></a></li>
      <li><a href="#sec-mechanics"><span class="nav-icon">&#x2699;</span><span class="nav-text">核心机制详解</span><span class="nav-step">CH 2</span></a></li>"""
new_nav = """      <li><a href="#sec-hero" class="active"><span class="nav-icon">&#x1F3E0;</span><span class="nav-text">封面与配方总览</span><span class="nav-step">TOP</span></a></li>
      <li><a href="#sec-mechanics"><span class="nav-icon">&#x2699;</span><span class="nav-text">核心机制详解</span><span class="nav-step">CH 1</span></a></li>"""
if old_nav in content:
    content = content.replace(old_nav, new_nav)
    print("Nav updated: removed unlock, renumbered")
else:
    print("WARNING: nav update failed")

# Update section numbering for CH 3->2, etc
content = content.replace('<span class="nav-step">CH 3</span>', '<span class="nav-step">CH 2</span>')
content = content.replace('<span class="nav-step">CH 4</span>', '<span class="nav-step">CH 3</span>')
content = content.replace('<span class="nav-step">CH 5</span>', '<span class="nav-step">CH 4</span>')
content = content.replace('<span class="nav-step">CH 6</span>', '<span class="nav-step">CH 5</span>')
print("Nav renumbered")

# Clean up JS references to removed elements
content = content.replace("""    const cB = document.getElementById('simClearBtn');
    const tB = document.getElementById('simTransmuteBtn');""", "")
content = content.replace("""    function clrS() { cs.forEach(function(s) { s.className = 'sim-slot'; s.querySelector('.slot-icon').innerHTML = '&#x25A1;'; s.querySelector('.slot-label').textContent = '空位'; }); }
    tB.addEventListener('click', function() { if (curR) { alert('"' + curR.name + '"配方已模拟执行！\n请在游戏内使用实际材料操作。'); } else { alert('请先在右侧配方列表中选择一个配方。'); } });
    cB.addEventListener('click', clrS);""", "")
content = content.replace("""    const cs = document.querySelectorAll('#simCubeGrid .sim-slot');
    const simDetail = document.getElementById('simDetail');""", """    const simDetail = document.getElementById('simDetail');""")

# Remove upS and updateSlots since we no longer have slots
# But keep the selectRecipe function clean
# Remove slot update related code
old_upS = """    function upS(r) {
      cs.forEach(function(s, i) {
        var l = s.querySelector('.slot-label'), ic = s.querySelector('.slot-icon');
        var f = r.slots && r.slots[i];
        if (f) { s.className = 'sim-slot filled'; ic.innerHTML = '&#x1F4E6;'; l.textContent = f; }
        else { s.className = 'sim-slot'; ic.innerHTML = '&#x25A1;'; l.textContent = '空位'; }
      });
    }
    """
content = content.replace(old_upS, "")

old_selR = """    function selR(r) {
      curR = r;
      document.querySelectorAll('.sim-r-item').forEach(function(e) { e.classList.remove('active'); });
      var t = document.querySelector('.sim-r-item[data-id="' + r.id + '"]'); if (t) t.classList.add('active');
      srT.textContent = r.name; srE.textContent = r.descEn; srD.textContent = r.desc; sC.textContent = '配方 #' + r.order;
      sM.innerHTML = '';
      r.materials.forEach(function(m) { var li = document.createElement('li'); li.innerHTML = '<span>' + (m.icon || '') + '</span> ' + m.name + ' x' + m.qty; sM.appendChild(li); });
      if (r.warning) { sW.style.display = 'block'; sW.innerHTML = '<div class="sim-warning"><span>&#x26A0;&#xFE0F;</span><p>' + r.warning + '</p></div>'; }
      else { sW.style.display = 'none'; }
      upS(r);
    }"""

new_selR = """    function selR(r) {
      curR = r;
      document.querySelectorAll('.sim-r-item').forEach(function(e) { e.classList.remove('active'); });
      var t = document.querySelector('.sim-r-item[data-id="' + r.id + '"]'); if (t) t.classList.add('active');
      srT.textContent = r.name; srE.textContent = r.descEn; srD.textContent = r.desc; sC.textContent = '配方 #' + r.order;
      sM.innerHTML = '';
      r.materials.forEach(function(m) { var li = document.createElement('li'); li.innerHTML = '<span>' + (m.icon || '') + '</span> ' + m.name + ' x' + m.qty; sM.appendChild(li); });
      if (r.warning) { sW.style.display = 'block'; sW.innerHTML = '<div class="sim-warning"><span>&#x26A0;&#xFE0F;</span><p>' + r.warning + '</p></div>'; }
      else { sW.style.display = 'none'; }
    }"""

if old_selR in content:
    content = content.replace(old_selR, new_selR)
    print("JS cleanup done: removed slot/button refs")
else:
    print("WARNING: selR update failed")

# Update the sim description for text area (id="simRecipeDesc")
# Make the desc show a placeholder initially if empty
content = content.replace('<div class="sim-recipe-desc" id="simRecipeDesc"></div>', '<div class="sim-recipe-desc" id="simRecipeDesc">请选择右侧配方查看详情</div>')

with open('games/diablo4/horadric-cube-guide.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("\nALL CHANGES COMPLETE!")
