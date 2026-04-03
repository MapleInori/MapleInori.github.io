---
layout: article
title: UnityLevel1
tags: ["Unity"]
key: 20250513Unity
permalink: docs/Unity/Level1
aside:
  toc: true
sidebar:
  nav: docs-Unity
---
## 命名空间

命名空间(namespace)是C#中组织代码的一种方式，它可以帮助我们：

* 避免命名冲突
* 逻辑组织相关代码
* 控制代码的可访问性

即使跨脚本的代码也可以属于同一个命名空间。

> [命名空间 - Unity 手册](https://docs.unity.cn/cn/2022.3/Manual/Namespaces.html)

## 生命周期

一般关注的生命周期：Awake，OnEnable，Start，FixedUpdate，Update，LateUpdate，OnGUI，OnDisable，OnDestroy。

场景加载时：调用Awake和OnEnable

- Awake：当脚本所挂载的对象在场景加载后处于激活状态，则会执行该脚本的Awake函数。即脚本所挂载对象被实例化时立刻调用Awake，如果游戏对象没有启用，则不会立刻调用Awake，而是在启用该游戏对象时立刻调用Awake。Awake在生命周期中仅会执行一次，并且Awake函数的执行与Awake所在脚本本身是否启用无关，即游戏对象启用但脚本未启用，依然可以执行Awake。
- OnEnable：当脚本被激活时调用，该函数可以在生命周期中多次执行，只要脚本从未激活状态切换到激活状态，则会执行一次OnEnable，不会反复执行Awake。

请注意，对于添加到场景中的对象，在为任何对象调用 Start 和 Update 等函数之前，会为_所有_ 脚本调用 Awake 和 OnEnable 函数。当然，在游戏运行过程中实例化对象时，不能强制执行此调用。

即Unity会确保所有脚本的Awake和OnEnable函数都被执行后，才会执行最早的一个Start。可以Test脚本挂载到多个游戏对象上进入游戏模式观察。

```csharp
using UnityEngine;

public class Test : MonoBehaviour
{
    private void Awake()
    {
        Debug.Log(gameObject.name + " Awake");
    }

    private void OnEnable()
    {
        Debug.Log(gameObject.name + " OnEnable");
    }
    // Start is called before the first frame update
    void Start()
    {
        Debug.Log(gameObject.name + " Start");
    }

    // Update is called once per frame
    void Update()
    {
  
    }
}

```

**Start**：在第一帧 **更新（Update）** 开始前执行Start函数，Unity会确保在执行任一Update之前，执行所有可执行（不包括未激活的脚本）的Start函数。

**FixedUpdate**：调用 **FixedUpdate** 的频度常常超过  **Update** 。如果帧率很低，可以每帧调用该函数多次；如果帧率很高，可能在帧之间完全不调用该函数。在 **FixedUpdate** 之后将立即进行所有物理计算和更新。在 **FixedUpdate** 内应用运动计算时，无需将值乘以  **Time.deltaTime** 。这是因为 **FixedUpdate** 的调用基于可靠的计时器（独立于帧率）。

**Update**：每帧调用一次  **Update** 。这是用于帧更新的主要函数。

**LateUpdate**：每帧调用一次 LateUpdate（在 Update完成后）。**LateUpdate** 开始时，在 **Update** 中执行的所有计算便已完成。**LateUpdate** 的常见用途是跟随第三人称摄像机。如果在 **Update** 内让角色移动和转向，可以在 **LateUpdate** 中执行所有摄像机移动和旋转计算。这样可以确保角色在摄像机跟踪其位置之前已完全移动。

**OnGUI：** 每帧调用多次以响应 GUI 事件。首先处理布局和重新绘制事件，然后为每个输入事件处理布局和键盘/鼠标事件。

在退出时调用：OnApplicationQuit，OnDisable，OnDestroy。OnDisable和OnEnable一样，都可以多次调用，OnDisable在脚本被失活时也会调用。

> [事件函数的执行顺序 - Unity 手册](https://docs.unity.cn/cn/2022.3/Manual/ExecutionOrder.html)

## 场景

 **场景(Scene)** 是游戏内容的基本组织单位，相当于游戏中的一个独立空间或关卡。每个场景包含：

* 游戏对象(GameObjects)的层级结构
* 场景特定的光照设置
* 摄像机、音频等环境配置
* 自定义的脚本逻辑

可以同时打开多个场景。

场景优化技巧：**场景分割** ，**空场景过渡，场景烘焙** ，**内存管理。**

启动场景(Splash Screen)在Player Settings中配置：设置启动画面，控制显示时间，指定首个加载场景

测试场景，创建专门的测试场景，包含调试工具和测试用例，不包含在最终发布版本中

创建可复用的场景模板，设置标准光照，配置通用UI框架，包含常用管理器

**Q: 场景加载后对象丢失引用？**
A: 使用FindObjectOfType或资源动态加载

**Q: 场景切换卡顿？**
A: 使用异步加载+加载画面

**Q: 如何跨场景保存数据？**
A: 使用PlayerPrefs、ScriptableObject或持久化单例

[场景 - Unity 手册](https://docs.unity.cn/cn/2022.3/Manual/CreatingScenes.html)

## Transform

任何子游戏对象的 Transform 值都是相对于父游戏对象的 Transform 值显示的。这些值称为 **局部坐标** 。对于场景构建，通常只需使用子游戏对象的局部坐标就足够了。

世界坐标：[position](https://docs.unity.cn/ScriptReference/Transform-position.html)，[rotation](https://docs.unity.cn/ScriptReference/Transform-rotation.html)，[lossyScale](https://docs.unity.cn/ScriptReference/Transform-lossyScale.html)，[eulerAngles](https://docs.unity.cn/ScriptReference/Transform-eulerAngles.html)

局部坐标：[localPosition](https://docs.unity.cn/ScriptReference/Transform-localPosition.html)，[localRotation](https://docs.unity.cn/ScriptReference/Transform-localRotation.html)，[localScale](https://docs.unity.cn/ScriptReference/Transform-localScale.html)，[localEulerAngles](https://docs.unity.cn/ScriptReference/Transform-localEulerAngles.html)

常用方法：[Find](https://docs.unity.cn/ScriptReference/Transform.Find.html)，[GetChild](https://docs.unity.cn/ScriptReference/Transform.GetChild.html)，[LookAt](https://docs.unity.cn/ScriptReference/Transform.LookAt.html)，[Rotate](https://docs.unity.cn/ScriptReference/Transform.Rotate.html)，[SetParent](https://docs.unity.cn/ScriptReference/Transform.SetParent.html)，[Translate](https://docs.unity.cn/ScriptReference/Transform.Translate.html)

[Unity - 脚本 API：转换](https://docs.unity.cn/ScriptReference/Transform.html)

[变换组件 - Unity 手册](https://docs.unity.cn/cn/2022.3/Manual/class-Transform.html)

## 渲染和相机

| 渲染器类型                       | 用途       | 典型对象         | 关键特性           |
| -------------------------------- | ---------- | ---------------- | ------------------ |
| **MeshRenderer**           | 3D模型渲染 | 立方体、角色模型 | 需要配合MeshFilter |
| **SkinnedMeshRenderer**    | 可变形网格 | 带动画的角色     | 支持骨骼权重       |
| **SpriteRenderer**         | 2D精灵渲染 | 2D角色、UI元素   | 使用Sprite图片     |
| **ParticleSystemRenderer** | 粒子效果   | 烟雾、火焰       | 配合粒子系统       |
| **LineRenderer**           | 绘制线条   | 激光、轨迹       | 动态生成线段       |

相机投影模式（Projection）：

- **Perspective（透视）** ：近大远小，模拟人眼。通过Field of View调整视野角度（通常60°）。
- **Orthographic（正交）** ：无透视效果，物体大小不变，通过Size调整可见范围，常用于2D游戏或UI。
- **Near** ：最近可见距离（建议≥0.3）
- **Far** ：最远可见距离（根据场景调整）

[Unity - Manual: Mesh Renderer component](https://docs.unity.cn/Manual/class-MeshRenderer.html)

[Unity - Manual: Skinned Mesh Renderer component](https://docs.unity.cn/Manual/class-SkinnedMeshRenderer.html)

[Unity - Manual: Sprite Renderer](https://docs.unity.cn/Manual/class-SpriteRenderer.html)

[Unity - Manual: Renderer module](https://docs.unity.cn/Manual/PartSysRendererModule.html)

[Unity - Manual: Line Renderer component](https://docs.unity.cn/Manual/class-LineRenderer.html)

[Unity - Manual: Camera component](https://docs.unity.cn/Manual/class-Camera.html)

[Unity - Scripting API: Camera](https://docs.unity.cn/ScriptReference/Camera.html)

**渲染优化** ：遮挡剔除(Occlusion Culling)、LOD、合批(Draw Call Batching)

**高级渲染** ：Shader编写、后处理栈(Post Processing Stack)

**相机进阶** ：Cinemachine插件、渲染纹理(Render Texture)

## 光照

| 光源类型                               | 图标 | 特点                       | 典型用途                   |
| -------------------------------------- | ---- | -------------------------- | -------------------------- |
| **Directional Light** （平行光） | ☀️ | 类似太阳光，无限远平行光线 | 户外日光效果               |
| **Point Light** （点光源）       | 💡   | 向所有方向均匀发光         | 灯泡、爆炸效果             |
| **Spot Light** （聚光灯）        | 🔦   | 锥形光束，有照射角度       | 手电筒、舞台灯             |
| **Area Light** （区域光）        | ▭   | 从矩形区域发光             | 柔和的室内灯光（仅烘焙用） |

* **Color** ：光源颜色（点击色块可调色）
* **Intensity** ：强度（平行光通常0.5-1，点光源1-10）
* **Shadow Type** ：阴影类型（无/硬阴影/软阴影）
* **Range** （点/聚光）：光照影响范围
* **Spot Angle** （聚光）：锥形角度（10-90度）
* **Baking** ：光照模式（Realtime/Mixed/Baked）

[Unity - Manual: Lights](https://docs.unity.cn/Manual/class-Light.html)

* **光照模式** ：Realtime（实时）/Baked（烘焙）/Mixed（混合）
* **全局光照** （Global Illumination）
* **光照探针** （Light Probes）
* **反射探针** （Reflection Probes）

## 碰撞和触发

1. 碰撞(Collision)

* **物理碰撞** ：两个物体实际接触并产生物理反应（如反弹）
* **必要条件** ：
  * 双方都有Collider组件
  * 至少一个物体有Rigidbody组件
  * 双方都不勾选"Is Trigger"

2. 触发(Trigger)

* **虚拟接触** ：物体穿过另一个物体但无物理反应
* **必要条件** ：
  * 双方都有Collider组件
  * 至少一个Collider勾选"Is Trigger"
  * 至少一个物体有Rigidbody组件（推荐挂在主动检测方）

| 函数                 | 调用时机           | 典型用途         |
| -------------------- | ------------------ | ---------------- |
| `OnCollisionEnter` | 碰撞开始时调用一次 | 播放撞击音效     |
| `OnCollisionStay`  | 碰撞持续时每帧调用 | 计算持续摩擦伤害 |
| `OnCollisionExit`  | 碰撞结束时调用一次 | 重置状态标志     |

| 函数           | 调用时机               | 典型用途       |
| -------------- | ---------------------- | -------------- |
| OnTriggerEnter | 进入触发区域时调用一次 | 拾取物品       |
| OnTriggerStay  | 在触发区域内每帧调用   | 持续治疗区域   |
| OnTriggerExit  | 离开触发区域时调用一次 | 离开安全区警告 |

物理碰撞消耗更多性能，如果不需要物理反应，优先使用触发检测。

## 刚体和关节

什么是刚体？

* 让游戏对象受物理引擎控制的组件
* 会自动响应重力、碰撞等物理效果

| 属性                   | 说明             | 典型值         |
| ---------------------- | ---------------- | -------------- |
| **Mass**         | 质量(kg)         | 1-10(合理范围) |
| **Drag**         | 空气阻力         | 0(无阻力)-10   |
| **Angular Drag** | 旋转阻力         | 0.05(默认)     |
| **Use Gravity**  | 是否受重力       | √/×          |
| **Is Kinematic** | 是否仅受脚本控制 | 常用于移动平台 |

固定关节(Fixed Joint)

* 将两个物体固定在一起
* 适合可断裂的连接

铰链关节(Hinge Joint)

* 像门铰链一样的旋转连接
* 可设置角度限制

弹簧关节(Spring Joint)

* 用弹簧连接两个物体
* 可调整刚度和阻尼

可配置关节(Configurable Joint)

* 最灵活的关节类型
* 可模拟各种物理连接(如布娃娃效果)

## 射线

什么是射线检测？

* **虚拟激光线** ：从起点沿特定方向发射一条不可见的检测线
* **碰撞检测** ：判断这条线是否与场景中的碰撞体相交
* **广泛应用** ：射击判定、物体选取、距离测量等

| 函数                   | 特点             | 适用场景             |
| ---------------------- | ---------------- | -------------------- |
| `Physics.RaycastAll` | 返回所有命中对象 | 穿透检测（如激光枪） |
| `Physics.SphereCast` | 球形射线检测     | 更宽松的检测范围     |
| `Physics.BoxCast`    | 盒形射线检测     | 区域检测             |
| `Physics.Linecast`   | 两点间直线检测   | 简单的视线判断       |

## 标签（Tag）和层（Layout）

**1. 标签（Tag）**

* **用途** ：用于快速识别和分类游戏对象（GameObject）。
* **特点** ：
  * 一个对象只能有一个标签
  * 常用于碰撞检测、查找对象（如 `FindGameObjectWithTag`）。
* **常见用法** ：

```csharp
  // 检查标签
  if (gameObject.CompareTag("Player")) {
      // 玩家逻辑
  }

  // 查找所有敌人
  GameObject[] enemies = GameObject.FindGameObjectsWithTag("Enemy");
```

**2. 层（Layer）**

* **用途** ：控制对象的物理碰撞、射线检测和渲染（如相机遮罩）。
* **特点** ：
  * 一个对象可以属于多个层（通过 LayerMask 组合）。
  * 32 个层可用（部分被 Unity 内置占用）。
* **常见用法** ：

```csharp
  // 设置对象层
  gameObject.layer = LayerMask.NameToLayer("Enemy");

  // 射线检测忽略特定层
  int layerMask = ~(1 << LayerMask.NameToLayer("UI"));
  Physics.Raycast(ray, out hit, Mathf.Infinity, layerMask);
```

**3. 核心区别**

| **特性**     | **标签（Tag）**  | **层（Layer）**            |
| ------------------ | ---------------------- | -------------------------------- |
| **数量限制** | 单个对象一个标签       | 单个对象一个主层（但掩码可组合） |
| **主要用途** | 逻辑分类（如敌我识别） | 物理/渲染控制（碰撞、射线等）    |
| **编辑方式** | 字符串自由定义         | 需在 Unity 的 Layer 面板预定义   |

**4. 使用建议**

* **标签** ：适合标记对象的 **逻辑角色** （如 "Player"、"Enemy"、"Item"）。
* **层** ：适合控制 **物理交互和渲染** （如 "Ground"、"UI"、"IgnoreRaycast"）。

[Unity - Manual: Tags](https://docs.unity.cn/Manual/Tags.html)

[Unity - Manual: Layers](https://docs.unity.cn/Manual/Layers.html)

## Action和UnityEvent

委托delegate还有UnityAction，几者对比。回调的概念

## UGUI

## Input系统

## 动画系统

## 特效系统

## 导航系统

## 多媒体

## 协程

## 场景切换

## LOD

## 预制体

## 对象池

## 网络请求

## Json解析

## 存档

## Cinemachine

## TimeLine

## 参考

[从零开始的Unity魔法学堂](https://learn.u3d.cn/tutorial/MagicCollege)，

数据存储存到本地也存到服务器，并且校验，选择可以覆盖，像steam。

把里边可以作为框架一部分的列出来，后续自己写独游框架

导出时的PlayerSetting

虚拟列表大量物品排列性能优化，对象池
