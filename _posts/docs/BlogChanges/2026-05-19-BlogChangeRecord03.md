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

## 2026-06-02（修改 23）

### 优化主页响应式布局，并扩大文档正文宽度

涉及文件：

- `_sass/layout/_home.scss`
- `_sass/layout/_page.scss`
- `AGENTS.md`
- `_posts/docs/BlogChanges/2026-05-19-BlogChangeRecord03.md`

修改前：

- 主页宽屏使用三栏布局：左侧个人简介、中间文章列表、右侧合集目录。
- 当视口宽度小于 `1024px` 时，右侧合集目录会直接移动到文章列表下方；当视口宽度小于 `500px` 时，三栏才改为单栏。
- 左右栏宽度、卡片内边距和头像尺寸散落在样式规则中，后续微调时不容易快速找到入口。
- 带合集导航的文档页正文继续使用主题默认的 `950px` 最大宽度，宽屏下两侧空白偏多。

修改前代码：

```scss
.home__grid {
  grid-template-columns: minmax(11rem, 14rem) minmax(0, 1fr) minmax(12rem, 15rem);
  gap: map-get($spacers, 4);
}

@include media-breakpoint-down(lg) {
  .home__grid {
    grid-template-columns: minmax(11rem, 14rem) minmax(0, 1fr);
  }

  .home__column--directory {
    grid-column: 1 / -1;
  }
}
```

```scss
.main {
  max-width: map-get($layout, content-max-width);
}
```

修改后：

- 在 `_sass/layout/_home.scss` 顶部增加主页布局调节区，集中维护左右栏宽度、列间距、卡片内边距、头像尺寸和隐藏断点。
- 主页在 `1180px ~ 1439px` 区间内平滑缩小左右栏、间距和卡片内容。
- 视口小于 `1180px` 时先隐藏左侧个人简介；小于 `860px` 时再隐藏右侧合集目录；右侧目录不再移动到文章列表下方。
- 在 `_sass/layout/_page.scss` 顶部增加文档页布局调节区，将正文最大宽度集中定义为 `1188px`，相比原本的 `950px` 扩大约 `25%`。
- 文档页宽度调整只作用于带左侧合集导航的页面，不影响主页和普通页面。
- 左侧合集导航、右侧文章目录和目录右侧留白也集中为变量，便于后续继续调节。

修改后代码：

```scss
$home-profile-width-max: 14rem;
$home-profile-width-min: 10rem;
$home-directory-width-max: 15rem;
$home-directory-width-min: 11rem;
$home-hide-profile-at: 1180px;
$home-hide-directory-at: 860px;
```

```scss
@media (max-width: $home-hide-profile-at - 1) {
  .home__column--profile {
    display: none;
  }
}

@media (max-width: $home-hide-directory-at - 1) {
  .home__column--directory {
    display: none;
  }
}
```

```scss
$page-article-width: 1188px;
$page-sidebar-width: 250px;
$page-aside-width: clamp(15rem, 18vw, 18.75rem);
$page-aside-right-gap: 1.25rem;
```
