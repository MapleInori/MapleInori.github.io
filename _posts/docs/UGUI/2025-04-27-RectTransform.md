---
layout: article
title: UGUI-Reference-Rect Transform
tags: ["Unity", "UGUI"]
key: Reference-RectTransform
permalink: docs/UGUI/Reference/RectTransform
aside:
  toc: true
sidebar:
  nav: docs-UGUI
---
## Rect Transform（矩形变换）

Rect Transform 组件是 Transform（变换）组件在 2D 布局中的对应体。Transform 表示一个单一的点，而 Rect Transform 表示一个可以放置 UI 元素的矩形区域。如果一个 Rect Transform 的父物体也是 Rect Transform，那么子 Rect Transform 还可以指定它相对于父矩形的位置和尺寸。

![1745828200978](image/2025-04-27-RectTransform/1745828200978.png)

## Properties（属性）

|           Properties（属性）           | Function（功能）                                                                                                                                                                                                                                                      |
| :-------------------------------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|         **Pos (X, Y, Z)**         | 矩形的枢轴点（pivot point）相对于锚点（anchors）的位置。枢轴点是矩形旋转时围绕的中心位置。                                                                                                                                                                            |
|         **Width/Height**         | 矩形的宽度和高度。                                                                                                                                                                                                                                                    |
|   **Left, Top, Right, Bottom**   | 矩形边缘相对于各自锚点的位置。可以理解为在锚点定义的矩形内部的**内边距（padding）** 。<br />当锚点分开设置时，会显示这一组属性，取代 Pos 和 Width/Height（见下文）。<br />要访问这些选项，请点击 RectTransform 组件左上角的方形Anchor Presets（锚点预设）按钮。 |
|            **Anchors**            | 定义矩形左下角和右上角的锚点位置。                                                                                                                                                                                                                                    |
|              **Min**              | 矩形左下角的锚点位置，以父矩形尺寸为基准的小数表示。0,0 对应父物体的左下角，1,1 对应父物体的右上角。                                                                                                                                                                  |
|              **Max**              | 矩形右上角的锚点位置，以父矩形尺寸为基准的小数表示。0,0 对应父物体的左下角，1,1 对应父物体的右上角。                                                                                                                                                                  |
|             **Pivot**             | 矩形自身尺寸的小数表示的旋转枢轴点位置。0,0 对应左下角，1,1 对应右上角。                                                                                                                                                                                              |
|           **Rotation**           | 围绕枢轴点在 X、Y 和 Z 轴方向的旋转角度（单位为度数）。                                                                                                                                                                                                               |
|             **Scale**             | 在 X、Y 和 Z 方向上应用到对象的缩放因子。                                                                                                                                                                                                                             |
|  **Blueprint Mode（蓝图模式）**  | 将 RectTransform 编辑为未旋转和未缩放的状态，同时启用对齐吸附（snapping）。                                                                                                                                                                                           |
| **Raw Edit Mode（原始编辑模式）** | 启用后，编辑枢轴（pivot）和锚点（anchor）值时，不会为了保持矩形位置和大小不变而进行反向调整。                                                                                                                                                                         |

## Details（详细说明）

注意，一些 RectTransform 的计算是在一帧的末尾进行的，恰好在计算 UI 顶点之前，这样可以确保其与帧内所有最新变更同步。这意味着，在 Start 回调（Start()）和第一次 Update 回调（Update()）中，这些计算还尚未完成。

你可以通过在 Start() 回调中调用 `Canvas.ForceUpdateCanvases()` 方法来解决这个问题。这样可以强制 Canvas 在调用该方法时立即更新，而不是等待到帧结束时。

要了解 Rect Transform 的完整介绍和使用概览，请参见 **Basic Layout（基础布局）** 页面。
