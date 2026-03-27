---
layout: article
title: Blog 项目修改记录 02
tags: ["Blog", "项目修改记录"]
key: BlogChangeRecord02
permalink: docs/BlogChanges/ChangeRecord02
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
