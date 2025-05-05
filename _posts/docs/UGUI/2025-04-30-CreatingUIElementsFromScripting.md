---
layout: article
title: UGUI-UIHowTos-Creating UI elements from scripting
tags: ["Unity", "UGUI"]
key: UIHowTos-CreatingUIElementsFromScripting
permalink: docs/UGUI/UIHowTos/CreatingUIElementsFromScripting
aside:
  toc: true
sidebar:
  nav: docs-UGUI
---
# **Creating UI elements from scripting（通过脚本创建 UI 元素）**

如果你正在创建一个动态 UI，其中的 UI 元素会根据用户操作或游戏中的其他行为出现、消失或变化，那么你可能需要编写脚本，根据自定义逻辑实例化新的 UI 元素。

## **Creating a prefab of the UI element（创建 UI 元素的预制体）**

为了能够动态地轻松实例化 UI 元素，第一步是为你想要实例化的 UI 元素类型创建一个  **Prefab（预制体）** 。在场景中按照你希望的方式设置 UI 元素，然后将该元素拖入 **Project View（项目视图）** 中，将其变为一个预制体。

例如，一个按钮的预制体可能是一个包含 **Image（图像）组件** 和 **Button（按钮）组件** 的  **GameObject（游戏对象）** ，并且该对象还有一个包含 **Text（文本）组件** 的子对象。根据你的需求，具体设置可能会有所不同。

你可能会疑惑为什么我们没有提供用于创建各种控件（包括外观和其他内容）的 API 方法。原因是，比如一个按钮，就有无限种设置方式。它是只使用图像、文本，还是两者都有？是否使用多个图像？文本的字体、颜色、字号、对齐方式又是什么？图像使用哪一个或哪些  **Sprite（精灵）** ？通过让你创建预制体并实例化，你可以精确地设置你希望的样式。而且如果你之后想更改 UI 的外观和风格，只需要修改预制体即可，这些更改将会自动反映到你的 UI 中，包括那些通过脚本动态创建的 UI。

## **Instantiating the UI element（实例化 UI 元素）**

UI 元素的预制体通过常规方式使用 **Instantiate（实例化）** 方法进行创建。在设置新实例化的 UI 元素的父对象时，推荐使用 **Transform.SetParent（设置父级）** 方法，并将 **worldPositionStays（保持世界坐标）** 参数设置为  **false** 。

## **Positioning the UI element（定位 UI 元素）**

UI 元素通常通过其 **Rect Transform（矩形变换）** 进行定位。如果 UI 元素是某个 **Layout Group（布局组）** 的子对象，它会自动进行定位，这一步可以省略。

在定位一个 Rect Transform 时，首先要确定它是否具有拉伸行为。**拉伸行为（Stretching behavior）** 发生在 **anchorMin（锚点最小值）** 和 **anchorMax（锚点最大值）** 属性不相等的情况下。

对于不拉伸的 Rect Transform，最简单的定位方式是设置 **anchoredPosition（锚点位置）** 和 **sizeDelta（尺寸增量）** 属性。anchoredPosition 表示对象的 **pivot（中心点）** 相对于锚点的位置。sizeDelta 在没有拉伸的情况下等同于元素的实际大小。

对于拉伸的 Rect Transform，更简单的设置方式是使用 **offsetMin（最小偏移）** 和 **offsetMax（最大偏移）** 属性。offsetMin 表示矩形左下角相对于左下锚点的偏移量，offsetMax 表示矩形右上角相对于右上锚点的偏移量。

## **Customizing the UI Element（自定义 UI 元素）**

如果你要动态实例化多个 UI 元素，它们很可能需要不同的外观和行为。无论是菜单中的按钮、背包中的物品，还是其他类型的元素，你通常希望每个元素有不同的文本或图像，并在交互时执行不同的操作。

实现方法是获取各种组件并更改它们的属性。请参阅 **Image（图像）** 和 **Text（文本）** 组件的脚本参考文档，以及如何在脚本中使用  **UnityEvents（Unity 事件）** 。
