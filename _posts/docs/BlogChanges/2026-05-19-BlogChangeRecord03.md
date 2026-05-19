---
layout: article
title: Blog 项目修改记录 03
tags: ["Blog", "项目修改记录"]
key: BlogChangeRecord03
permalink: docs/BlogChanges/ChangeRecord03
home_exclude: true
aside:
  toc: true
sidebar:
  nav: docs-blog-changes
---
# Blog 项目修改记录 03

本文件用于记录第 21 至第 30 次站点项目改动。记录满 10 次后，新建下一篇继续记录。

## 2026-05-19（修改 21）

### 按年份整理 2025 年文章，并修正图片资源路径

涉及文件：

- `_config.yml`
- `_layouts/article.html`
- `_data/navigation.yml`
- `AGENTS.md`
- `CHANGELOG.md`
- `_posts/2025Year/`
- `_posts/docs/BlogChanges/2026-05-19-BlogChangeRecord03.md`

修改前：

- 2025 年文章直接散落在 `_posts` 根层级。
- 文章配图原先放在 `_posts/image`，后续移动文章后，如果编辑器继续把图片保存到文章同层的 `image` 文件夹，源码结构和页面图片重写逻辑会不一致。
- `_config.yml` 使用 `permalink: date`，该规则允许 `_posts` 下的子目录作为分类参与默认文章 URL。
- `_layouts/article.html` 中普通文章的图片 CDN 路径固定指向 `_posts/image`。

修改前代码：

{% raw %}
```yml
permalink   : date
```
{% endraw %}

{% raw %}
```js
newSrc = `https://cdn.jsdelivr.net/gh/MapleInori/MapleInori.github.io/_posts/${src}?raw=true`;
```
{% endraw %}

修改后：

- 把 `_posts` 根层级下的 25 篇 `2025-*.md` 移入 `_posts/2025Year/`。
- 把 2025 年文章使用的 `image` 文件夹放到 `_posts/2025Year/image/`，保持文章和编辑器粘贴图片生成目录处于同一层级。
- 保持全局文章 permalink 为 `date`，允许 `_posts/2025Year/` 作为分类前缀参与生成文章 URL。
- 构建排除列表继续保留 `_posts/image`，用于兼容编辑器在 `_posts` 根层级自动创建的粘贴图片目录；同时新增 `_posts/2025Year/image`。
- 让文章页脚本根据文章源码路径决定图片 CDN 根目录，位于 `_posts/2025Year/` 下的文章会访问 `_posts/2025Year/image/...`，`docs` 文章仍沿用原有 docs 图片路径。

修改后代码：

{% raw %}
```yml
permalink   : date
```
{% endraw %}

{% raw %}
```js
newSrc = `https://cdn.jsdelivr.net/gh/MapleInori/MapleInori.github.io/${postAssetRoot}/${src}?raw=true`;
```
{% endraw %}
