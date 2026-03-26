---
layout: article
title: Blog 项目修改记录 01
tags: ["Blog", "项目修改记录"]
key: BlogChangeRecord01
permalink: docs/BlogChanges/ChangeRecord01
aside:
  toc: true
sidebar:
  nav: docs-blog-changes
---
# Blog 项目修改记录 01

本文件用于记录第 1 至第 10 次站点项目改动。记录满 10 次后，新建下一篇继续记录。

## 2026-03-26（修改 1）

### 主页增加左侧个人信息窗口和右侧目录区

涉及文件：

- `_config.yml`
- `_layouts/home.html`
- `_includes/home/profile-card.html`
- `_includes/home/directory-panel.html`
- `_sass/layout/_home.scss`

修改前：

- 首页主体只有文章列表和分页，没有固定的个人信息区和目录区。
- `_layouts/home.html` 只有文章分页入口。
- `_sass/layout/_home.scss` 只有分页和列表的基础样式。
- `_includes/home/profile-card.html` 与 `_includes/home/directory-panel.html` 这两个文件当时还不存在。

修改前代码：

`_layouts/home.html`

{% raw %}
```html
<div class="layout--home">
  {%- include paginator.html -%}
</div>
```
{% endraw %}

`_sass/layout/_home.scss`

```scss
.layout--home {
  .pagination {
    margin: map-get($spacers, 4) 0;
  }
  .pagination__menu {
    max-width: 100%;
    @include overflow(auto);
  }
  .pagination__omit {
    color: $text-color-l;
  }
  .items {
    margin-top: map-get($spacers, 4) * 1.5;
  }
}
```

`_includes/home/profile-card.html`

```html
<!-- 文件不存在 -->
```

`_includes/home/directory-panel.html`

```html
<!-- 文件不存在 -->
```

修改后：

- 首页改成左侧个人信息、中央文章流、右侧目录的三栏结构。
- 左侧展示头像、昵称和自定义文本，数据来自 `_config.yml` 里的 `home_profile`。
- 右侧目录面板集中展示站点常用入口。
- 首页样式增加了卡片、响应式三栏和悬浮布局。

修改后代码：

`_layouts/home.html`

{% raw %}
```html
<div class="layout--home">
  <div class="home__grid">
    <aside class="home__column home__column--profile">
      {%- include home/profile-card.html -%}
    </aside>

    <div class="home__column home__column--feed">
      {%- include paginator.html -%}
    </div>

    <aside class="home__column home__column--directory">
      {%- include home/directory-panel.html -%}
    </aside>
  </div>
</div>
```
{% endraw %}

`_includes/home/profile-card.html`

{% raw %}
```html
<section class="home-profile card card--flat">
  <div class="home-profile__avatar-wrap">
    <img class="home-profile__avatar" src="{{ _profile_avatar_url }}" alt="{{ _profile_name }}">
  </div>
  <div class="home-profile__content">
    <p class="home-profile__eyebrow">{{ site.title }}</p>
    <h2 class="home-profile__name">{{ _profile_name }}</h2>
    {%- if _profile_message -%}
      <p class="home-profile__message">{{ _profile_message }}</p>
    {%- endif -%}
  </div>
</section>
```
{% endraw %}

`_includes/home/directory-panel.html`

{% raw %}
```html
<section class="home-directory card card--flat">
  <div class="home-directory__header">
    <p class="home-directory__eyebrow">Site Map</p>
    <h2 class="home-directory__title">目录</h2>
    <p class="home-directory__intro">主页右侧集中放置常用入口，顶部在首页保留品牌与搜索。</p>
  </div>

  <ul class="home-directory__list">
    {%- for _item in site.data.navigation.header -%}
      <li class="home-directory__item">
        <a href="{{ _nav_url }}">
          <span class="home-directory__item-title">{{ _item_title }}</span>
        </a>
      </li>
    {%- endfor -%}
  </ul>
</section>
```
{% endraw %}

`_sass/layout/_home.scss`

```scss
.layout--home {
  margin-top: map-get($spacers, 4);

  .home__grid {
    display: grid;
    grid-template-columns: minmax(14rem, 18rem) minmax(0, 1fr) minmax(15rem, 19rem);
    gap: map-get($spacers, 4);
    align-items: start;
  }
}

.home-profile,
.home-directory {
  padding: map-get($spacers, 4);
  background: linear-gradient(180deg, rgba($main-color-1, .08), rgba($background-color, .98));
}
```

### 首页把顶部导航标题改到右侧目录面板

涉及文件：

- `_includes/header.html`
- `_data/navigation.yml`

修改前：

- 首页顶部导航始终显示，不能单独为首页隐藏。
- 首页目录入口只能放在顶部，不能迁移到主页右侧。
- 导航里还有一个当前仓库没有落地页面的 `Csharp` 入口。

修改前代码：

`_includes/header.html`

{% raw %}
```html
{%- if site.data.navigation.header -%}
<nav class="navigation">
  <ul>
    {%- for _item in site.data.navigation.header -%}
      ...
    {%- endfor -%}
  </ul>
</nav>
{%- endif -%}
```
{% endraw %}

