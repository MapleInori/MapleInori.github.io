---
layout: article
title: UGUI-Events-Input Modules
tags: ["Unity", "UGUI"]
key: Events-InputModules
permalink: docs/UGUI/Events/InputModules
aside:
  toc: true
sidebar:
  nav: docs-UGUI
---
## Input Modules（输入模块）

输入模块是配置和自定义事件系统主要逻辑的地方。Unity 默认提供了两种输入模块（Input Modules），一种为独立平台（Standalone）设计，另一种为触控输入（Touch Input）设计。每个模块根据其配置接收并分发事件，行为符合预期。

输入模块是事件系统（Event System）中处理“业务逻辑”的地方。当事件系统启用时，它会检查附加了哪些输入模块，并将更新处理交由具体的模块负责。

输入模块被设计为可以根据你希望支持的输入系统进行扩展或修改。它们的目的是将特定硬件的输入（如触摸、操纵杆、鼠标、动作控制器等）映射成通过消息系统发送的事件。

内置的输入模块旨在支持常见的游戏配置，如触摸输入、控制器输入、键盘输入和鼠标输入。如果你在 `MonoBehaviour` 上实现了特定接口，这些输入模块可以向应用程序中的控件发送各种事件。所有的 UI 组件都实现了适合自身功能的相关接口。
