---
layout: article
title: UGUI-Reference-Events
tags: ["Unity", "UGUI"]
key: Reference-Events
permalink: docs/UGUI/Reference/Events
aside:
  toc: true
sidebar:
  nav: docs-UGUI
---
# Event System Reference

本节提供以下事件系统组成部分的详细信息：

* [Event System Manager](https://docs.unity.cn/Packages/com.unity.ugui@1.0/manual/script-EventSystem.html)
* [Graphic Raycaster](https://docs.unity.cn/Packages/com.unity.ugui@1.0/manual/script-GraphicRaycaster.html)
* [Physics Raycaster](https://docs.unity.cn/Packages/com.unity.ugui@1.0/manual/script-PhysicsRaycaster.html)
* [Physics2D Raycaster](https://docs.unity.cn/Packages/com.unity.ugui@1.0/manual/script-Physics2DRaycaster.html)
* [Standalone Input Module](https://docs.unity.cn/Packages/com.unity.ugui@1.0/manual/script-StandaloneInputModule.html)
* [Touch Input Module](https://docs.unity.cn/Packages/com.unity.ugui@1.0/manual/script-TouchInputModule.html)
* [Event Trigger](https://docs.unity.cn/Packages/com.unity.ugui@1.0/manual/script-EventTrigger.html)

## **Event System Manager（事件系统管理器）**

该子系统负责控制组成事件系统的所有其他元素。它协调当前处于激活状态的  **Input Module（输入模块）** ，当前被认为“已选中”的  **GameObject（游戏对象）** ，以及其他一系列高级事件系统概念。

每次 **Update（更新）** 调用时，Event System 会查看其所有输入模块，并判断当前这一帧（tick）应使用哪一个输入模块。然后，它会将处理任务委托给该模块。

**属性（Properties）**

| 属性（Property）                       | 功能（Function）                                     |
| -------------------------------------- | ---------------------------------------------------- |
| First Selected（最初选中的对象）       | 第一个被选中的 GameObject（游戏对象）。              |
| Send Navigation Events（发送导航事件） | EventSystem 是否允许导航事件（移动 / 提交 / 取消）。 |
| Drag Threshold（拖拽阈值）             | 拖拽的软边界，以像素为单位。                         |

属性表下方是一个按钮： **“Add Default Input Modules（添加默认输入模块）”** 。

## **Graphic Raycaster（图形射线检测器）**

Graphic Raycaster 用于对 **Canvas（画布）** 执行射线检测。该射线检测器会检查画布上的所有  **Graphics（图形）** ，并判断是否有被命中。

Graphic Raycaster 可配置为忽略背面朝向的图形（Backfacing Graphics），也可以被其前方的 2D 或 3D 物体所阻挡。如果你希望将此元素的处理优先级手动设置为最前或最后，也可以通过设置优先级实现。

**属性（Properties）**

| 属性（Property）                         | 功能（Function）                   |
| ---------------------------------------- | ---------------------------------- |
| Ignore Reversed Graphics（忽略反向图形） | 是否忽略面朝背离射线检测器的图形？ |
| Blocked Objects（阻挡对象）              | 会阻挡图形射线检测的对象类型。     |
| Blocking Mask（阻挡遮罩）                | 会阻挡图形射线检测的对象遮罩类型。 |

## **Physics Raycaster（物理射线检测器）**

该射线检测器用于对场景中的 3D 物体进行射线检测。这允许将消息发送给实现了事件接口的 3D 物理对象。

**属性（Properties）**

| 属性（Property）                 | 功能（Function）                        |
| -------------------------------- | --------------------------------------- |
| Depth（深度）                    | 获取配置相机的深度。                    |
| Event Camera（事件相机）         | 获取此模块使用的相机。                  |
| Event Mask（事件遮罩）           | 相机遮罩与 eventMask 的逻辑与运算结果。 |
| Final Event Mask（最终事件遮罩） | 相机遮罩与 eventMask 的逻辑与运算结果。 |

## **Physics 2D Raycaster（2D 物理射线检测器）**

2D 射线检测器用于对场景中的 2D 对象进行射线检测。这允许将消息发送给实现了事件接口的 2D 物理对象。需要为此使用  **Camera GameObject（相机游戏对象）** ，如果未将 Physics 3D Raycaster 添加到该相机对象，则会自动将其添加。

关于更多 Raycaster（射线检测器）信息，请参阅 Raycasters 文档。

**属性（Properties）**

| 属性（Property）                        | 功能（Function）                 |
| --------------------------------------- | -------------------------------- |
| Event Camera（事件相机）                | 为此射线检测器生成射线的相机。   |
| Priority（优先级）                      | 与其他射线检测器相比的优先级。   |
| Sort Order Priority（排序顺序优先级）   | 基于排序顺序的射线检测器优先级。 |
| Render Order Priority（渲染顺序优先级） | 基于渲染顺序的射线检测器优先级。 |

## **Standalone Input Module（独立输入模块）**

该模块的设计行为符合你对控制器 / 鼠标输入的预期。按钮按下、拖拽等事件会根据输入情况发送。

当鼠标或其他输入设备在场景中移动时，该模块会向组件发送  **Pointer（指针）事件** ，并使用 **Graphics Raycaster（图形射线检测器）** 和 **Physics Raycaster（物理射线检测器）** 来计算当前被某个输入设备指向的是哪个元素。你可以根据需求配置这些射线检测器以检测或忽略场景的部分内容。

该模块还会根据 **Input 窗口**中追踪的输入，发送移动事件（move）以及提交 / 取消事件（submit / cancel）。这对键盘和控制器输入都适用。可在模块的 **Inspector（检查器）** 中配置追踪的轴和按键。

**属性（Properties）**

| 属性（Property）                         | 功能（Function）                                                 |
| ---------------------------------------- | ---------------------------------------------------------------- |
| Horizontal Axis（水平轴）                | 输入你希望用于水平轴的管理器名称。                               |
| Vertical Axis（垂直轴）                  | 输入你希望用于垂直轴的管理器名称。                               |
| Submit Button（提交按钮）                | 输入你希望用于提交按钮的管理器名称。                             |
| Cancel Button（取消按钮）                | 输入你希望用于取消按钮的管理器名称。                             |
| Input Actions Per Second（每秒输入次数） | 每秒允许多少次键盘 / 控制器输入。                                |
| Repeat Delay（重复延迟）                 | 在输入动作开始重复之前的延迟秒数。                               |
| Force Module Active（强制启用模块）      | 启用该属性以强制激活此 Standalone Input Module（独立输入模块）。 |

**详细说明（Details）**

该模块使用：

* **Vertical / Horizontal（垂直 / 水平）轴** 进行键盘和控制器导航
* **Submit / Cancel 按钮** 发送提交和取消事件
* 在事件之间设有超时限制，确保每秒最多触发一定数量的事件

---

**模块流程如下：**

* 若输入窗口中输入了有效轴，则向选中的对象发送 **Move（移动）事件**
* 若按下了  **Submit 或 Cancel 按钮** ，则向选中的对象发送提交或取消事件
* 处理鼠标输入：
  * 如果是新按下：
    * 向层级中每个可处理的对象发送 **PointerEnter（指针进入）事件**
    * 发送 **PointerPress（指针按下）事件**
    * 缓存拖拽处理器（层级中第一个能处理拖拽的元素）
    * 向拖拽处理器发送 **BeginDrag（开始拖拽）事件**
    * 将“按下”的对象设为 EventSystem 中的已选中对象
  * 如果是持续按压：
    * 处理移动
    * 向缓存的拖拽处理器发送 **Drag（拖拽）事件**
    * 如果触摸在对象之间移动，处理 **PointerEnter / PointerExit（指针进入 / 离开）事件**
  * 如果是释放：
    * 向接收 PointerPress 的对象发送 **PointerUp（指针抬起）事件**
    * 若当前悬停对象与 PointerPress 对象一致，则发送 **PointerClick（点击）事件**
    * 如果存在缓存的拖拽处理器，则发送 **Drop（放下）事件**
    * 向缓存的拖拽处理器发送 **EndDrag（结束拖拽）事件**
  * 处理滚轮事件（Scroll）

## **Touch Input Module（触摸输入模块）**

**注意：TouchInputModule 已被弃用。触摸输入现在由 StandaloneInputModule 处理。**

该模块专为触摸设备设计。它会根据用户输入发送指针触摸和拖拽事件。支持多点触控。

该模块使用场景中配置的 **Raycasters（射线检测器）** 来计算当前被触摸的元素。每个当前的触摸都会发出一次射线检测。

**属性（Properties）**

| 属性（Property）                    | 功能（Function） |
| ----------------------------------- | ---------------- |
| Force Module Active（强制启用模块） | 强制激活此模块。 |

**模块流程如下：**

* 对每个触摸事件：
  * 如果是新按下：
    * 向层级中每个可处理的对象发送 **PointerEnter（指针进入）事件**
    * 发送 **PointerPress（指针按下）事件**
    * 缓存拖拽处理器（层级中第一个能处理拖拽的元素）
    * 向拖拽处理器发送 **BeginDrag（开始拖拽）事件**
    * 将“按下”的对象设为 EventSystem 中的已选中对象
  * 如果是持续按压：
    * 处理移动
    * 向缓存的拖拽处理器发送 **Drag（拖拽）事件**
    * 如果触摸在对象之间移动，处理 **PointerEnter / PointerExit（指针进入 / 离开）事件**
  * 如果是释放：
    * 向接收 PointerPress 的对象发送 **PointerUp（指针抬起）事件**
    * 若当前悬停对象与 PointerPress 对象一致，则发送 **PointerClick（点击）事件**
    * 如果存在缓存的拖拽处理器，则发送 **Drop（放下）事件**
    * 向缓存的拖拽处理器发送 **EndDrag（结束拖拽）事件**

## **Event Trigger（事件触发器）**

Event Trigger 从 **Event System（事件系统）** 接收事件，并为每个事件调用注册的函数。

你可以使用 Event Trigger 为每一个事件系统事件指定希望调用的函数。你可以为单个事件指定多个函数，每当 Event Trigger 接收到该事件时，就会调用这些函数。

**注意：** 为 GameObject 添加 Event Trigger 组件后，该对象会拦截所有事件，**不会再向上传递（冒泡）事件！**

**事件（Events）**

点击  **Add New Event Type（添加新事件类型）按钮** ，可以选择将每个支持的事件包含在 Event Trigger 中。
