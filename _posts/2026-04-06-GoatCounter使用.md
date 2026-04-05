---
layout: article
title: GoatCounter 使用说明
tags: ["Blog", "统计", "GoatCounter"]
key: 20260406GoatCounter
aside:
  toc: true
---
最近把博客的阅读量统计从 LeanCloud 换成了 GoatCounter，这篇文章简单记录一下使用方式、接入步骤，以及实际使用中踩到的坑。

**纯AI写的这篇，主要是LeanCloud停运了，没办法。好困，眠了。**

GoatCounter 官网：
[GoatCounter](https://www.goatcounter.com/)

官方文档里我这次主要参考了这几页：

- [Getting started](https://www.goatcounter.com/help/start)
- [Visitor counter](https://www.goatcounter.com/help/visitor-counter)
- [Control the path that&#39;s sent to GoatCounter](https://www.goatcounter.com/help/path)
- [Sessions and visitors](https://www.goatcounter.com/help/sessions)
- [Host count.js somewhere else](https://www.goatcounter.com/help/countjs-host)

## 1. 为什么换成 GoatCounter

我原来用的是 LeanCloud 统计阅读量。

但后来不想继续依赖它，于是开始找替代方案。我的需求其实很简单：

1. 配置尽量少
2. 能接进静态博客
3. 最好还能显示文章阅读量

GoatCounter 对这种需求还挺合适，因为它最基础的接入方式只需要一段脚本：

```html
<script data-goatcounter="https://你的站点代号.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
```

像我注册后拿到的就是：

```html
<script data-goatcounter="https://mapleinori.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
```

这一步就已经可以开始统计访问了。

## 2. 最基础的接入方式

GoatCounter 官方给的入门方式就是把统计脚本插进页面里。

```html
<script data-goatcounter="https://mapleinori.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
```

如果只是想让后台开始有数据，这一段就够了。

它的作用是：

1. 页面加载时向 GoatCounter 发送一次统计
2. 后台开始记录访问数据

如果你用的是普通静态博客、GitHub Pages、Jekyll 一类的站点，这种方式已经足够简单。

## 3. 在 Jekyll 里怎么放

如果是 Jekyll 站点，最方便的方式一般有两种：

### 3.1 直接写进模板

比如写进统一的页面统计入口：

```html
<script data-goatcounter="https://mapleinori.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
```

只要模板会在文章页和首页渲染，这样访问时就会自动开始统计。

### 3.2 抽成单独的 include

如果项目里本来就有“阅读量 provider”或者“统计 provider”的结构，也可以像我现在这样，单独放进一个自定义 include 文件里。

这样以后切换统计服务时，只需要改这一块。

## 4. 如果想显示“阅读量数字”

只统计后台访问是不够的，有些博客还希望直接在页面上显示：

- 本文阅读量
- 首页文章列表里的阅读量

GoatCounter 官方文档给了两种方式。

### 4.1 用 `visit_count()`

官方推荐的最简单显示方式是：

```html
<script>
  var t = setInterval(function() {
    if (window.goatcounter && window.goatcounter.visit_count) {
      clearInterval(t);
      window.goatcounter.visit_count({append: 'body'});
    }
  }, 100);
</script>
<script data-goatcounter="https://mapleinori.goatcounter.com/count"
        async src="//gc.zgo.at/count.js"></script>
```

这会直接在页面里插入一个 GoatCounter 自带的计数显示块。

适合：

1. 只想快速看到数字
2. 不在意页面样式和结构统一

### 4.2 直接请求 `counter/[PATH].json`

如果你已经有自己的页面结构，比如文章信息栏里固定有一个“阅读量”位置，那更适合用 JSON 接口。

官方文档给的形式是：

```text
https://你的代号.goatcounter.com/counter/[PATH].json
```

例如：

```text
https://mapleinori.goatcounter.com/counter/%2Fdocs%2FUnity%2FSafeArea.json
```

然后前端拿到 JSON 后，把里面的 `count` 写回页面。

一个最基本的例子可以写成这样：

```html
<span id="stats">0</span>

<script>
  let r = new XMLHttpRequest();
  r.addEventListener('load', function() {
    document.querySelector('#stats').innerText = JSON.parse(this.responseText).count;
  });

  let path = '/docs/Unity/SafeArea';
  r.open('GET', 'https://mapleinori.goatcounter.com/counter/' + encodeURIComponent(path) + '.json');
  r.send();
</script>
```

这就是我现在博客里采用的思路：
页面结构自己控制，计数数字自己渲染。

## 5. 为什么会出现 404

GoatCounter 最容易让人困惑的一个点就是：

```text
GET https://mapleinori.goatcounter.com/counter/...json 404
```

这并不一定代表你写错了。

官方文档明确说明了：

1. `counter/[PATH].json` 请求的路径必须和 GoatCounter 里记录的路径完全一致
2. 如果这个路径还没有统计数据，就会返回 `404`

所以出现 404，通常只有两种可能：

### 5.1 这篇文章还没有被 GoatCounter 记录过

比如：

1. 你刚接入 GoatCounter
2. 某篇旧文章还没人访问过
3. 你首页提前去请求它的阅读量

这时它当然会返回 404。

### 5.2 你请求的路径和 GoatCounter 实际记录的路径不一致

例如可能出现这些不一致：

1. `/docs/Unity/SafeArea`
2. `/docs/Unity/SafeArea/`
3. `/2026/04/03/Unity安全区域.html`
4. 是否带 query 参数

只要路径不完全一致，就可能查不到。

## 6. 为什么 canonical 很重要

GoatCounter 官方在 path 文档里特别提到：

它会优先使用页面里的 canonical URL 来决定统计路径。

也就是说，如果页面头部有：

```html
<link rel="canonical" href="https://example.com/path">
```

那 GoatCounter 更倾向于把路径记成：

```text
/path
```

这对博客站点特别重要，因为它能减少这些情况：

1. 同一篇文章因为不同链接形式被记成多条数据
2. 尾部斜杠不一致
3. query 参数把一篇文章拆成多个路径

我的站点模板里本来就有 canonical，这点对 GoatCounter 挺友好。

## 7. Sessions 是什么意思

GoatCounter 默认统计的不是传统的 pageview，而更接近 visit。

官方说明是：

1. `pageview`：每次页面加载都算一次
2. `visit`：同一个人在一段时间内第一次访问这个页面才算一次

这意味着：

1. 刷新十次页面，不会变成十次有效访问
2. 去别的页面再回来，也不一定重复算

所以它默认更像“去重后的访问”。

这个设置在后台这里可以改：

```text
Settings -> Data collection -> Sessions
```

如果关闭它，那么每次页面加载都会更接近传统 pageview。

我自己的理解是：

1. 如果更在意“真实访问”，保留默认即可
2. 如果更想接近旧式“阅读量一直累加”的效果，可以考虑关闭 Sessions

## 8. AdGuard 和广告拦截器的问题

GoatCounter 官方文档明确提醒了：

如果你看不到统计数据，先检查广告拦截器是不是把下面这些域名拦掉了：

1. `goatcounter.com`
2. `gc.zgo.at`

实际使用时，我这边也确实遇到了类似问题：

```text
GET https://gc.zgo.at/count.js net::ERR_BLOCKED_BY_CLIENT
```

后来确认就是浏览器插件拦截。

如果你也遇到这种情况，最直接的做法是把这些加入白名单：

1. 你的站点域名
2. `gc.zgo.at`
3. `你的代号.goatcounter.com`

比如我自己测试时就需要放行：

1. `mapleinori.net`
2. `mapleinori.github.io`
3. `gc.zgo.at`
4. `mapleinori.goatcounter.com`

## 9. 可不可以自己托管 `count.js`

可以。

GoatCounter 官方文档专门写了这一点：
`count.js` 可以自己托管。

比如：

1. 把 `https://gc.zgo.at/count.js` 下载到自己站点
2. 放到 `assets/js/` 之类的位置
3. 再改成站内路径加载

这种做法的好处是：

1. 可以减少对第三方脚本地址的依赖
2. 某些浏览器隐私提示会少一点

但它有一个限制：

1. 就算你自己托管了 `count.js`
2. 真正发统计和读取计数时，还是要访问 GoatCounter 的 `/count` 或 `/counter` 接口

所以广告拦截器问题不一定会完全消失。

## 10. 我最后采用的思路

我自己最后的用法是：

1. 页面访问统计走 GoatCounter
2. 页面内阅读量显示走 `counter/[PATH].json`
3. 保留 canonical
4. 遇到 404 时，接受“旧文章第一次还没统计到”的情况

也就是说：

1. 先让 GoatCounter 能正常开始记录
2. 再让前端去读它的统计数字
3. 某篇文章只要访问过一次，之后再读就不会一直 404

## 11. 总结

如果只想快速上手 GoatCounter，最简单的记法就是：

1. 先加统计脚本
2. 想显示数字就再接 `counter/[PATH].json`
3. canonical 要保持稳定
4. 404 通常是因为路径不一致或还没数据
5. 广告拦截器是最常见的额外问题

对静态博客来说，GoatCounter 的优点主要是：

1. 接入简单
2. 后台轻量
3. 不需要自己搭数据库
4. 既能只看后台，也能继续在前端显示阅读量
