---
layout: article
title: VSCode Unity C# 加载问题记录
tags: ["Unity", "VSCode"]
key: 20260527VSCodeUnityCSharpLoad
permalink: docs/Unity/VSCodeUnityCSharpLoad
aside:
  toc: true
sidebar:
  nav: docs-Unity
---
之前也没在意，今天发现两台电脑扩展相同的情况下，居然一个正常一个不正常。

### 问题现象

在 VS Code 中打开 Unity 项目根目录后，C# 脚本看起来像“半失联”：

- 部分类名只是普通白色文本，没有正常的语义高亮。
- 无法跳转定义。
- 无法正常查找引用。
- 右键 `.sln` 或 `.csproj` 重新生成时也不顺利，容易看到项目加载失败。

这种情况第一眼很像 Unity 工程坏了，或者 C# 扩展没装好。但这次真正的问题不是脚本本身，而是 **VS Code 的 C# 后端选错了项目加载方式**。

### 日志里的关键线索

异常时，在 VS Code 的 Output 面板里可能会看到类似日志：

```text
ms-dotnettools.csdevkit\Projects.log
C# 开发工具包中不支持此项目
项目系统初始化已完成。0 项目已加载，6 加载失败。
```

这基本说明当前 workspace 被 **C# Dev Kit** 接管了。

Unity 2017 这类项目生成的 `.csproj` 通常是传统 .NET Framework 风格项目。VS Code 官方 C# Dev Kit FAQ 里也提到，C# Dev Kit 不支持 .NET Framework 项目；如果 workspace 设置了 `dotnet.preferCSharpExtension` 为 `true`，C# Dev Kit 会在这个 workspace 中被禁用。

所以这次要做的事情不是重装 Unity扩展，而是让当前 Unity 项目优先走普通 C# 扩展的加载方式。

正常时，在 `Output > C#` 里更希望看到类似内容：

```text
Activating C# standalone...
Language server initialized
正在加载 xxx.sln...
已成功完成加载 xxx.csproj
已完成加载所有项目
```

其中有些 warning 不一定致命，比如“具有未解析的依赖项”或“找不到 Visual Studio / Build Tools”。只要后面能看到 `.csproj` 成功加载，VS Code 的跳转、引用查找、语义高亮通常就会恢复。

### 修复方式

在 Unity 项目根目录创建或修改：

```text
.vscode/settings.json
```

写入：

```jsonc
{
    "dotnet.preferCSharpExtension": true, // 要求当前项目使用C#扩展，默认应该是false导致的
}
```

这个设置大概可以这样理解：

- `dotnet.preferCSharpExtension`：当前 workspace 优先使用普通 C# 扩展，避免 C# Dev Kit 接管 Unity 传统项目。

![1779812672198](https://file+.vscode-resource.vscode-cdn.net/d%3A/_MapleInori/MapleInori%20blog/MapleInori.github.io/_posts/image/2026-05-27-VsC/1779812672198.png)

其实VS Code 右下角会弹提示，可能没注意随手关了，大意是问这个 workspace 是否要使用 C# 扩展。点使用 C# 扩展后，它会自动创建 `.vscode/settings.json`，并写入：

```jsonc
{
    "dotnet.preferCSharpExtension": true
}
```

接下来就只需要保存文件并重启VScode就行了，然后回到脚本里测试类名高亮、跳转定义、查找引用。

如果仍然看到：

```text
ms-dotnettools.csdevkit\Projects.log
0 项目已加载
加载失败
```

那就说明当前 workspace 可能还是被 C# Dev Kit 接管，需要检查 `.vscode/settings.json` 是否真的写在 Unity 项目根目录下，以及 VS Code 是否已经 reload。

### 注意事项

- 如果只是想让这个 Unity 项目避开 C# Dev Kit，不需要全局卸载 C# Dev Kit，用 workspace 设置即可。
- `.vscode/settings.json` 是当前项目级设置，不会影响所有 VS Code 项目。
- `settings.json` 在 VS Code 里是 JSON with Comments，所以示例里写注释也能识别；如果拿到普通 JSON 工具里校验，注释可能会被报错。

简书那个文章里说的批量修改文件的方式我不喜欢，这怪麻烦的，他是这样的。

```
在所有*.csproj文件中搜索<TargetFrameworkVersion>v4.7.1</TargetFrameworkVersion>，在下面添加一行：<TargetFramework>net7.0</TargetFramework>，重启vscode即可。

作者：taiyosen
链接：https://www.jianshu.com/p/d364d6d0f3c7
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

### 参考

- [C# Dev Kit FAQ](https://code.visualstudio.com/docs/csharp/cs-dev-kit-faq#_why-isnt-chash-dev-kit-activating-chash-dev-kit-commands-are-not-found)  ， 跳转过去就是目标原文
- [简书记录](https://www.jianshu.com/p/d364d6d0f3c7)
