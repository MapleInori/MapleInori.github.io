---
layout: article
title: JsonUtility 无法转换匿名类
tags: ["Unity", "C#"]
key: 20260414JsonUtilityAnonymousClass
permalink: docs/Unity/JsonUtilityAnonymousClass
aside:
  toc: true
sidebar:
  nav: docs-Unity
---
# JsonUtility 为什么不能直接转匿名类

这次遇到的问题其实很简单：我想把几份存档数据临时拼成一个对象，然后直接交给 `JsonUtility.ToJson()` 转成字符串。

按普通 C# 的直觉来看，这样写好像没什么问题，因为匿名类本质上也是对象，里面也确实有字段内容，所以第一反应往往会觉得“应该能转”。

但实际在 Unity 里，`JsonUtility` 并不是一个特别通用的 JSON 工具。它依赖的是 Unity 自己的序列化规则，更适合处理结构明确、字段清晰的类型。

## 我一开始想写成什么样

一开始更省事的写法，大概会像这样：

```csharp
var saveData = new
{
    taskData = this.taskData,
    statsData = this.statsData
};
```

这样写的好处是临时组合数据很方便，不需要额外定义类型。

但问题就在这里：匿名类只是 C# 语法层面上方便，`JsonUtility` 并不会把它当成一个适合稳定序列化的目标类型来处理。

## 如果真的拿 JsonUtility 去转匿名类，会发生什么

这次我专门写了一个测试方法，把“序列化 -> 保存 -> 读取 -> 反序列化”整个流程都走了一遍：

```csharp
public void TestJsonUtilityWithAnonymousClass()
{
    var anonymousObject = new { Name = "Test", Value = 123 };

    string jsonString = JsonUtility.ToJson(anonymousObject);
    Debug.Log("Serialized Anonymous Object: " + jsonString); // Serialized Anonymous Object: {}

    const string saveKey = "Test_AnonymousClass_Json";

    // 先保存
    PlayerPrefs.SetString(saveKey, jsonString);
    PlayerPrefs.Save();
    Debug.Log("Saved Anonymous JSON: " + jsonString); // Saved Anonymous JSON: {}

    // 再读取
    string loadedJsonString = PlayerPrefs.GetString(saveKey, string.Empty);
    Debug.Log("Loaded Anonymous JSON: " + loadedJsonString); // Loaded Anonymous JSON: {}

    // 尝试反序列化回匿名类
    try
    {
        var deserializedObject = JsonUtility.FromJson(loadedJsonString, anonymousObject.GetType());
        Debug.Log("Deserialized Anonymous Object: " + deserializedObject); // Deserialized Anonymous Object: { Name = , Value = 0 }
    }
    catch (Exception ex)
    {
        Debug.LogError("Failed to deserialize anonymous object: " + ex.Message);
    }
}
```

从这组日志可以比较清楚地看出几件事：

- 第一步序列化时，结果直接变成了 `{}`，说明匿名类里的数据没有被 `JsonUtility` 正常写进去。
- 第二步保存到 `PlayerPrefs` 时，保存进去的也只是这个空对象字符串 `{}`。
- 第三步读取出来的内容依然是 `{}`，说明问题不是出在保存和读取环节，而是前面的序列化阶段就已经丢失了数据。
- 最后反序列化虽然没有直接报错，但拿回来的对象里 `Name` 变成空字符串，`Value` 变成 `0`，也就是只拿到了默认值，没有拿到原本真正的数据。

## 即使已经有同字段的类，var 也不会自动对应过去

这次测试里还有一个很容易误解的点：就算项目中已经提前定义了一个字段看起来一模一样的类，也不会改变匿名类测试失败的结果。

比如已经有这样一个类型：

```csharp
public class TestClass
{
    public string Name;
    public int Value;
}
```

但如果测试代码写的仍然是：

```csharp
var anonymousObject = new { Name = "Test", Value = 123 };
```

那这里的 `var` 推断出来的，依然是“匿名类型”，而不是上面的 `TestClass`。

也就是说，`var` 的作用只是让编译器根据右边实际创建出来的对象去推断类型，它不会因为项目里正好存在一个字段名相同、结构看起来很像的类，就自动帮你把它对应过去。

所以这类测试的关键并不在于“有没有写 `TestClass`”，而在于你右边到底创建的是什么：

- 写 `new { Name = "Test", Value = 123 }`，得到的就是匿名类型。
- 写 `new TestClass { Name = "Test", Value = 123 }`，得到的才是 `TestClass`。

这也解释了为什么“明明我已经写了 `TestClass`，结果还是空的”：因为 `JsonUtility` 处理到的对象类型，从头到尾就不是 `TestClass`，而是匿名类实例，也是为什么需要创建一个对应的包装类。

## 为什么 var 在别的地方又能显示正确类型

这里也顺手把 `var` 这个点理清楚一下。`var` 并不是“没有类型”，也不是“运行时再决定类型”，它本质上仍然是 **编译期类型推断**。

也就是说，编译器会根据右边表达式，或者 `foreach` 遍历目标的元素类型，直接推断出一个明确类型。

比如下面这些写法：

```csharp
var number = 123;
var text = "Hello";
var list = new List<string>();
```

它们之所以能显示出正确类型，是因为右边本身就已经很明确了：

- `123` 的类型就是 `int`
- `"Hello"` 的类型就是 `string`
- `new List<string>()` 的类型就是 `List<string>`

`foreach` 也是同样的道理：

```csharp
foreach (var item in stringList)
{
    Debug.Log(item.Length);
}
```

如果 `stringList` 的元素类型是 `string`，那 `item` 推断出来就是 `string`，所以鼠标放上去会显示正确类型，也能正常调用 `string` 的属性和方法。

所以 `var` 始终都只是“把已经能确定的真实类型省略掉不写出来”。

匿名类这个例子之所以容易让人误会，是因为它右边虽然也能推断出类型，但推断出来的恰好不是 `TestClass`，而是编译器生成的匿名类型。

所以至少也得是这样的：

```csharp
var anonymousObject2 = new TestClass { Name = "Test", Value = 123 };
```

## 为什么换成包装类就可以

如果改成显式定义一个包装类，`JsonUtility` 就更容易按 Unity 的序列化规则去处理这些字段。

```csharp
public string GetSaveData()
{
    TaskSaveDataWrapper saveData = new TaskSaveDataWrapper();

    saveData.taskData = this.taskData;
    saveData.statsData = this.statsData;

    Debug.Log(GetSaveKey() + " 存档数据: " + JsonUtility.ToJson(saveData));
    return JsonUtility.ToJson(saveData);
}

[System.Serializable]
public class TaskSaveDataWrapper
{
    public TaskSaveData taskData;
    public TaskStatsData statsData;
}
```

这里的关键点不是“包装类更高级”，而是它把数据结构明确写出来了。对 `JsonUtility` 来说，这种写法更稳定，也更符合它原本擅长处理的对象形式。

## 这件事应该怎么理解

所以这次踩坑之后，我会把它理解成一句话：

`JsonUtility` 适合处理“已经定义清楚结构的数据类”，不适合拿来随手序列化匿名类这种临时对象。

如果只是为了把几份数据拼在一起做存档，最稳妥的做法还是单独写一个 `[System.Serializable]` 的包装类。这样不仅当前序列化更清楚，后面如果还要用 `JsonUtility.FromJson()` 反序列化回来，也会更好维护。
