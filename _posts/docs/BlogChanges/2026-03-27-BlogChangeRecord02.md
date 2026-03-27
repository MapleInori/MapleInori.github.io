---
layout: article
title: Blog 项目修改记录 02
tags: ["Blog", "项目修改记录"]
key: BlogChangeRecord02
permalink: docs/BlogChanges/ChangeRecord02
home_exclude: true
aside:
  toc: true
sidebar:
  nav: docs-blog-changes
---
# Blog 项目修改记录 02

本文件用于记录第 11 至第 20 次站点项目改动。记录满 10 次后，新建下一篇继续记录。

## 2026-03-27（修改 1）

### 更新协作规则，明确主页右侧导航只保留合集入口

涉及文件：

- `AGENTS.md`
- `_data/navigation.yml`
- `_posts/docs/BlogChanges/2026-03-27-BlogChangeRecord02.md`

修改前：

- 协作规则里虽然已经区分了顶部导航和主页右侧导航，但还没有明确写出主页右侧只能放合集级入口。
- 项目修改日志规则也没有单独说明：日志正文不需要把 `CHANGELOG.md` 的同步更新写进“涉及文件”。
- 结构化项目修改记录上一篇已经写满 10 次，但侧边栏导航还没有接入下一篇记录文件。

修改后：

- 在 `AGENTS.md` 中新增“主页导航约定”，明确顶部导航保留站点级入口，主页右侧只显示合集名字。
- 明确规定：主页右侧导航不展开合集内部文章，不显示零散单篇，只跳转到合集第一篇或入口页。
- 在项目修改日志规则中补充：每次项目级改动仍要同步更新 `CHANGELOG.md` 摘要，但日志正文不需要把 `CHANGELOG.md` 单独列入“涉及文件”。
- 新建 `Blog 项目修改记录 02`，并把它接入 `docs-blog-changes` 侧边栏导航，作为后续新的记录文件。

## 2026-03-27（修改 2）

### 调整首页三栏宽度，恢复中间文章列表的阅读宽度

涉及文件：

- `_layouts/home.html`
- `_sass/layout/_home.scss`
- `_posts/docs/BlogChanges/2026-03-27-BlogChangeRecord02.md`

修改前：

- 首页虽然已经恢复成左侧个人信息、中间文章流、右侧文档入口的三栏结构，但主题主内容区默认最大宽度较窄。
- 左右两栏此前分配的宽度偏大，导致中间文章列表被明显挤压，阅读区域过小。

修改前代码：

`_layouts/home.html`

```yml
---
layout: page
type: webpage
---
```

`_sass/layout/_home.scss`

```scss
.layout--home {
  .home__grid {
    grid-template-columns: minmax(14rem, 18rem) minmax(0, 1fr) minmax(15rem, 19rem);
  }
}
```

修改后：

- 首页改为使用更适合三栏布局的全宽内容模式。
- 同时收窄左右两栏的最大宽度，把更多空间还给中间文章列表。
- 平板尺寸下的两栏布局也同步缩窄左栏，避免文章流再次被挤压。

修改后代码：

`_layouts/home.html`

```yml
---
layout: page
type: webpage
full_width: true
---
```

`_sass/layout/_home.scss`

```scss
.layout--home {
  .home__grid {
    grid-template-columns: minmax(11rem, 14rem) minmax(0, 1fr) minmax(12rem, 15rem);
  }
}
```

## 2026-03-27（修改 3）

### 主页右侧导航收敛为只显示合集名字

涉及文件：

- `_includes/home/directory-panel.html`
- `_data/navigation.yml`
- `_posts/docs/BlogChanges/2026-03-27-BlogChangeRecord02.md`

修改前：

- 主页右侧导航虽然已经改成合集入口，但每个入口下仍然带有说明文字。
- 对于后续合集和文章都会继续增长的站点来说，这种写法会让右侧导航显得偏长，也会继续占用中间文章区的可用宽度。

修改后：

- 主页右侧导航改为只显示合集名字，不再显示每个合集的说明文字。
- 文档入口数据也同步收敛为“标题加跳转地址”的轻量结构。
- 这样右侧更接近目录型导航，也更适合后续继续增加合集入口。

## 2026-03-27（修改 4）

### 恢复首页文章列表显示，并把右侧合集描述加回来

涉及文件：

- `_layouts/home.html`
- `_includes/home/directory-panel.html`
- `_data/navigation.yml`
- `_posts/docs/BlogChanges/2026-03-27-BlogChangeRecord02.md`

修改前：

- 首页中间栏只显示文章总数统计和分页按钮，没有实际文章列表。
- 原因是首页模板里只保留了 `paginator`，但 `paginator` 组件本身只负责统计与翻页，不负责渲染文章条目。
- 右侧合集导航在上一轮调整中被收成了只有标题，合集描述文字被去掉了。

