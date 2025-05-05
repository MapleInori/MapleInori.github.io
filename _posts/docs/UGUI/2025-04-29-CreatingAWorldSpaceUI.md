---
layout: article
title: UGUI-UIHowTos-Creating a World Space UI
tags: ["Unity", "UGUI"]
key: UIHowTos-CreatingAWorldSpaceUI
permalink: docs/UGUI/UIHowTos/CreatingAWorldSpaceUI
aside:
  toc: true
sidebar:
  nav: docs-UGUI
---
# 创建一个世界空间 UI（World Space UI）

UI 系统使得在场景中的其他 2D 或 3D 对象之间创建定位在世界中的 UI 变得非常容易。

如果你的场景中还没有 UI 元素（例如 Image 图像），请通过 `GameObject > UI > Image` 创建一个 UI 元素。这也会为你自动创建一个 `Canvas`（画布）。

## 将 Canvas 设置为世界空间（World Space）

选择你的 `Canvas`，然后将其 `Render Mode`（渲染模式）更改为 `World Space`（世界空间）。

现在你的 `Canvas` 已经定位在世界中，并且只要摄像机指向它，就能被所有摄像机看到，但它相对于场景中的其他对象来说可能非常大。我们稍后会处理这个问题。

## 决定分辨率

首先你需要决定 `Canvas` 的分辨率。如果这是一个图像，它的像素分辨率应该是多少？例如，800x600 是一个不错的起点。你可以在 `Canvas` 的 `Rect Transform`（矩形变换）组件中的 `Width`（宽度）和 `Height`（高度）值中输入分辨率。最好同时将位置设置为 0,0。

## 指定 Canvas 在世界中的尺寸

现在你应该考虑 `Canvas` 在世界中应该有多大。你可以使用 `Scale`（缩放）工具将其缩小，直到它的尺寸看起来合适，或者你可以决定它在世界中应有多少米宽。

如果你希望它在世界中具有特定的宽度（以米为单位），你可以通过公式 `meter_size / canvas_width` 计算出所需的缩放比例。例如，如果你希望它是 2 米宽，而 `Canvas` 的宽度是 800，那么就是 2 / 800 = 0.0025。然后将 `Canvas` 的 `Rect Transform`（矩形变换）组件中的 `Scale` 属性设置为 X、Y 和 Z 都为 0.0025，以确保其均匀缩放。

另一种理解方式是：你在控制 `Canvas` 中一个像素在世界中的实际大小。如果 `Canvas` 被缩放为 0.0025，那么 `Canvas` 中的每个像素在世界中也就是 0.0025 米大小。

## 设置 Canvas 的位置

与设置为 `Screen Space`（屏幕空间）的 Canvas 不同，`World Space`（世界空间）Canvas 可以在场景中自由定位和旋转。你可以将 `Canvas` 放在任何墙面、地板、天花板或倾斜的表面上（当然也可以悬浮在空中）。只需使用工具栏中的常规 `Translate`（移动）和 `Rotate`（旋转）工具即可。

## 创建 UI

现在你可以像使用 `Screen Space Canvas`（屏幕空间画布）那样开始设置你的 UI 元素和布局了。
