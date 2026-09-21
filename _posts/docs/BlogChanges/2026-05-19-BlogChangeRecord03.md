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

## 2026-06-11（修改 24）

### 修复文章代码块触发 Liquid 解析的问题

涉及文件：

- `_posts/2026-06-01-热更新开发2.md`
- `AGENTS.md`
- `_posts/docs/BlogChanges/2026-05-19-BlogChangeRecord03.md`

修改前：

- `热更新开发2-Lua语言` 文章里的 Lua 二维表示例，外层 table 的左花括号后紧跟内层 table 的左花括号。
- GitHub Pages 构建时会先解析 Liquid，再渲染 Markdown；即使内容位于 Markdown 代码块中，连续的模板变量起始符号仍可能被 Liquid 当成模板语法。
- 构建因此在该文章处报 Liquid syntax error。
- `AGENTS.md` 已记录说明文档里的 Liquid 兼容注意，但没有明确提醒 `_posts` 文章代码块同样会经过 Liquid 预处理。

修改后：

- 调整 Lua 示例写法，在外层 table 与内层 table 的左花括号之间加空格，Lua 语义不变。
- 补充 `AGENTS.md` 规则：文章代码块同样要避开 Liquid 模板符号，Lua、Vue、Handlebars、Mustache 等示例如果出现连续模板符号，应加空格、拆开示例，或使用 `raw` / `endraw` 包裹。
- 后续新增或修改文章时，遇到嵌套花括号示例要主动检查是否会被 GitHub Pages 的 Liquid 阶段提前解析。

## 2026-08-19（修改 25）

### 将 IMGUI 与 NGUI 课程文章加入 Unity 合集导航

涉及文件：

- `_data/navigation.yml`
- `_posts/2026-08-19-UnityUI系统-NGUI.md`
- `_posts/docs/BlogChanges/2026-05-19-BlogChangeRecord03.md`

修改前：

- Unity 合集导航只有“综合性知识”和“功能实现与问题记录”两个分组。
- IMGUI 文章虽然使用了 `docs-Unity` 侧边栏，却没有对应的合集导航入口。
- 新建的 NGUI 文章为空，也没有 Front Matter、固定链接和合集侧边栏配置。

修改后：

- 在 Unity 合集导航中新增“UI 系统”分组。
- 为 IMGUI 和 NGUI 两篇课程文章补充合集入口，使两篇文章可以相互切换。
- 为 NGUI 文章设置 Unity 标签、`docs/Unity/NGUI` 固定链接和 `docs-Unity` 侧边栏。
- 根据 53 节课程视频的标题建立文章章节，并补充 NGUI 定位、学习主线和阅读问题作为开头。

## 2026-08-19（修改 26）

### 新增 C# 合集并重构 Unity 合集导航

涉及文件：

- `_data/navigation.yml`
- `CHANGELOG.md`
- `_posts/2026-08-20-CSharp入门.md` ~ `_posts/2026-09-17-MVC思想.md`（29 篇课程目录文章）
- `_posts/2026-06-15-唐老师Unity框架.md`
- `_posts/2026-07-03-唐老师热更新-AssetBundle.md`
- `_posts/docs/BlogChanges/2026-05-19-BlogChangeRecord03.md`

修改前：

- 主页右侧目录只有 UGUI、Unity、Blog 修改三个合集入口。
- Unity 合集导航只有“综合性知识”“UI 系统”“功能实现与问题记录”三个分组，没有覆盖课程中的 C# 四部曲、Unity 基础/核心、数据持久化、网络开发、热更新和选修等内容。
- 部分课程文章标题里保留了讲师名。

修改后：

- 新增 `docs-CSharp` 侧边栏，并在主页右侧目录新增 C# 合集入口。
- 将 Unity 合集导航重构为 Unity 三部曲、UI 系统、数据持久化、网络开发、热更新、选修与进阶、综合性知识、功能实现与问题记录八个分组。
- 按课程视频标题为 29 门课创建了仅含目录的文章骨架（8 篇 C# + 21 篇 Unity）。
- 将导航中框架条目的显示名中性化，并在两篇含讲师名的文章末尾追加“参考”说明。

## 2026-08-19（修改 27）

### 拆分热更新系列并迁移两个 C# 小项目

涉及文件：

- `_data/navigation.yml`
- `CHANGELOG.md`
- `_posts/2026-05-20-编辑器扩展.md`（新建）
- `_posts/2026-05-20-热更新开发-AssetBundle.md`（新建，合并原 AssetBundle 笔记）
- `_posts/2026-06-01-热更新开发-Lua.md`（由热更新开发2 更名）
- `_posts/2026-06-06-热更新开发-xLua.md`（由热更新开发3 更名）
- `_posts/2026-09-06-热更新开发-ILRuntime.md`、`2026-09-07-热更新开发-ab包上传和下载.md`、`2026-09-08-热更新开发-toLua.md`（由三篇热更新骨架更名）
- `_posts/2026-08-24-CSharp实践-勇者斗恶龙.md`（并入 2025 年勇者斗恶龙内容）
- 删除 `_posts/2026-05-20-热更新开发1.md`、`2026-07-03-热更新-AssetBundle.md`、`2025Year` 下勇者斗恶龙与飞行棋两篇文章

修改前：

- 热更新相关内容分散为“热更新开发1/2/3”和一篇独立的 AssetBundle 笔记，其中“热更新开发1”同时包含编辑器扩展与 AssetBundle 两部分。
- 勇者斗恶龙、飞行棋两篇 C# 控制台项目文章仍放在 `_posts/2025Year/` 下，未归入 C# 合集。

修改后：

- 将“热更新开发1”拆分为“Unity 编辑器扩展”和“热更新开发-AssetBundle”两篇，AssetBundle 笔记并入后者。
- 热更新系列统一为“热更新开发-AssetBundle/Lua/xLua/toLua/ab包上传和下载/ILRuntime”六个条目，并在导航中新增“编辑器扩展”分组。
- 勇者斗恶龙内容迁移到 C# 合集“C# 实践——勇者斗恶龙”，飞行棋为空白文章直接移除，两篇均从 `_posts/2025Year/` 移出。

## 2026-09-21（修改 28）

### 新增理论类与实践类问题双向导航

涉及文件：

- `_data/navigation.yml`
- `_includes/sidebar/toc.html`
- `AGENTS.md`
- 使用 `docs-learning-theory` 与 `docs-learning-practice` 侧边栏的相关文章

修改前：

- 学习和开发过程中积累的问题分散在普通文章与 Unity 合集中，没有按“理论”和“实践”形成独立目录。
- 文档侧边栏的一级项目只能显示为分组标题，不能直接跳转到另一个文档类别。
- 主页右侧没有统一进入这批问题记录的合集入口。

修改前代码：

```html
<li class="toc-h1">一级标题</li>
```

修改后：

- 新增 `docs-learning-theory` 与 `docs-learning-practice` 两套侧边栏，分别收录原理类笔记和开发操作、故障处理类笔记。
- 两套侧边栏的第一项互相跳转：理论页顶部显示“实践类问题”，实践页顶部显示“理论类问题”。
- 侧边栏一级项目设置地址时渲染为链接；未设置地址的原有分组标题保持不变。
- 主页右侧新增“学习与开发问题”合集入口。
- 原 Unity 合集中的“安全区域”入口迁移到实践类问题目录，避免同一文章在两个合集目录中重复列出。

修改后代码：

```html
<li class="toc-h1"><a href="目标地址">一级标题</a></li>
```
