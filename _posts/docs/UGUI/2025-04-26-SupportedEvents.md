---
layout: article
title: UGUI-Events-Supported Events
tags: ["Unity", "UGUI"]
key: Events-SupportedEvents
permalink: docs/UGUI/Events/SupportedEvents
aside:
  toc: true
sidebar:
  nav: docs-UGUI
---
## Supported Events（支持的事件）

事件系统（Event System）支持多种事件，这些事件还可以通过用户自定义的输入模块（Input Modules）进一步扩展。

由独立输入模块（Standalone Input Module）和触控输入模块（Touch Input Module）支持的事件是通过接口（interface）提供的，可以在 `MonoBehaviour` 上通过实现接口来使用。如果配置了有效的事件系统（Event System），这些事件将在正确的时机被调用。

* [IPointerEnterHandler](https://docs.unity.cn/Packages/com.unity.ugui@1.0/api/UnityEngine.EventSystems.IPointerEnterHandler.html) - **OnPointerEnter** - 当指针进入对象时调用
* [IPointerExitHandler](https://docs.unity.cn/Packages/com.unity.ugui@1.0/api/UnityEngine.EventSystems.IPointerExitHandler.html) - **OnPointerExit** - 当指针离开对象时调用
* [IPointerDownHandler](https://docs.unity.cn/Packages/com.unity.ugui@1.0/api/UnityEngine.EventSystems.IPointerDownHandler.html) - **OnPointerDown** - 当在对象上按下指针时调用
* [IPointerUpHandler](https://docs.unity.cn/Packages/com.unity.ugui@1.0/api/UnityEngine.EventSystems.IPointerUpHandler.html) - **OnPointerUp** - 当指针释放时调用（在指针点击的 GameObject 上调用）
* [IPointerClickHandler](https://docs.unity.cn/Packages/com.unity.ugui@1.0/api/UnityEngine.EventSystems.IPointerClickHandler.html) - **OnPointerClick** - 当指针在同一个对象上按下并释放时调用
* [IInitializePotentialDragHandler](https://docs.unity.cn/Packages/com.unity.ugui@1.0/api/UnityEngine.EventSystems.IInitializePotentialDragHandler.html) - **OnInitializePotentialDrag** - 找到拖拽目标时调用，可用于初始化数值
* [IBeginDragHandler](https://docs.unity.cn/Packages/com.unity.ugui@1.0/api/UnityEngine.EventSystems.IBeginDragHandler.html) - **OnBeginDrag** - 拖拽即将开始时，在拖拽物体上调用
* [IDragHandler](https://docs.unity.cn/Packages/com.unity.ugui@1.0/api/UnityEngine.EventSystems.IDragHandler.html) - **OnDrag** - 拖拽进行中时，在拖拽物体上调用
* [IEndDragHandler](https://docs.unity.cn/Packages/com.unity.ugui@1.0/api/UnityEngine.EventSystems.IEndDragHandler.html) - **OnEndDrag** - 拖拽结束时，在拖拽物体上调用
* [IDropHandler](https://docs.unity.cn/Packages/com.unity.ugui@1.0/api/UnityEngine.EventSystems.IDropHandler.html) - **OnDrop** - 拖拽结束时，在被放置的对象上调用
* [IScrollHandler](https://docs.unity.cn/Packages/com.unity.ugui@1.0/api/UnityEngine.EventSystems.IScrollHandler.html) - **OnScroll** - 鼠标滚轮滚动时调用
* [IUpdateSelectedHandler](https://docs.unity.cn/Packages/com.unity.ugui@1.0/api/UnityEngine.EventSystems.IUpdateSelectedHandler.html) - **OnUpdateSelected** - 每帧在选中对象上调用
* [ISelectHandler](https://docs.unity.cn/Packages/com.unity.ugui@1.0/api/UnityEngine.EventSystems.ISelectHandler.html) - **OnSelect** - 当对象成为选中对象时调用
* [IDeselectHandler](https://docs.unity.cn/Packages/com.unity.ugui@1.0/api/UnityEngine.EventSystems.IDeselectHandler.html) - **OnDeselect** - 当选中对象被取消选中时调用
* [IMoveHandler](https://docs.unity.cn/Packages/com.unity.ugui@1.0/api/UnityEngine.EventSystems.IMoveHandler.html) - **OnMove** - 发生移动事件（左、右、上、下）时调用
* [ISubmitHandler](https://docs.unity.cn/Packages/com.unity.ugui@1.0/api/UnityEngine.EventSystems.ISubmitHandler.html) - **OnSubmit** - 当提交按钮被按下时调用
* [ICancelHandler](https://docs.unity.cn/Packages/com.unity.ugui@1.0/api/UnityEngine.EventSystems.ICancelHandler.html) - **OnCancel** - 当取消按钮被按下时调用
