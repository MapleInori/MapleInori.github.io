---
layout: article
title: UGUI-Events-Messaging System
tags: ["Unity", "UGUI"]
key: Events-MessagingSystem
permalink: docs/UGUI/Events/MessagingSystem
aside:
  toc: true
sidebar:
  nav: docs-UGUI
---
## Messaging System（消息系统）

新的 UI 系统使用了一个消息系统，旨在取代 `SendMessage`。该系统完全基于 C#，并且旨在解决 `SendMessage` 存在的一些问题。这个系统通过使用可以在 `MonoBehaviour` 上实现的自定义接口来工作，以指示组件能够从消息系统接收回调。当发出调用时，会指定一个目标 `GameObject`；调用会在该 `GameObject` 上所有实现了指定接口的组件上执行。该消息系统允许传递自定义用户数据，并且可以指定事件在 `GameObject` 层级结构中传播的范围；也就是说，事件只在指定的 `GameObject` 上执行，或者也在其子对象和父对象上执行。

除此之外，消息框架还提供了辅助函数，用于搜索并查找实现了特定消息接口的 `GameObject`。

这个消息系统是通用的，设计上不仅可以供 UI 系统使用，也可以供一般的游戏代码使用。添加自定义消息事件非常简单，并且它们将使用与 UI 系统处理所有事件相同的框架进行工作。

## Defining A Custom Message（定义自定义消息）

如果你希望定义一个自定义消息，过程是相当简单的。在 `UnityEngine.EventSystems` 命名空间中，有一个名为 `IEventSystemHandler` 的基础接口。任何继承自该接口的内容，都可以被视为可以通过消息系统接收事件的目标。

```csharp
public interface ICustomMessageTarget : IEventSystemHandler
{
    // 可以通过消息系统调用的函数
    void Message1();
    void Message2();
}
```

一旦定义了这个接口，它就可以被一个 `MonoBehaviour` 实现。当实现后，就定义了如果针对这个 `MonoBehaviour` 的 `GameObject` 发送消息时要执行的函数。

```csharp
public class CustomMessageTarget : MonoBehaviour, ICustomMessageTarget
{
    public void Message1()
    {
        Debug.Log ("Message 1 received");
    }

    public void Message2()
    {
        Debug.Log ("Message 2 received");
    }
}
```

现在已经存在了一个可以接收消息的脚本，接下来需要发出消息。通常，这是为了响应某些松散耦合的事件。例如，在 UI 系统中，我们会在用户输入触发时发出事件，比如 `PointerEnter` 和 `PointerExit`，以及其他各种可能发生的交互。

为了发送消息，存在一个静态辅助类来执行这项操作。作为参数，它需要一个消息的目标对象、一些用户特定数据，以及一个映射到你希望调用的消息接口中特定函数的 functor（函数对象）。

```csharp
ExecuteEvents.Execute<ICustomMessageTarget>(target, null, (x,y)=>x.Message1());
```

这段代码会在目标 `GameObject` 上所有实现了 `ICustomMessageTarget` 接口的组件上执行 `Message1` 函数。关于 `ExecuteEvents` 类的脚本文档中还涵盖了其他形式的 `Execute` 函数，比如在子对象或父对象中执行调用。
