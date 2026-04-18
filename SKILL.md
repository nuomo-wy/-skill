---
name: storyboard-master
description: 专业视频分镜生成与优化技能。当用户需要创建视频分镜、镜头脚本、拍摄方案，或询问镜头语言、构图技巧、运镜方式、分镜格式、好莱坞分镜、导演风格等相关问题时使用。支持广告、短片、MV、剧情片、纪录片、短视频、动画等多种视频类型的分镜创作。
---

# Storyboard Master - 分镜大师

## 概述

本技能提供专业的视频分镜知识体系，帮助AI生成结构化、可执行的分镜脚本。

## 核心能力

1. **分镜生成** - 根据创意描述生成完整分镜脚本
2. **镜头设计** - 提供镜头类型、景别、运镜方式建议
3. **格式输出** - 支持多种分镜格式（表格、脚本、可视化描述）
4. **优化建议** - 对现有分镜进行专业优化
5. **质量自检** - 生成后自动检查常见问题

## 工作流程

```
用户需求 → 需求澄清 → 视频类型判断 → 加载知识库 → 生成分镜 → 质量自检 → 格式输出
```

### 步骤1：理解需求
- 视频类型（广告/短片/MV/剧情片/纪录片/短视频/动画）
- 时长要求
- 画幅（横屏16:9 / 竖屏9:16 / 方形1:1 / 超宽2.39:1）
- 风格定位
- 关键信息点
- 目标受众
- 预算/制作条件（实拍/动画/混合）

### 步骤2：类型路由 — 加载知识库

根据视频类型**必须加载**对应参考文件：

| 视频类型 | 必须加载 | 建议加载 |
|----------|----------|----------|
| 广告 | `commercial.md` | `cinematography.md`, `transition.md` |
| 剧情短片 | `narrative.md` | `cinematography.md`, `sound_design.md` |
| MV | `mv.md` | `cinematography.md`, `transition.md`, `rhythm.md` |
| 纪录片 | `documentary.md` | `cinematography.md`, `sound_design.md` |
| 短视频/竖屏 | `short_video.md` | `transition.md` |
| 动画 | `animation.md` | `cinematography.md`, `transition.md` |
| 好莱坞/长片 | `hollywood.md` | `cinematography.md`, `sound_design.md`, `rhythm.md` |

**通用加载**（所有类型都建议参考）：
- `format.md` — 格式规范
- `tools_and_terms.md` — 术语参考

**专题加载**（按需）：
- 转场设计 → `transition.md`
- 声音叙事 → `sound_design.md`
- 色彩情绪 → `color_mood.md`
- 节奏控制 → `rhythm.md`

### 步骤3：生成分镜
1. 确定镜头数量（参考 format.md 时长分配）
2. 规划情绪曲线/叙事弧线
3. 逐镜头设计（景别/机位/运镜/画面/声音/转场）
4. 标注色彩/影调方向
5. 检查轴线/视线匹配

### 步骤4：质量自检（生成后必须执行）

**叙事检查**：
- [ ] 每个镜头服务故事？
- [ ] 前3秒/开场抓住注意力？
- [ ] 情绪曲线有起伏？
- [ ] 结尾有记忆点？

**技术检查**：
- [ ] 轴线原则是否遵守？
- [ ] 视线方向是否匹配？
- [ ] 景别变化是否有逻辑（避免跳跃过大）？
- [ ] 转场是否自然？
- [ ] 声音设计是否完整（对白/音效/音乐/静默）？

**类型专项检查**（按类型加载）：
- 广告：产品3秒内出现？CTA明确？
- 短视频：前3秒钩子？无声可看？
- 动画：关键姿势标注？口型同步？
- 纪录片：采访+空镜比例？旁白节奏？

### 步骤5：格式输出
根据受众选择输出格式，详见 `format.md`。

## 分镜要素

### 标准镜头要素
| 要素 | 说明 | 必填 |
|------|------|------|
| 镜号 | 顺序编号 | ✅ |
| 景别 | 远/全/中/近/特 | ✅ |
| 机位 | 拍摄角度与高度 | ✅ |
| 运镜 | 固定/推/拉/摇/移/跟/升降 | ✅ |
| 画面内容 | 主体动作、构图描述 | ✅ |
| 时长 | 秒数 | ✅ |
| 转场 | 与上一镜头的衔接方式 | ✅ |
| 声音 | 对白、音效，音乐标注 | ✅ |
| 色彩/影调 | 暖调/冷调/高调/低调 | 建议填 |
| 备注 | 特殊要求 | 按需 |

