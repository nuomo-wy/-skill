# Storyboard Master - 分镜大师

一个专为 AI 视频创作设计的 OpenClaw Skill，提供专业的分镜知识和生成能力。

## 功能特点

- 📽️ **专业镜头语言** - 涵盖景别、角度、运镜、构图等完整知识体系
- 🎬 **多类型支持** - 广告、短片、MV、剧情片、纪录片等
- 📝 **标准格式输出** - 表格、剧本、可视化描述等多种格式
- 🎯 **实用模板** - 15秒/30秒广告、剧情短片等现成模板
- ⚡ **生成器脚本** - Python 脚本支持程序化分镜生成

## 适用场景

- "帮我写一个30秒咖啡广告的分镜"
- "把这个剧本转成详细分镜脚本"
- "给这个镜头推荐几种拍摄手法"
- "什么是三分法则？"

## 知识库内容

| 文件 | 内容 |
|------|------|
| `cinematography.md` | 电影摄影基础：景别、角度、运镜、构图、光线 |
| `commercial.md` | 广告分镜专项：节奏控制、钩子设计、品牌露出 |
| `narrative.md` | 剧情片分镜：场景设计、叙事技巧、情感表达 |
| `format.md` | 格式规范：标注标准、输出格式、工具兼容 |

## 安装使用

### 作为 OpenClaw Skill 安装

1. 下载 `storyboard-master.skill` 文件
2. 放入 OpenClaw 的 skills 目录
3. 重启 OpenClaw 即可使用

### 直接使用知识库

所有 `references/` 下的文档可直接作为参考资料使用。

## 项目结构

```
storyboard-master/
├── SKILL.md                    # Skill 入口文件
├── scripts/
│   └── storyboard_generator.py # 分镜生成器
├── references/
│   ├── cinematography.md       # 镜头语言基础
│   ├── commercial.md           # 广告分镜指南
│   ├── narrative.md            # 剧情片分镜
│   └── format.md               # 格式规范
└── assets/templates/
    ├── 15s_commercial.md       # 15秒广告模板
    ├── 30s_commercial.md       # 30秒广告模板
    └── short_film.md           # 剧情短片模板
```

## 贡献

欢迎提交 Issue 和 PR，共同完善这个世界级的分镜知识库。

## 许可证

MIT License
