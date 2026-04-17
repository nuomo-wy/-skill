---
name: storyboard-master
description: 专业视频分镜生成与优化技能。当用户需要创建视频分镜、镜头脚本、拍摄方案，或询问镜头语言、构图技巧、运镜方式、分镜格式、好莱坞分镜、导演风格等相关问题时使用。支持广告、短片、MV、剧情片、纪录片、好莱坞电影等多种视频类型的分镜创作。
---

# Storyboard Master - 分镜大师

## 概述

本技能提供专业的视频分镜知识体系，帮助AI生成结构化、可执行的分镜脚本。

## 核心能力

1. **分镜生成** - 根据创意描述生成完整分镜脚本
2. **镜头设计** - 提供镜头类型、景别、运镜方式建议
3. **格式输出** - 支持多种分镜格式（表格、脚本、可视化描述）
4. **优化建议** - 对现有分镜进行专业优化

## 工作流程

```
用户需求 → 视频类型判断 → 加载对应知识库 → 生成分镜 → 格式输出
```

### 步骤1：理解需求
- 视频类型（广告/短片/MV/剧情片/纪录片）
- 时长要求
- 风格定位
- 关键信息点

### 步骤2：选择知识库
根据视频类型加载对应参考文件：
- 通用镜头语言 → `references/cinematography.md`
- 广告分镜技巧 → `references/commercial.md`
- 剧情片分镜 → `references/narrative.md`
- 分镜格式规范 → `references/format.md`

### 步骤3：生成与输出
使用 `scripts/storyboard_generator.py` 生成标准格式分镜。

## 分镜要素

每个镜头应包含：
| 要素 | 说明 |
|------|------|
| 镜号 | 顺序编号 |
| 景别 | 远/全/中/近/特 |
| 机位 | 拍摄角度与高度 |
| 运镜 | 固定/推/拉/摇/移/跟/升降 |
| 画面内容 | 主体动作、构图描述 |
| 时长 | 秒数 |
| 声音/台词 | 对白、音效、音乐 |
| 备注 | 特殊要求 |

## 输出格式

### 格式A：表格分镜（推荐）
适合大多数场景，清晰易读。

### 格式B：剧本式分镜
适合剧情类，强调叙事 flow。

### 格式C：可视化描述
适合与画师/摄影师沟通，强调画面细节。

## 使用示例

**用户**："帮我写一个30秒咖啡广告的分镜，要温馨治愈风格"

**处理流程**：
1. 加载 `references/commercial.md` 和 `references/cinematography.md`
2. 分析：30秒广告 ≈ 8-12个镜头，节奏较快
3. 生成：包含产品展示、情感连接、品牌露出等关键镜头
4. 输出：表格分镜 + 镜头说明

## 资源引用

- **镜头语言基础** → [references/cinematography.md](references/cinematography.md)
- **广告分镜专项** → [references/commercial.md](references/commercial.md)
- **剧情片分镜** → [references/narrative.md](references/narrative.md)
- **好莱坞分镜** → [references/hollywood.md](references/hollywood.md)
- **MV分镜** → [references/mv.md](references/mv.md)
- **纪录片分镜** → [references/documentary.md](references/documentary.md)
- **分镜格式规范** → [references/format.md](references/format.md)
- **生成器脚本** → [scripts/storyboard_generator.py](scripts/storyboard_generator.py)
- **示例模板** → [assets/templates/](assets/templates/)
