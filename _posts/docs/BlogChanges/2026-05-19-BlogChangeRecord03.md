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

## 2026-05-19（修改 22）

### 修复带 docs permalink 的根层级文章图片路径误判

涉及文件：

- `_layouts/article.html`
- `AGENTS.md`
- `CHANGELOG.md`
- `_posts/docs/BlogChanges/2026-05-19-BlogChangeRecord03.md`

修改前：

- 文章页脚本用浏览器公开路径判断是否属于 `docs` 文档。
- 像 `_posts/2026-04-27-Unity中图片占用.md` 这种源码位于 `_posts` 根层级、但 permalink 是 `docs/Unity/ImageSizeInUnity` 的文章，会被误判为 `_posts/docs/Unity/` 下的文章。
- 因此正文里的 `image/2026-04-27-Unity中图片占用/1779192573093.png` 会被拼成 `_posts/docs/Unity/image/...`，而真实图片在 `_posts/image/...`。

修改前代码：

{% raw %}
```js
const currentPath = window.location.pathname;
const basePath = currentPath.substring(0, currentPath.lastIndexOf('/'));
const isDocs = basePath.includes('/docs/');
```
{% endraw %}

修改后：

- 图片根目录改为根据 Jekyll 提供的 `page.path` 计算，也就是按 Markdown 源文件所在目录解析。
- `_posts/2026-04-27-Unity中图片占用.md` 会解析到 `_posts/image/...`。
- `_posts/2025Year/2025-01-08-first_test.md` 会解析到 `_posts/2025Year/image/...`。
- `_posts/docs/UGUI/2025-04-23-BasicLayout.md` 会解析到 `_posts/docs/UGUI/image/...`。
- 这样公开 URL、permalink、导航路径如何变化，都不会影响文章内同层 `image/` 目录的图片解析。

修改后代码：

{% raw %}
```js
const postSourcePath = "{{ page.path }}";
const postAssetRoot = postSourcePath.includes("/")
  ? postSourcePath.substring(0, postSourcePath.lastIndexOf("/"))
  : "_posts";
```
{% endraw %}
