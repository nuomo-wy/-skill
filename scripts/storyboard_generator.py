#!/usr/bin/env python3
"""
Storyboard Generator - 分镜生成器
将自然语言描述转换为标准格式的分镜脚本
"""

import json
import sys
from datetime import datetime
from typing import List, Dict, Any

# 镜头类型定义
SHOT_TYPES = {
    "远": "远景",
    "全": "全景", 
    "中": "中景",
    "近": "近景",
    "特": "特写"
}

MOVEMENT_TYPES = [
    "固定", "推", "拉", "摇", "移", "跟", "升", "降", "手持"
]

ANGLE_TYPES = {
    "俯": "俯拍",
    "平": "平拍",
    "仰": "仰拍"
}

class StoryboardGenerator:
    def __init__(self):
        self.shots = []
        
    def add_shot(self, 
                 shot_num: int,
                 shot_type: str,
                 angle: str,
                 movement: str,
                 content: str,
                 audio: str = "",
                 duration: int = 3,
                 note: str = "") -> Dict:
        """添加单个镜头"""
        shot = {
            "镜号": shot_num,
            "景别": shot_type,
            "机位": angle,
            "运镜": movement,
            "画面内容": content,
            "声音": audio,
            "时长": f"{duration}s",
            "备注": note
        }
        self.shots.append(shot)
        return shot
    
    def generate_table(self) -> str:
        """生成表格格式的分镜"""
        if not self.shots:
            return "暂无镜头"
        
        # 表头
        headers = ["镜号", "景别", "机位", "运镜", "画面内容", "声音", "时长", "备注"]
        
        # 计算列宽
        col_widths = {}
        for h in headers:
            col_widths[h] = len(h)
        
        for shot in self.shots:
            for h in headers:
                col_widths[h] = max(col_widths[h], len(str(shot.get(h, ""))))
        
        # 生成表格
        lines = []
        
        # 分隔线
        sep = "+" + "+".join(["-" * (col_widths[h] + 2) for h in headers]) + "+"
        
        # 表头
        header_line = "|" + "|".join([f" {h:<{col_widths[h]}} " for h in headers]) + "|"
        
        lines.append(sep)
        lines.append(header_line)
        lines.append(sep)
        
        # 数据行
        for shot in self.shots:
            row = "|" + "|".join([f" {str(shot.get(h, '')):<{col_widths[h]}} " for h in headers]) + "|"
            lines.append(row)
        
        lines.append(sep)
        
        return "\n".join(lines)
    
    def generate_script(self, title: str = "分镜脚本") -> str:
        """生成剧本格式的分镜"""
        lines = [f"# {title}", f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ""]
        
        total_duration = 0
        
        for shot in self.shots:
            lines.append(f"### 镜头 {shot['镜号']}")
            lines.append(f"- 景别: {shot['景别']}")
            lines.append(f"- 机位: {shot['机位']}")
            lines.append(f"- 运镜: {shot['运镜']}")
            lines.append(f"- 时长: {shot['时长']}")
            lines.append(f"- 画面: {shot['画面内容']}")
            if shot['声音']:
                lines.append(f"- 声音: {shot['声音']}")
            if shot['备注']:
                lines.append(f"- 备注: {shot['备注']}")
            lines.append("")
            
            # 计算总时长
            try:
                total_duration += int(shot['时长'].replace('s', ''))
            except:
                pass
        
        lines.append(f"---")
        lines.append(f"总时长: {total_duration}秒")
        lines.append(f"镜头数: {len(self.shots)}个")
        lines.append(f"平均时长: {total_duration/len(self.shots):.1f}秒/镜头" if self.shots else "")
        
        return "\n".join(lines)
    
    def generate_summary(self) -> Dict[str, Any]:
        """生成统计分析"""
        if not self.shots:
            return {}
        
        total_duration = 0
        shot_type_count = {}
        movement_count = {}
        
        for shot in self.shots:
            # 时长统计
            try:
                total_duration += int(shot['时长'].replace('s', ''))
            except:
                pass
            
            # 景别统计
            st = shot['景别']
            shot_type_count[st] = shot_type_count.get(st, 0) + 1
            
            # 运镜统计
            mv = shot['运镜']
            movement_count[mv] = movement_count.get(mv, 0) + 1
        
        return {
            "总时长": f"{total_duration}秒",
            "镜头数": len(self.shots),
            "平均时长": f"{total_duration/len(self.shots):.1f}秒",
            "景别分布": shot_type_count,
            "运镜分布": movement_count
        }
    
    def export_json(self) -> str:
        """导出JSON格式"""
        return json.dumps({
            "shots": self.shots,
            "summary": self.generate_summary(),
            "generated_at": datetime.now().isoformat()
        }, ensure_ascii=False, indent=2)
    
    def clear(self):
        """清空所有镜头"""
        self.shots = []


def create_sample_storyboard() -> StoryboardGenerator:
    """创建示例分镜"""
    gen = StoryboardGenerator()
    
    # 示例：咖啡广告 15秒
    gen.add_shot(1, "远景", "俯拍", "固定", "城市清晨，阳光洒落", "轻音乐起", 2)
    gen.add_shot(2, "中景", "平拍", "推", "主角走进咖啡店", "门铃声", 2)
    gen.add_shot(3, "特写", "平拍", "固定", "咖啡杯，热气升腾", "咖啡机声音", 2)
    gen.add_shot(4, "近景", "平拍", "固定", "主角品尝，满足微笑", "", 3)
    gen.add_shot(5, "特写", "平拍", "固定", "咖啡品牌Logo", "品牌音效", 2)
    gen.add_shot(6, "全黑", "", "", "Slogan: 唤醒每一个清晨", "", 2)
    
    return gen


if __name__ == "__main__":
    # 命令行使用示例
    if len(sys.argv) > 1 and sys.argv[1] == "--sample":
        gen = create_sample_storyboard()
        print("=== 表格格式 ===")
        print(gen.generate_table())
        print("\n=== 剧本格式 ===")
        print(gen.generate_script("示例：咖啡广告"))
        print("\n=== 统计分析 ===")
        print(json.dumps(gen.generate_summary(), ensure_ascii=False, indent=2))
    else:
        print("Storyboard Generator")
        print("Usage: python storyboard_generator.py --sample")