### 动画附加要素
| 要素 | 说明 |
|------|------|
| 关键姿势 | KEY/BRK/INB 标注 |
| 口型同步 | 发音口型序列 |
| 动作线 | 运动轨迹 |

## 输出格式

### 格式A：表格分镜（推荐）
适合大多数场景，清晰易读。

### 格式B：剧本式分镜
适合剧情类，强调叙事 flow。

### 格式C：可视化描述
适合与画师/摄影师沟通，强调画面细节。

### 格式D：短视频分镜（紧凑版）
竖屏短视频专用，强调时长精确和钩子设计。

### 格式E：动画分镜
含关键帧、口型同步、动作线标注。

## 使用示例

**用户**："帮我写一个30秒咖啡广告的分镜，要温馨治愈风格"

**处理流程**：
1. 加载 `commercial.md` + `cinematography.md` + `transition.md`
2. 分析：30秒广告 ≈ 8-12个镜头，节奏中速偏慢（治愈风）
3. 确定色调：暖调、高调、软光
4. 生成：钩子→产品亮相→使用场景→情感升华→品牌CTA
5. 自检：产品3秒内出现✅ CTA明确✅ 转场流畅✅
6. 输出：表格分镜 + 色彩/影调建议

**用户**："做一个抖音15秒的美妆教程分镜"

**处理流程**：
1. 加载 `short_video.md` + `transition.md`
2. 分析：竖屏9:16，15秒，极快节奏，3-5秒换视觉
3. 结构：钩子(0-2s)→效果展示(2-5s)→步骤(5-13s)→CTA(13-15s)
4. 生成：含字幕位置/安全区标注
5. 自检：前3秒钩子✅ 无声可看✅ 竖屏构图✅
6. 输出：紧凑版表格分镜

## 资源引用

### 核心知识库
- **镜头语言基础** → [references/cinematography.md](references/cinematography.md)
- **广告分镜专项** → [references/commercial.md](references/commercial.md)
- **剧情片分镜** → [references/narrative.md](references/narrative.md)
- **好莱坞分镜** → [references/hollywood.md](references/hollywood.md)
- **MV分镜** → [references/mv.md](references/mv.md)
- **纪录片分镜** → [references/documentary.md](references/documentary.md)
- **短视频/竖屏分镜** → [references/short_video.md](references/short_video.md)
- **动画分镜** → [references/animation.md](references/animation.md)
- **长镜头设计** → [references/long_take.md](references/long_take.md)
- **电影级分镜** → [references/cinematic.md](references/cinematic.md)

### 专题知识库
- **转场设计** → [references/transition.md](references/transition.md)
- **声音叙事** → [references/sound_design.md](references/sound_design.md)
- **色彩情绪** → [references/color_mood.md](references/color_mood.md)
- **节奏控制** → [references/rhythm.md](references/rhythm.md)

### 参考与工具
- **分镜工具与术语** → [references/tools_and_terms.md](references/tools_and_terms.md)
- **分镜格式规范** → [references/format.md](references/format.md)
- **生成器脚本** → [scripts/storyboard_generator.py](scripts/storyboard_generator.py)
- **示例模板** → [assets/templates/](assets/templates/)

## 知识库完整列表

```
references/
├── cinematography.md      # 镜头语言基础
├── commercial.md          # 广告分镜专项
├── narrative.md           # 剧情片分镜
├── hollywood.md           # 好莱坞分镜+导演风格
├── mv.md                  # MV分镜
├── documentary.md         # 纪录片分镜
├── short_video.md         # 短视频/竖屏分镜
├── animation.md           # 动画分镜
├── long_take.md           # 长镜头设计
├── cinematic.md           # 电影级分镜
├── transition.md          # 转场设计
├── sound_design.md        # 声音叙事
├── color_mood.md          # 色彩与影调
├── rhythm.md              # 节奏控制
├── tools_and_terms.md     # 分镜工具与术语
└── format.md              # 格式规范
```
