import datetime
import os

# 配置数据：按顺序排列需要生成的所有条目（跳过已创建的3个）
entries = [
    # 概述章节后续条目
    {"title": "Visual Components", "key": "VisualComponents"},
    {"title": "Interaction Components", "key": "InteractionComponents"},
    {"title": "Animation Integration", "key": "AnimationIntegration"},
    {"title": "Auto Layout", "key": "AutoLayout"},
    {"title": "Rich Text", "key": "RichText"},
    
    # Events章节
    {"title": "Messaging System", "key": "MessagingSystem"},
    {"title": "Input Modules", "key": "InputModules"},
    {"title": "Supported Events", "key": "SupportedEvents"},
    {"title": "Raycasters", "key": "Raycasters"},
    
    # Reference章节
    {"title": "Rect Transform", "key": "RectTransform"},
    {"title": "Canvas Components", "key": "CanvasComponents"},
    {"title": "Visual UI Interaction Components", "key": "VisualUIInteractionComponents"},
    {"title": "Interaction Components", "key": "InteractionComponents"},
    {"title": "Auto Layout", "key": "AutoLayout"},
    {"title": "Events", "key": "Events"},
    
    # UI How Tos章节
    {"title": "Designing UI for Multiple Resolutions", "key": "DesigningUIForMultipleResolutions"},
    {"title": "Making UI elements fit the size of their content", "key": "MakingUIElementsFitTheSizeOfTheirContent"},
    {"title": "Creating a World Space UI", "key": "CreatingAWorldSpaceUI"},
    {"title": "Creating UI elements from scripting", "key": "CreatingUIElementsFromScripting"},
    {"title": "Creating Screen Transitions", "key": "CreatingScreenTransitions"}
]

# 生成配置
start_date = datetime.date(2025, 4, 24)  # 开始日期
current_date = start_date

for i in range(0, len(entries), 3):
    # 每天生成三个文件
    batch = entries[i:i+3]
    for entry in batch:
        # 生成文件名
        filename = f"{current_date}-{entry['key']}.md"
        
        # 生成文件内容
        content = f"""---
layout: article
title: UGUI-{entry['title']}
tags: ["Unity", "UGUI"]
key: {entry['key']}
permalink: docs/UGUI/{entry['key']}
aside:
  toc: true
sidebar:
  nav: docs-UGUI
---"""
        
        # 写入文件
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
    
    # 日期递增
    current_date += datetime.timedelta(days=1)

print(f"已生成 {len(entries)} 个文件，从 {start_date} 开始")