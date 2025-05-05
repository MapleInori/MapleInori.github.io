---
layout: article
title: UGUI-UIHowTos-Making UI elements fit the size of their content
tags: ["Unity", "UGUI"]
key: UIHowTos-MakingUIElementsFitTheSizeOfTheirContent
permalink: docs/UGUI/UIHowTos/MakingUIElementsFitTheSizeOfTheirContent
aside:
  toc: true
sidebar:
  nav: docs-UGUI
---
# **Making UI elements fit the size of their content**（使 UI 元素适应其内容的大小）

通常，当使用其 **Rect Transform（矩形变换）** 来定位一个 UI 元素时，其位置和大小是手动指定的（也可以选择设置为随着父 **Rect Transform（矩形变换）** 拉伸的行为）。

然而，有时你可能希望该矩形根据 UI 元素的内容自动调整大小。这可以通过添加一个名为 **Content Size Fitter（内容尺寸适配器）** 的组件来实现。

## **Fit to size of Text**（适应 Text 文本的大小）

为了使带有 **Text（文本）** 组件的 **Rect Transform（矩形变换）** 适应其文本内容，需在拥有该 **Text** 组件的同一个 **Game Object（游戏对象）** 上添加一个 **Content Size Fitter** 组件。然后将 **Horizontal Fit（水平方向适配）** 和 **Vertical Fit（垂直方向适配）** 的下拉菜单都设置为  **Preferred（首选）** 。

### **How does it work?**（它是如何工作的？）

这里的原理是 **Text** 组件作为一个  **Layout Element（布局元素）** ，它可以提供其最小和首选尺寸的信息。在手动布局中，这些信息并不会被使用。而 **Content Size Fitter** 是一种  **Layout Controller（布局控制器）** ，它会监听 **Layout Element** 提供的布局信息，并根据这些信息控制 **Rect Transform** 的尺寸。

### **Remember the pivot**（记得设置 pivot（枢轴点））

当 UI 元素根据内容自动调整大小时，应格外注意 **Rect Transform** 的  **pivot（枢轴点）** 。调整大小时，**pivot** 会保持在原地，因此通过设置 **pivot** 的位置，可以控制元素扩展或收缩的方向。例如，若 **pivot** 设在中心，元素会向四周等量扩展；若设在左上角，则元素会向右和下扩展。

## **Fit to size of UI element with child Text**（使带有子 Text 的 UI 元素适应其内容大小）

如果你有一个 UI 元素，例如  **Button（按钮）** ，其拥有一个背景图像并包含一个作为子对象的 **Text** 组件，你可能希望整个 UI 元素根据文本的大小来适配（可能还需加些内边距）。

要实现这一点，先给该 UI 元素添加一个  **Horizontal Layout Group（水平布局组）** ，然后也添加一个  **Content Size Fitter** 。将  **Horizontal Fit** 、**Vertical Fit** 或两者都设置为  **Preferred** 。你可以使用 **Horizontal Layout Group** 中的 **padding（内边距）** 属性来添加并调整边距。

为什么要使用 Horizontal Layout Group？其实也可以使用  **Vertical Layout Group（垂直布局组）** ——只要子元素只有一个，它们的效果是一样的。

### **How does it work?**（它是如何工作的？）

**Horizontal（或 Vertical）Layout Group** 既是一个  **Layout Controller** ，也是一个  **Layout Element** 。它首先监听组内子对象（在此例中为子  **Text** ）提供的布局信息。然后，它计算出要容纳所有子对象所需的最小和首选尺寸，并将这些信息作为 **Layout Element** 提供出去。

**Content Size Fitter** 监听同一个 **Game Object** 上的任何 **Layout Element** 提供的布局信息——在此例中为  **Horizontal（或 Vertical）Layout Group** 。根据其设置，它随后会根据这些信息控制 **Rect Transform** 的大小。

一旦 **Rect Transform** 的大小被设置，**Horizontal（或 Vertical）Layout Group** 会确保根据可用空间对其子对象进行定位和尺寸调整。有关其如何控制子对象的位置和大小的更多信息，请参见 **Horizontal Layout Group** 页面。

## **Make children of a Layout Group fit their respective sizes**（使布局组中的子对象适应各自的内容大小）

如果你有一个  **Layout Group（布局组）** （水平或垂直），并希望其中的每个 UI 元素都适配自己的内容大小，该怎么做？

你不能给每个子对象都添加  **Content Size Fitter** 。原因是 **Content Size Fitter** 希望控制其自己的  **Rect Transform** ，而父 **Layout Group** 也想控制其子对象的  **Rect Transform** 。这就产生了冲突，结果是未定义行为。

不过也没必要这么做。父 **Layout Group** 本身就可以让每个子对象适配其内容大小。你需要做的是取消勾选 **Layout Group** 中的 **Child Force Expand（子对象强制扩展）** 选项。如果子对象本身也是  **Layout Group** ，你可能也需要在它们上面取消该选项。

一旦子对象不再随着灵活宽度扩展，你就可以通过 **Layout Group** 中的 **Child Alignment（子对象对齐）** 设置来指定它们的对齐方式。

如果你希望只有部分子对象扩展填充额外空间，而其他子对象不扩展怎么办？你可以通过给希望扩展的子对象添加一个 **Layout Element** 组件来轻松控制，并在这些 **Layout Element** 上启用 **Flexible Width（灵活宽度）** 或 **Flexible Height（灵活高度）** 属性。父 **Layout Group** 仍应保持 **Child Force Expand** 选项关闭，否则所有子对象都会灵活扩展。

### **How does it work?**（它是如何工作的？）

一个 **Game Object** 可以拥有多个组件，这些组件各自提供最小、首选和灵活尺寸的布局信息。一个优先级系统决定哪些值会覆盖其他值。**Layout Element** 组件的优先级高于  **Text** 、**Image** 和 **Layout Group** 组件，因此它可以用来覆盖它们提供的任何布局值。

当 **Layout Group** 监听其子对象提供的布局信息时，它会将被覆盖的灵活尺寸纳入考虑。然后在控制子对象大小时，不会将它们设置得大于其首选尺寸。然而，如果 **Layout Group** 启用了 **Child Force Expand** 选项，它仍会使所有子对象的灵活尺寸至少为 1。

## **More information**（更多信息）

本页讲解了一些常见用例的解决方案。关于自动布局系统的更深入解释，请参见 **UI Auto Layout** 页面。
