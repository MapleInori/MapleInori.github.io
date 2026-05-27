---
layout: article
title: VSCode 文件列表不显示 Git 状态标记
tags: ["VSCode", "Git"]
key: 20260527VSCodeGitDecorations
permalink: docs/Unity/VSCodeGitDecorations
aside:
  toc: true
sidebar:
  nav: docs-Unity
---
这篇记录一个很小但挺容易误判的问题：同样的 VS Code 扩展环境下，一个配置里文件列表会显示绿色文件、黄色文件，以及 `U`、`M` 之类的 Git 状态标记；另一个配置里却完全没有。

## 现象

在 VS Code 左侧 Explorer 文件列表中，正常情况下 Git 仓库里的文件会带状态装饰：

- 绿色文件 + `U`：`Untracked`，还没有被 Git 跟踪的新文件。
- 黄色文件 + `M`：`Modified`，已经被 Git 跟踪但内容发生修改。
- 其他常见字母还有 `A`、`D`、`R`，分别表示新增、删除、重命名等。

如果这些颜色和字母都不显示，很容易以为是 GitLens、Unity 扩展或者图标主题少装了。

## 原因

这不是 Unity 扩展问题，也不是 GitLens 必需功能，而是 VS Code 内置 Git 文件装饰被关掉了。

关键设置是：

```json
"git.decorations.enabled": false
```

当它为 `false` 时，Explorer 里的 Git 颜色和 `U/M` 标记会被隐藏。

另外还要确认 Explorer 装饰本身没有被关闭：

```json
"explorer.decorations.badges": true,
"explorer.decorations.colors": true
```

## 修复方式

在 VS Code 设置中搜索：

```text
Git: Decorations Enabled
或者
git.decorations.enabled
```

把它打开，或者在 `settings.json` 中写入：

```json
{
    "git.decorations.enabled": true,
    "explorer.decorations.badges": true,
    "explorer.decorations.colors": true
}
```

## 注意事项

这个功能还有一个前提：当前打开的目录必须是 Git 仓库，或者位于某个 Git 仓库内部。

如果项目根目录没有 `.git`，即使设置全部打开，也不会显示 `U/M` 这些 Git 状态标记。

简单判断方式：

```powershell
git status
```

如果能正常显示 Git 状态，说明仓库存在；如果提示不是 Git 仓库，则需要先初始化仓库或打开正确的项目根目录。