修改前代码：

`_layouts/home.html`

{% raw %}
```html
<div class="home__column home__column--feed">
  {%- include paginator.html -%}
</div>
```
{% endraw %}

`_includes/home/directory-panel.html`

{% raw %}
```html
<li class="home-directory__item">
  <a href="{{ _nav_url }}">
    <span class="home-directory__item-title">{{ _item.title }}</span>
  </a>
</li>
```
{% endraw %}

## 2026-03-27（修改 5）

### 总结本轮排查经验，并把可复用规则回写到 Agent 文档

涉及文件：

- `AGENTS.md`
- `_posts/docs/BlogChanges/2026-03-27-BlogChangeRecord02.md`

修改前：

- `AGENTS.md` 已经记录了部分规则，但还缺少一份基于这几轮真实排查过程整理出来的“已知问题和处理经验”。
- 对 Agent 的要求主要还是“记录规则”，还没有明确强调：遇到同类问题后，应该主动复盘、提炼判断标准，并把稳定经验回写到规则文档中。

修改后：

- 在 `AGENTS.md` 中新增“已知问题与处理经验”，把 GitHub Pages 构建、首页三栏布局、主页导航职责分离、文章列表与分页关系、资源目录使用方式等经验集中写清楚。
- 新增“Agent 自我迭代要求”，明确要求后续修改不能只做一次性补丁，而要在问题解决后主动沉淀规则、补齐判断标准、检查文档是否过时。
- 这样后续再改首页、日志、导航或构建配置时，可以直接按经验清单检查，减少重复踩坑。

## 2026-03-27（修改 6）

### 让新的结构化修改记录不再出现在主页文章列表

涉及文件：

- `AGENTS.md`
- `_layouts/home.html`
- `_includes/paginator.html`
- `_posts/docs/BlogChanges/2026-03-26-BlogChangeRecord01.md`
- `_posts/docs/BlogChanges/2026-03-27-BlogChangeRecord02.md`

修改前：

- 新的结构化修改记录和普通文章一样都属于 `_posts`，因此会一起出现在主页中间的文章列表中。
- 旧的 `Blog修改` 文章也在 `_posts` 中，但用户希望它继续保留在主页文章流里，不需要隐藏。
- 主页当前直接读取 `paginator.posts` 渲染文章流，没有区分“应显示在首页”的文章和“只应保留在合集里的记录页”。

修改前代码：

`_layouts/home.html`

{% raw %}
```html
<div class="layout--articles">
  {%- include article-list.html articles=paginator.posts type='item'
    article_type='BlogPosting'
    show_cover=false
    show_excerpt=true
    show_readmore=true
    show_info=true -%}
</div>
```
{% endraw %}

修改后：

- 给新的结构化修改记录文件统一增加 `home_exclude: true` 标记。
- 首页文章流改为先过滤掉带有这个标记的记录页，再渲染文章列表。
- 分页统计文案也改为按过滤后的可见文章数量显示，避免主页上继续把隐藏记录算进去。
- 最初的 `Blog修改` 文章没有加这个标记，因此仍然会保留在主页文章流里。

修改后代码：

`_layouts/home.html`

{% raw %}
```html
{%- assign _home_posts = paginator.posts | where_exp: '_post', '_post.home_exclude != true' -%}
<div class="layout--articles">
  {%- include article-list.html articles=_home_posts type='item'
    article_type='BlogPosting'
    show_cover=false
    show_excerpt=true
    show_readmore=true
    show_info=true -%}
</div>
```
{% endraw %}

修改后：

- 首页中间栏重新加入文章列表渲染，恢复为“文章条目 + 翻页”的完整结构。
- 右侧合集导航恢复说明文字，继续保持“只列合集，不展开单篇”的形式。
- 这样首页中间栏能正常浏览文章，右侧目录也保留了更清晰的合集说明。

修改后代码：

`_layouts/home.html`

{% raw %}
```html
<div class="home__column home__column--feed">
  <div class="layout--articles">
    {%- include article-list.html articles=paginator.posts type='item'
      article_type='BlogPosting'
      show_cover=false
      show_excerpt=true
      show_readmore=true
      show_info=true -%}
  </div>
  {%- include paginator.html -%}
</div>
```
{% endraw %}

`_includes/home/directory-panel.html`

{% raw %}
```html
<li class="home-directory__item">
  <a href="{{ _nav_url }}">
    <span class="home-directory__item-title">{{ _item.title }}</span>
    {%- if _item.description -%}
      <span class="home-directory__item-description">{{ _item.description }}</span>
    {%- endif -%}
  </a>
</li>
```
{% endraw %}
