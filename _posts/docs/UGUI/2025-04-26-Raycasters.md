---
layout: article
title: UGUI-Events-Raycasters
tags: ["Unity", "UGUI"]
key: Events-Raycasters
permalink: docs/UGUI/Events/Raycasters
aside:
  toc: true
sidebar:
  nav: docs-UGUI
---
## Raycasters（射线检测器）

事件系统（Event System）需要一种方法来检测当前输入事件应该发送到哪里，这由射线检测器（Raycasters）提供。给定一个屏幕空间位置（screen space position），射线检测器会收集所有可能的目标，判断它们是否位于指定位置之下，然后返回距离屏幕最近的对象。Unity提供了几种类型的射线检测器：

* **Graphic Raycaster（图形射线检测器）** —— 用于 UI 元素，挂载在 Canvas 上，并在该 Canvas 内进行搜索
* **Physics 2D Raycaster（2D 物理射线检测器）** —— 用于 2D 物理元素
* **Physics Raycaster（3D 物理射线检测器）** —— 用于 3D 物理元素

当场景中存在并启用了射线检测器（Raycaster）时，只要输入模块（Input Module）发起查询，事件系统（Event System）就会使用它。

如果场景中使用了多个射线检测器（Raycasters），那么系统会对它们全部进行检测（casting），然后根据与元素的距离对结果进行排序。
