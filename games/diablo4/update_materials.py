import json

with open('assets/js/horadric-cube-materials.json', 'r', encoding='utf-8') as f:
    materials = json.load(f)

base_img = '../../assets/images/diablo4/dlc2/horadric_cube/'

prism_map = {
    "娴熟调谐棱柱": "技能/核心棱镜",
    "侵略调谐棱柱": "攻击棱镜",
    "保护调谐棱柱": "防御棱镜",
    "多彩调谐棱柱": "抗性棱镜",
    "实用调谐棱柱": "机动/通用棱镜",
    "资源调谐棱柱": "资源棱镜"
}

prism_cards = []
for m in materials:
    name = m["name"]
    if "棱柱" not in name or name in ("熵能调谐棱柱", "库勒调谐棱柱"):
        continue
    icon_file = name + "-图标.png"
    common_name = prism_map.get(name, name.replace("调谐棱柱", ""))
    prism_cards.append(f'<div class="prism-card"><img src="{base_img}{icon_file}" alt="{name}" class="mat-icon-img"><div><div class="prism-name">{common_name}</div><div class="prism-examples">{m["description"]}</div></div></div>')

prism_html = '          <div class="prism-grid">\n' + '\n'.join(prism_cards) + '\n          </div>'

with open('games/diablo4/horadric-cube-guide.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace prism grid
import re
old_start = '          <div class="prism-grid">\n            <div class="prism-card">\n              <div class="prism-name">'
old_end = '          </div>\n\n          <div class="content-block">\n            <p><strong>'
s1 = html.index(old_start)
e1 = html.index(old_end, s1)
new_prism_full = prism_html + '\n\n          <div class="content-block">\n            <p><strong>主要获取途径：</strong>最稳定的来源是<strong>"战争计划"系统</strong>及折磨难度以上的终局活动。急需某一类棱镜时，可关注<strong>低语古树</strong>的棱镜宝匣赠礼，或参加<strong>军团入侵事件</strong>。</p>\n          </div>'
html = html[:s1] + new_prism_full + html[e1:]
print("Prism grid replaced")

# Replace material grid
mat_order = ["粗制的源生粉尘", "原始的源生粉尘", "精炼的源生粉尘", "纯净的源生粉尘", "强化的源生粉尘", "同调的源生粉尘", "不稳定的源生粉尘", "注能赫拉迪姆树脂"]
rarity_colors = {"魔法": "#4a9eff", "稀有": "#27ae60", "传奇": "#8e44ad", "暗金": "#daa520"}
mat_cards = []
for name in mat_order:
    m = next((x for x in materials if x["name"] == name), None)
    if not m: continue
    icon_file = name + "-图标.png"
    if name == "不稳定的源生粉尘": icon_file = "不稳的源生粉尘-图标.png"
    elif name == "注能赫拉迪姆树脂": icon_file = "注能的赫拉迪姆树脂-图标.png"
    rarity = m.get("rarity", "")
    color = rarity_colors.get(rarity, "#8a7a70")
    sources = m.get("sources", [])
    sources_text = "获取: " + " / ".join(sources[:2])
    mat_cards.append(f'<div class="mat-card" data-rarity="{rarity}"><img src="{base_img}{icon_file}" alt="{name}" class="mat-card-icon"><div><div class="mat-card-header"><div class="mat-name">{name}</div><span class="mat-rarity" style="color:{color}">{rarity}</span></div><div class="mat-name-zh">{m.get("usage", "")}</div><div class="mat-use">{m["description"]}</div><div class="mat-sources">{sources_text}</div></div></div>')

mat_grid_html = '          <div class="mat-grid">\n' + '\n'.join(mat_cards) + '\n          </div>'

old_mat_s = '          <div class="mat-grid">\n            <div class="mat-card">\n              <div class="mat-name">'
old_mat_e = '          </div>\n        </div>\n      </section>\n\n      <!-- ====== 魔盒配方大全 ====== -->'
s2 = html.index(old_mat_s)
e2 = html.index(old_mat_e)
html = html[:s2] + mat_grid_html + html[e2:]
print("Material grid replaced")

# Add CSS
css_block = '    .mat-icon-img { width: 36px; height: 36px; object-fit: contain; flex-shrink: 0; }\n    .prism-card { display: flex; align-items: center; gap: 0.75rem; background: rgba(26,15,20,0.7); border: 1px solid rgba(58,32,40,0.4); border-radius: 10px; padding: 0.85rem 1rem; }\n    .prism-card .mat-icon-img { width: 32px; height: 32px; }\n    .prism-card .prism-name { font-size: 0.85rem; font-weight: 600; color: var(--gold); margin-bottom: 0.15rem; }\n    .prism-card .prism-examples { font-size: 0.72rem; color: #665555; line-height: 1.4; }\n    .mat-card { display: flex; gap: 0.75rem; background: rgba(26,15,20,0.7); border: 1px solid rgba(58,32,40,0.4); border-radius: 10px; padding: 1rem; transition: all 0.2s; }\n    .mat-card:hover { border-color: rgba(218,165,32,0.3); }\n    .mat-card-icon { width: 40px; height: 40px; object-fit: contain; flex-shrink: 0; margin-top: 0.15rem; }\n    .mat-card-header { display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.15rem; }\n    .mat-card .mat-name { font-family: \'Cinzel\', serif; font-size: 0.82rem; color: var(--gold); }\n    .mat-card .mat-rarity { font-size: 0.6rem; font-weight: 600; letter-spacing: 0.5px; }\n    .mat-card .mat-name-zh { font-size: 0.75rem; color: #8a7a70; margin-bottom: 0.3rem; }\n    .mat-card .mat-use { font-size: 0.75rem; color: #665555; line-height: 1.5; margin-bottom: 0.3rem; }\n    .mat-card .mat-sources { font-size: 0.65rem; color: #4a4a3a; line-height: 1.4; }\n    .mat-card[data-rarity="暗金"] { border-color: rgba(218,165,32,0.3); }\n    .mat-card[data-rarity="传奇"] { border-color: rgba(142,68,173,0.3); }\n    .mat-card[data-rarity="稀有"] { border-color: rgba(39,174,96,0.3); }\n    .mat-card[data-rarity="魔法"] { border-color: rgba(74,158,255,0.2); }\n'
html = html.replace('\r\n', '\n')
# Find the comment and insert CSS before it
sim_marker = '    /* ===== Horadric Cube Simulator Styles ===== */'
html = html.replace(sim_marker, css_block + '\n' + sim_marker)
print("CSS added")

with open('games/diablo4/horadric-cube-guide.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("DONE!")