修改后：

- 首页增加 `hide_navigation` 开关，只在首页隐藏顶部导航。
- 原本顶部的导航标题改为由右侧目录面板统一展示。
- 清理掉无实际落地页面的 `Csharp` 导航入口。

修改后代码：

`_includes/header.html`

{% raw %}
```html
{%- assign _hide_navigation = page.header.hide_navigation | default: layout.header.hide_navigation -%}
...
{%- if site.data.navigation.header and _hide_navigation != true -%}
<nav class="navigation">
  <ul>
    {%- for _item in site.data.navigation.header -%}
      ...
    {%- endfor -%}
  </ul>
</nav>
{%- endif -%}
```
{% endraw %}

### 项目修改记录接入侧边栏导航并补充规则

涉及文件：

- `_data/navigation.yml`
- `_posts/2025-01-08-Blog修改.md`
- `AGENTS.md`
- `CHANGELOG.md`

修改前：

- `Blog修改` 这篇文章没有独立的结构化记录配套目录。
- 仓库里只有较粗略的说明，没有把“项目日志”和“CHANGELOG 摘要”一起约束清楚。

修改后：

- 新增 `docs-blog-changes` 侧边栏导航。
- `Blog修改` 文章接入侧边栏导航。
- 仓库规则里明确：项目本身改动要写详细日志，也要在 `CHANGELOG.md` 写摘要。

## 2026-03-26（修改 2）

### 项目修改记录迁移到独立文档目录

涉及文件：

- `AGENTS.md`
- `_data/navigation.yml`
- `_posts/2025-01-08-Blog修改.md`
- `_posts/docs/BlogChanges/2026-03-26-BlogChangeRecord01.md`
- `CHANGELOG.md`

修改前：

- 上一轮新增的 2026-03-26 项目修改记录直接写在旧文章 `Blog修改` 里。
- 虽然已经有 `docs-blog-changes` 侧边栏组，但还没有真正建立 `BlogChanges` 专用记录文件夹。
- 协作规则没有强制要求：只要改了 HTML、CSS、JavaScript，就必须贴出修改文件、修改前代码和修改后代码。

修改后：

- 新建 `_posts/docs/BlogChanges/`，结构化项目修改记录从 `ChangeRecord01` 开始。
- 把上一轮追加在 `Blog修改` 里的 2026-03-26 记录迁移到新文件中。
- `Blog修改` 文章继续保留，但回到“历史总记录”定位，并在正文里指向新的结构化记录页面。
- `docs-blog-changes` 导航同时包含旧的 `Blog修改` 和新的结构化记录文件。
- 协作规则新增：如果改动涉及 HTML、CSS、JavaScript，日志必须记录修改文件、修改前代码和修改后代码。
- 结构化记录文件从这一篇开始按“每篇最多 10 次修改”的规则继续滚动。

## 2026-03-26（修改 3）

### 转义修改记录文档中的 Liquid 代码片段以修复 GitHub Pages 构建

涉及文件：

- `_posts/docs/BlogChanges/2026-03-26-BlogChangeRecord01.md`
- `_posts/2025-01-08-Blog修改.md`
- `CHANGELOG.md`

修改前：

- 新的结构化修改记录页里直接写了包含 Liquid 语法的代码示例，例如 `&#123;%- include ... -%&#125;` 和 `&#123;&#123; ... &#125;&#125;`。
- GitHub Pages 使用的 Jekyll 会先解析 Liquid，再处理 Markdown，这会让“本来只是示例代码”的内容被当成真实模板执行。

修改前代码：

```text
代码块里直接写 Liquid 语法，例如：

&#123;%- include paginator.html -%&#125;
&#123;&#123; _profile_avatar_url &#125;&#125;
```

修改后：

- 给新日志页和旧 `Blog修改` 里带 Liquid 的代码示例补上 `raw` 包裹。
- 这样页面仍然显示原始代码，但构建时不会再把这些示例当模板执行。

修改后代码：

```text
在代码块外层增加 raw / endraw 包裹，让 GitHub Pages 只展示代码，不执行其中的 Liquid。
代码本身仍然保留原样，例如：
&#123;%- include paginator.html -%&#125;
&#123;&#123; _profile_avatar_url &#125;&#125;
```

## 2026-03-26（修改 5）

### 排除 `_posts` 下的二进制图片目录，避免 GitHub Pages 把图片当 UTF-8 文本读取

涉及文件：

- `_config.yml`
- `_posts/docs/BlogChanges/2026-03-26-BlogChangeRecord01.md`
- `CHANGELOG.md`

修改前：

- GitHub Pages 构建时会扫描 `_posts/image` 和 `_posts/docs/UGUI/image` 下的二进制图片。
- 在当前环境里，这些文件被不断报成 `invalid byte sequence in UTF-8`，日志非常长，也会干扰定位真正的致命错误。

修改前代码：

```yml
exclude:
  - CHANGELOG.md
  - HOW_TO_RELEASE.md
  - Gemfile
  - Gemfile.lock
  - LICENSE
  - README-*.md
  - README.md
```

