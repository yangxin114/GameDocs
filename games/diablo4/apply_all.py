with open('games/diablo4/horadric-cube-guide.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# PART A: Add simulator CSS (before </style>)
# ============================================================
sim_css = '''
    /* ===== Horadric Cube Simulator Styles ===== */
    .sim-layout {
      display: flex;
      gap: 2rem;
      align-items: flex-start;
    }

    .sim-panel {
      flex: 1;
      background: rgba(26,15,20,0.85);
      border: 1px solid rgba(58,32,40,0.5);
      border-radius: 14px;
      overflow: hidden;
    }

    .sim-panel-header {
      padding: 1.25rem 1.5rem;
      background: rgba(139,0,0,0.08);
      border-bottom: 1px solid rgba(58,32,40,0.4);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .sim-panel-title {
      font-family: 'Cinzel', serif;
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--gold);
    }

    .sim-panel-body { padding: 1.5rem; }

    .sim-detail {
      min-height: 200px;
    }

    .sim-recipe-title {
      font-family: 'Cinzel', serif;
      font-size: 1.05rem;
      font-weight: 600;
      color: #f0e8e0;
      margin-bottom: 0.75rem;
    }

    .sim-recipe-desc {
      color: #b0a098;
      font-size: 0.85rem;
      line-height: 1.8;
      margin-bottom: 1rem;
    }

    .sim-recipe-desc-en {
      font-style: italic;
      color: #665555;
      font-size: 0.8rem;
      line-height: 1.7;
      padding: 0.65rem 1rem;
      background: rgba(0,0,0,0.2);
      border-left: 3px solid var(--gold-dim);
      border-radius: 0 8px 8px 0;
      margin-bottom: 1rem;
    }

    .sim-section-label {
      font-size: 0.85rem;
      color: var(--gold);
      font-weight: 600;
      margin: 1rem 0 0.5rem;
      padding-bottom: 0.35rem;
      border-bottom: 1px solid rgba(58,32,40,0.3);
    }

    .sim-materials {
      list-style: none;
      padding: 0;
      margin: 0 0 1rem;
    }

    .sim-materials li {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.35rem 0;
      font-size: 0.82rem;
      color: #b0a098;
      border-bottom: 1px solid rgba(58,32,40,0.2);
    }

    .sim-materials li:last-child { border-bottom: none; }

    .sim-warning {
      display: flex;
      align-items: flex-start;
      gap: 0.5rem;
      padding: 0.65rem 1rem;
      background: rgba(231,76,60,0.08);
      border: 1px solid rgba(231,76,60,0.25);
      border-radius: 8px;
      margin-top: 0.75rem;
    }

    .sim-warning p {
      font-size: 0.8rem;
      color: #e07060;
      line-height: 1.6;
      margin: 0;
    }

    .sim-recipes {
      width: 320px;
      flex-shrink: 0;
      background: rgba(26,15,20,0.85);
      border: 1px solid rgba(58,32,40,0.5);
      border-radius: 14px;
      overflow: hidden;
      max-height: 700px;
      display: flex;
      flex-direction: column;
    }

    .sim-recipes-header {
      padding: 1rem 1.25rem;
      background: rgba(139,0,0,0.08);
      border-bottom: 1px solid rgba(58,32,40,0.4);
      font-family: 'Cinzel', serif;
      font-size: 1rem;
      font-weight: 600;
      color: var(--gold);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .sim-recipes-list {
      flex: 1;
      overflow-y: auto;
    }

    .sim-recipes-list::-webkit-scrollbar { width: 4px; }
    .sim-recipes-list::-webkit-scrollbar-track { background: transparent; }
    .sim-recipes-list::-webkit-scrollbar-thumb { background: rgba(58,32,40,0.5); border-radius: 2px; }

    .sim-cat {
      padding: 0.65rem 1.25rem;
      background: rgba(139,0,0,0.05);
      font-weight: 600;
      color: #f0e8e0;
      font-size: 0.8rem;
      letter-spacing: 0.5px;
      border-bottom: 1px solid rgba(58,32,40,0.2);
    }

    .sim-r-item {
      padding: 0.85rem 1.25rem;
      border-bottom: 1px solid rgba(58,32,40,0.2);
      cursor: pointer;
      transition: all 0.2s;
    }

    .sim-r-item:hover {
      background: rgba(218,165,32,0.05);
      border-left: 3px solid var(--gold-dim);
    }

    .sim-r-item.active {
      background: rgba(218,165,32,0.1);
      border-left: 3px solid var(--gold);
    }

    .sim-r-item .r-name {
      font-size: 0.85rem;
      font-weight: 600;
      color: #f0e8e0;
    }

    @media (max-width: 1024px) {
      .sim-layout { flex-direction: column; }
      .sim-recipes { width: 100%; max-height: none; }
    }
'''

# Insert before </style>
content = content.replace('</style>', sim_css + '\n  </style>')
print("A: CSS added")

# ============================================================
# PART B: Replace old recipe sections with simulator HTML
# ============================================================
# Find the start and end markers
start_marker = '      <!-- ====== 装备改造配方 ====== -->'
end_marker = '      <!-- ====== 实战打造流程 ====== -->'

start_idx = content.index(start_marker)
end_idx = content.index(end_marker)

simulator_html = '''      <!-- ====== 魔盒配方模拟器 ====== -->
      <section class="cube-section cube-simulator" id="sec-simulator">
        <h2 class="cube-section-title"><span class="sec-icon">&#x1F52E;</span> 魔盒配方模拟器</h2>
        <p class="cube-section-desc">点击右侧配方查看详情，左侧展示配方的说明、材料与实践信息。共收录 <strong style="color:var(--gold)">22 个配方</strong>，涵盖装备改造、物品塑形、符文制作三大类。</p>

        <div class="sim-layout">
          <!-- Left Panel -->
          <div class="sim-panel">
            <div class="sim-panel-header">
              <span class="sim-panel-title">赫拉迪姆魔盒</span>
              <span style="font-size:0.75rem;color:#665555;" id="simRecipeCount">配方 #1</span>
            </div>
            <div class="sim-panel-body">
              <div class="sim-detail" id="simDetail">
                <div class="sim-recipe-title" id="simRecipeTitle">添加词缀</div>
                <div class="sim-recipe-desc-en" id="simRecipeDescEn">Adds a random Affix to an Item.</div>
                <div class="sim-section-label">配方说明</div>
                <div class="sim-recipe-desc" id="simRecipeDesc">请选择右侧配方查看详情</div>
                <div class="sim-section-label">所需材料</div>
                <ul class="sim-materials" id="simMaterials">
                  <li>请选择右侧配方查看详情</li>
                </ul>
                <div id="simWarning" style="display:none;"></div>
              </div>
            </div>
          </div>

          <!-- Right Panel -->
          <div class="sim-recipes">
            <div class="sim-recipes-header">
              配方列表
              <span style="font-size:0.65rem;color:#554444;margin-left:auto;">22个配方</span>
            </div>
            <div class="sim-recipes-list" id="simRecipeList"></div>
          </div>
        </div>
      </section>'''

content = content[:start_idx] + simulator_html + content[end_idx:]
print("B: Simulator HTML inserted")

# ============================================================
# PART C: Add simulator JS
# ============================================================
sim_js = '''  <script>
    // ===== Horadric Cube Simulator =====
    const recipeData = [
      { id: 'add-affix', order: 1, category: '装备改造', name: '添加词缀', descEn: 'Adds a random Affix to an Item.', desc: '为物品添加一条随机词缀。使用调谐棱镜可缩小词缀类别范围。', materials: [{ name: '普通/魔法/稀有/传奇 物品', qty: '1件', icon: '&#x1F4E6;' }, { name: '粗糙原初之尘', qty: '1', icon: '&#x2B50;' }, { name: '原始原初之尘', qty: '5', icon: '&#x2B50;' }, { name: '调谐棱镜', qty: '（可选）', icon: '&#x1F52E;' }], practice: '将底材和材料放入魔盒，点击重塑即可添加一条随机词缀。使用调谐棱镜可定向选择词缀类别。' },
      { id: 'chaotic-reroll', order: 2, category: '装备改造', name: '随机重洗', descEn: 'Changes a random Affix to another Category.', desc: '将一条随机词缀更改为另一类别的词缀。', materials: [{ name: '魔法/稀有/传奇 物品', qty: '1件', icon: '&#x1F4E6;' }, { name: '精炼原初之尘', qty: '1', icon: '&#x2B50;' }, { name: '原始原初之尘', qty: '15', icon: '&#x2B50;' }, { name: '调谐棱镜', qty: '（可选）', icon: '&#x1F52E;' }], practice: '随机性高，适合词缀数量多但不满意的情况。配合棱镜使用可缩小范围。' },
      { id: 'focused-reroll', order: 3, category: '装备改造', name: '定向重洗', descEn: 'Changes an Affix to one of the same Category.', desc: '将一条词缀更改为同一类别的另一词缀。必须使用调谐棱镜。', materials: [{ name: '魔法/稀有/传奇 物品', qty: '1件', icon: '&#x1F4E6;' }, { name: '精炼原初之尘', qty: '1', icon: '&#x2B50;' }, { name: '原始原初之尘', qty: '15', icon: '&#x2B50;' }, { name: '调谐棱镜', qty: '1块（必选）', icon: '&#x1F52E;' }], practice: '毕业装备修正的首选。放入与废词缀同类的棱镜，精准替换，零风险。' },
      { id: 'remove-affix', order: 4, category: '装备改造', name: '移除词缀', descEn: 'Removes a random Affix from an Item.', desc: '从物品上移除一条随机词缀。', materials: [{ name: '魔法或稀有 物品', qty: '1件', icon: '&#x1F4E6;' }, { name: '精炼原初之尘', qty: '1', icon: '&#x2B50;' }, { name: '原始原初之尘', qty: '15', icon: '&#x2B50;' }, { name: '调谐棱镜', qty: '（可选）', icon: '&#x1F52E;' }], practice: '随机移除一条词缀。建议在词缀数多于目标数时使用，配合棱镜控制移除范围。' },
      { id: 'transfigure', order: 5, category: '装备改造', name: '嬗变物品', descEn: 'Grants a random modification of great possibilities!', desc: '赋予物品极具可能性的随机改造。', materials: [{ name: '传奇/暗金/神话 物品', qty: '1件', icon: '&#x1F4E6;' }, { name: '不稳定原初之尘', qty: '1', icon: '&#x2B50;' }, { name: '调谐棱镜', qty: '（可选）', icon: '&#x1F52E;' }], practice: '高风险高回报。物品有极高几率变为不可修改状态。仅作为最后手段使用。', warning: '变形后物品有极高几率变为不可再修改状态（Unmodifiable）。请慎重使用！' },
      { id: 'unique-power', order: 6, category: '装备改造', name: '重置暗金威能', descEn: 'Randomizes the Unique Power value on an Ancestral Unique.', desc: '随机重铸先祖独特物品上独特威能的数值。', materials: [{ name: '先祖暗金 物品', qty: '1件', icon: '&#x1F4E6;' }, { name: '调和原初之尘', qty: '1', icon: '&#x2B50;' }, { name: '原始原初之尘', qty: '100', icon: '&#x2B50;' }], practice: '不会改变词缀，只重Roll底部的传奇特效数值。完美保护你现有的词缀组合。' },
      { id: 'three-to-one', order: 7, category: '物品塑形', name: '三合一塑形', descEn: '3 of the same type into 1 random new item.', desc: '将3件相同类型的装备/护身符/符文转化为一件随机新物品。', materials: [{ name: '同类型物品', qty: '3件', icon: '&#x1F4E6;' }], practice: '处理多余装备的最基础方法。不看具体名称，只看稀有度，是凑套装的重要来源。' },
      { id: 'recycle-uniques', order: 8, category: '物品塑形', name: '回收暗金', descEn: '3 of the same Unique into a new version.', desc: '将3件相同暗金装备或护身符转化为该暗金的新版本。', materials: [{ name: '相同的暗金物品', qty: '3件', icon: '&#x1F4E6;' }], practice: '重复暗金的好出路，有机会获得更高roll值的同件暗金。' },
      { id: 'upgrade-unique', order: 9, category: '物品塑形', name: '升级为暗金', descEn: 'Common item into a random Unique of the same type.', desc: '将普通装备转化为同类型随机暗金装备。', materials: [{ name: '普通物品', qty: '1件', icon: '&#x1F4E6;' }, { name: '强化原初之尘', qty: '1', icon: '&#x2B50;' }, { name: '原始原初之尘', qty: '10', icon: '&#x2B50;' }], practice: '低成本搏高回报。白色底材越高级，出好暗金的概率越大。' },
      { id: 'upgrade-legendary', order: 10, category: '装备改造', name: '升级至传奇', descEn: 'Rare item into a Legendary with a random power.', desc: '将稀有装备转化为带有随机传奇威能的传奇物品。', materials: [{ name: '稀有物品', qty: '1件', icon: '&#x1F4E6;' }, { name: '纯净原初之尘', qty: '1', icon: '&#x2B50;' }, { name: '原始原初之尘', qty: '10', icon: '&#x2B50;' }, { name: '调谐棱镜', qty: '（可选）', icon: '&#x1F52E;' }], practice: '词缀转化核心。稀有→传奇保留词缀并赋予随机威能，配合棱镜可控制威能类别。' },
      { id: 'reroll-set-charm', order: 11, category: '装备改造', name: '重置套装神符', descEn: 'Set Charm into a different Charm from the same Set.', desc: '将套装护身符转化为同一套装中的另一件。', materials: [{ name: '套装神符', qty: '1枚', icon: '&#x1F48E;' }, { name: '原始原初之尘', qty: '25', icon: '&#x2B50;' }, { name: '注能赫拉迪姆树脂', qty: '50', icon: '&#x1F9EA;' }], practice: '将重复的符咒转化为紧缺部位，快速解锁多套装特效。' },
      { id: 'craft-unique-charm', order: 12, category: '装备改造', name: '制作暗金神符', descEn: 'Unique equipment into a Unique Charm.', desc: '将独特装备转化为独特护身符。', materials: [{ name: '先祖暗金物品', qty: '1件', icon: '&#x1F4E6;' }, { name: '任意暗金神符', qty: '3枚', icon: '&#x1F48E;' }, { name: '强化原初之尘', qty: '1', icon: '&#x2B50;' }, { name: '原始原初之尘', qty: '50', icon: '&#x2B50;' }, { name: '注能赫拉迪姆树脂', qty: '100', icon: '&#x1F9EA;' }], practice: '暗金装备威能→可镶嵌神符。解放装备位，让核心威能变成可携带的护身符。' },
      { id: 'amalgamation', order: 13, category: '装备改造', name: '融合', descEn: 'Multiple items of the same type to upgrade.', desc: '重塑多个同类型物品以升级。', materials: [{ name: '可组合物品', qty: '多个', icon: '&#x1F4E6;' }], practice: '仅限部分消耗品、镶嵌物以及地下城钥匙。将低级材料合成为高级材料。' },
      { id: 'ritual-rune-bac', order: 14, category: '符文制作', name: '仪祭符文：跋', descEn: 'Craft Bac - a Ritual Rune.', desc: '制作仪祭符文。', materials: [{ name: '普瑞德', qty: '1', icon: '&#x2728;' }, { name: '任意稀有符文', qty: '5枚', icon: '&#x2728;' }, { name: '传奇祈告符文', qty: '5枚', icon: '&#x2728;' }], practice: '消耗基础符文和传奇符文，定向制作指定仪祭符文。' },
      { id: 'ritual-rune-igni', order: 15, category: '符文制作', name: '仪祭符文：伊格尼', descEn: 'Craft Igni - a Ritual Rune.', desc: '制作仪祭符文。', materials: [{ name: '泰布', qty: '1', icon: '&#x2728;' }, { name: '任意稀有符文', qty: '5枚', icon: '&#x2728;' }, { name: '传奇祈告符文', qty: '5枚', icon: '&#x2728;' }], practice: '消耗基础符文和传奇符文，定向制作指定仪祭符文。' },
      { id: 'ritual-rune-tam', order: 16, category: '符文制作', name: '仪祭符文：塔姆', descEn: 'Craft Tam - a Ritual Rune.', desc: '制作仪祭符文。', materials: [{ name: '讷尔', qty: '1', icon: '&#x2728;' }, { name: '任意稀有符文', qty: '5枚', icon: '&#x2728;' }, { name: '传奇祈告符文', qty: '5枚', icon: '&#x2728;' }], practice: '消耗基础符文和传奇符文，定向制作指定仪祭符文。' },
      { id: 'ritual-rune-yul', order: 17, category: '符文制作', name: '仪祭符文：尤尔', descEn: 'Craft Yul - a Ritual Rune.', desc: '制作仪祭符文。', materials: [{ name: '乌尔', qty: '1', icon: '&#x2728;' }, { name: '任意稀有符文', qty: '5枚', icon: '&#x2728;' }, { name: '传奇祈告符文', qty: '5枚', icon: '&#x2728;' }], practice: '消耗基础符文和传奇符文，定向制作指定仪祭符文。' },
      { id: 'summon-rune-eom', order: 18, category: '符文制作', name: '祈告符文：伊欧姆', descEn: 'Craft Eom - a Summon Rune.', desc: '制作祈告符文。', materials: [{ name: '兹克', qty: '1', icon: '&#x2728;' }, { name: '任意稀有符文', qty: '5枚', icon: '&#x2728;' }, { name: '传奇仪祭符文', qty: '5枚', icon: '&#x2728;' }], practice: '消耗基础符文和传奇符文，定向制作指定祈告符文。' },
      { id: 'summon-rune-ja', order: 19, category: '符文制作', name: '祈告符文：扎', descEn: 'Craft Ja - a Summon Rune.', desc: '制作祈告符文。', materials: [{ name: '杰姆', qty: '1', icon: '&#x2728;' }, { name: '任意稀有符文', qty: '5枚', icon: '&#x2728;' }, { name: '传奇仪祭符文', qty: '5枚', icon: '&#x2728;' }], practice: '消耗基础符文和传奇符文，定向制作指定祈告符文。' },
      { id: 'summon-rune-om', order: 20, category: '符文制作', name: '祈告符文：奥姆', descEn: 'Craft Ohm - a Summon Rune.', desc: '制作祈告符文。', materials: [{ name: '夸', qty: '1', icon: '&#x2728;' }, { name: '任意稀有符文', qty: '5枚', icon: '&#x2728;' }, { name: '传奇仪祭符文', qty: '5枚', icon: '&#x2728;' }], practice: '消耗基础符文和传奇符文，定向制作指定祈告符文。' },
      { id: 'summon-rune-wicks', order: 21, category: '符文制作', name: '祈告符文：威克斯', descEn: 'Craft Wix - a Summon Rune.', desc: '制作祈告符文。', materials: [{ name: '加尔', qty: '1', icon: '&#x2728;' }, { name: '任意稀有符文', qty: '5枚', icon: '&#x2728;' }, { name: '传奇仪祭符文', qty: '5枚', icon: '&#x2728;' }], practice: '消耗基础符文和传奇符文，定向制作指定祈告符文。' },
      { id: 'summon-rune-jom', order: 22, category: '符文制作', name: '祈告符文：约姆', descEn: 'Craft Jom - a Summon Rune.', desc: '制作祈告符文。', materials: [{ name: '克莱', qty: '1', icon: '&#x2728;' }, { name: '任意稀有符文', qty: '5枚', icon: '&#x2728;' }, { name: '传奇仪祭符文', qty: '5枚', icon: '&#x2728;' }], practice: '消耗基础符文和传奇符文，定向制作指定祈告符文。' }
    ];

    const rl = document.getElementById('simRecipeList');
    const srT = document.getElementById('simRecipeTitle');
    const srE = document.getElementById('simRecipeDescEn');
    const srD = document.getElementById('simRecipeDesc');
    const sM = document.getElementById('simMaterials');
    const sW = document.getElementById('simWarning');
    const sC = document.getElementById('simRecipeCount');
    var cats = {};
    recipeData.forEach(function(r) { if (!cats[r.category]) cats[r.category] = []; cats[r.category].push(r); });
    Object.keys(cats).forEach(function(cat) {
      var d = document.createElement('div'); d.className = 'sim-cat'; d.textContent = cat; rl.appendChild(d);
      cats[cat].forEach(function(r) {
        var i = document.createElement('div'); i.className = 'sim-r-item'; i.dataset.id = r.id;
        i.innerHTML = '<div class="r-name">' + r.name + '</div>';
        i.addEventListener('click', function() { selR(r); }); rl.appendChild(i);
      });
    });
    var curR = null;
    function selR(r) {
      curR = r;
      document.querySelectorAll('.sim-r-item').forEach(function(e) { e.classList.remove('active'); });
      var t = document.querySelector('.sim-r-item[data-id="' + r.id + '"]'); if (t) t.classList.add('active');
      srT.textContent = r.name; srE.textContent = r.descEn; srD.textContent = r.desc; sC.textContent = '配方 #' + r.order;
      sM.innerHTML = '';
      r.materials.forEach(function(m) { var li = document.createElement('li'); li.innerHTML = '<span>' + (m.icon || '') + '</span> ' + m.name + ' x' + m.qty; sM.appendChild(li); });
      if (r.warning) { sW.style.display = 'block'; sW.innerHTML = '<div class="sim-warning"><span>&#x26A0;&#xFE0F;</span><p>' + r.warning + '</p></div>'; }
      else { sW.style.display = 'none'; }
    }
    if (recipeData.length > 0) { selR(recipeData[0]); }
  </script>
'''

content = content.replace('<script src="../../assets/js/guide-sidebar.js"></script>', sim_js + '\n  <script src="../../assets/js/guide-sidebar.js"></script>')
print("C: Simulator JS added")

# ============================================================
# PART D: Rename "魔方" → "魔盒" in visible text
# ============================================================
lines = content.split('\n')
new_lines = []
for line in lines:
    if 'href=' in line or 'src=' in line or 'data-' in line:
        new_lines.append(line)
    else:
        new_lines.append(line.replace('魔方', '魔盒'))
content = '\n'.join(new_lines)
print("D: 魔方→魔盒")

# ============================================================
# PART E: Remove "配方分类一览" table
# ============================================================
marker = '<h3 style="font-family:\'Cinzel\',serif;font-size:1rem;color:#f0e8e0;margin-bottom:1rem;">配方分类一览</h3>'
if marker in content:
    s = content.index(marker)
    e = content.index('</section>\n</section>', s + len(marker)) + len('</section>\n</section>')
    content = content[:s] + content[e:]
    print("E: Removed 配方分类一览 table")

# ============================================================
# PART F: Move unlock section to QA end
# ============================================================
u_start = content.index('<!-- ====== 解锁流程 ====== -->')
u_end = content.index('<!-- ====== 核心机制详解 ====== -->')
unlock_html = content[u_start:u_end]
content = content[:u_start] + content[u_end:]

qa_marker = '<!-- 护身符终极配置 -->'
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
print("F: Unlock moved to QA")

# ============================================================
# PART G: Update nav (remove unlock, renumber)
# ============================================================
old_nav = """      <li><a href="#sec-hero" class="active"><span class="nav-icon">&#x1F3E0;</span><span class="nav-text">封面与配方总览</span><span class="nav-step">TOP</span></a></li>
      <li><a href="#sec-unlock"><span class="nav-icon">&#x1F513;</span><span class="nav-text">解锁流程</span><span class="nav-step">CH 1</span></a></li>
      <li><a href="#sec-mechanics"><span class="nav-icon">&#x2699;</span><span class="nav-text">核心机制详解</span><span class="nav-step">CH 2</span></a></li>"""
new_nav = """      <li><a href="#sec-hero" class="active"><span class="nav-icon">&#x1F3E0;</span><span class="nav-text">封面与配方总览</span><span class="nav-step">TOP</span></a></li>
      <li><a href="#sec-mechanics"><span class="nav-icon">&#x2699;</span><span class="nav-text">核心机制详解</span><span class="nav-step">CH 1</span></a></li>"""
content = content.replace(old_nav, new_nav)

# Renumber: CH 3->2, CH 4->3, CH 5->4, CH 6->5
content = content.replace('<span class="nav-step">CH 3</span>', '<span class="nav-step">CH 2</span>')
content = content.replace('<span class="nav-step">CH 4</span>', '<span class="nav-step">CH 3</span>')
content = content.replace('<span class="nav-step">CH 5</span>', '<span class="nav-step">CH 4</span>')
content = content.replace('<span class="nav-step">CH 6</span>', '<span class="nav-step">CH 5</span>')
print("G: Nav updated")

with open('games/diablo4/horadric-cube-guide.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("\nALL DONE!")
