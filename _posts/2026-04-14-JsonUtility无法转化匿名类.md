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

**JsonUtility无法转换匿名类，必须要用准确类型**

在 Unity 里，如果想直接用 `JsonUtility.ToJson()` 去序列化匿名类，通常不会得到预期结果。

原因是 `JsonUtility` 走的是 Unity 自己的序列化规则，它更适合处理结构明确、可序列化的类型，而不是 C# 里这种临时拼出来的匿名对象。

所以这里更稳妥的做法是：单独定义一个包装类，把要保存的数据字段明确写出来。

```csharp
public string GetSaveData()
{
    //var saveData = new
    //{
    //    taskData = this.taskData,
    //    statsData = this.statsData
    //};

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

这样写虽然比匿名类多了一层定义，但好处是存档结构更清晰，后面如果还要配合 `JsonUtility.FromJson()` 反序列化，也会更稳定一些。