修改后：

- 把 `_posts/image` 和 `_posts/docs/UGUI/image` 加入 `exclude`。
- 这些图片本来就通过外部地址访问，不依赖 Jekyll 复制到 `_site`，因此这里直接排除更稳妥。

修改后代码：

```yml
exclude:
  - CHANGELOG.md
  - HOW_TO_RELEASE.md
  - Gemfile
  - Gemfile.lock
  - LICENSE
  - README-*.md
  - README.md
  - /_posts/image
  - /_posts/docs/UGUI/image
```

## 2026-03-26（修改 4）

### 调整首页目录卡片的过渡动画写法以兼容 GitHub Pages 自带 Sass

涉及文件：

- `_sass/layout/_home.scss`
- `_posts/docs/BlogChanges/2026-03-26-BlogChangeRecord01.md`
- `CHANGELOG.md`

修改前：

- 首页目录卡片的 hover 动画使用了三个独立参数调用 `transition` mixin。
- 但当前主题里的 `transition` mixin 只接受一个参数，GitHub Pages 自带的旧版 Sass 在构建时会直接报错。

修改前代码：

```scss
@include transition(transform map-get($animation, duration), border-color map-get($animation, duration), box-shadow map-get($animation, duration));
```

修改后：

- 把三个动画项合并成主题已有写法支持的单参数形式。
- 现在既保留原来的过渡效果，也兼容 GitHub Pages 使用的 Sass 3.7 / Jekyll 3.10 环境。

修改后代码：

```scss
@include transition(#{transform map-get($animation, duration) map-get($animation, timing-function),
border-color map-get($animation, duration) map-get($animation, timing-function),
box-shadow map-get($animation, duration) map-get($animation, timing-function)});
```

## 2026-03-26（修改 6）

### 更新协作规则，补充 GitHub Pages 构建兼容约束

涉及文件：

- `AGENTS.md`
- `_posts/docs/BlogChanges/2026-03-26-BlogChangeRecord01.md`
- `CHANGELOG.md`

修改前：

- 协作规则已经要求记录项目级改动，但没有把这次排查出来的 GitHub Pages 构建兼容细节写进去。
- 文档里还缺少对 Liquid 示例写法、旧版 Sass mixin 兼容形式，以及 `_posts` 图片目录已被排除出构建的明确说明。

修改后：

- 在 `AGENTS.md` 中新增 GitHub Pages 兼容注意事项。
- 明确约束：Markdown 中展示 Liquid 语法要使用 `raw` 包裹或 HTML 实体转义。
- 明确说明：样式修改要优先兼容 GitHub Pages 自带的旧版 Jekyll / Liquid / Sass 环境。
- 明确说明：`_posts/image` 与 `_posts/docs/UGUI/image` 已排除出构建，站点级公共资源应优先放在未排除目录。

## 2026-03-26（修改 7）

### 排除 `AGENTS.md` 参与站点构建，并修复文档内的 Liquid 行内示例

涉及文件：

- `AGENTS.md`
- `_config.yml`
- `_posts/docs/BlogChanges/2026-03-26-BlogChangeRecord01.md`
- `CHANGELOG.md`

修改前：

- GitHub Pages 构建会把仓库根目录下的 `AGENTS.md` 当成普通 Markdown 页面处理。
- `AGENTS.md` 里新增的规则正文包含行内 Liquid 示例，写法是 `&#123;&#123; ... &#125;&#125;` 和 `&#123;% ... %&#125;`，在 GitHub Pages 的 Jekyll 里会先被 Liquid 解析。
- 结果是构建阶段直接报 `Tag '&#123;% ... %&#125;' was not properly terminated`，站点无法发布。

修改后：

- 把 `AGENTS.md` 中的行内 Liquid 示例改成 HTML 实体转义形式，避免再次触发模板解析。
- 在 `_config.yml` 的 `exclude` 中加入 `AGENTS.md`，让它只作为仓库协作文档存在，不再参与 GitHub Pages 构建。
- 以后即使继续补充 Agent 规则，也不会再因为这个文件本身进入构建流程而影响站点发布。

## 2026-03-26（修改 8）

### 修复项目修改记录页自身的 Liquid 行内示例转义遗漏

涉及文件：

- `_posts/docs/BlogChanges/2026-03-26-BlogChangeRecord01.md`
- `CHANGELOG.md`

修改前：

- `修改 7` 这条记录在描述报错原因时，又直接写了一次行内 Liquid 示例。
- 虽然逻辑上是在说明问题，但这两段 `&#123;&#123; ... &#125;&#125;` 与 `&#123;% ... %&#125;` 仍会被 GitHub Pages 当成真实 Liquid 语法解析。
- 结果是构建报错位置从 `AGENTS.md` 转移到了这篇项目修改记录页本身。

修改后：

- 把 `修改 7` 里的行内 Liquid 示例统一改成 HTML 实体转义形式。
- 这样这篇修改记录页在描述 Liquid 报错时，也不会再自己触发同类构建错误。
