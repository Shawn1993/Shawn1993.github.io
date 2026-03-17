---
date: 2026-03-17
title: 'Core Web Vitals优化手册'
categories: [技术SEO]
tags: [SEO, Ahrefs, 深度文章]
layout: post
---

# Core Web Vitals优化手册：从指标理解到实战优化的完整指南

Core Web Vitals（核心网页指标）是 Google 用于衡量用户在网页上体验的三个关键指标。虽然它们对 SEO 排名的影响相对有限，但对用户体验的影响却是巨大的。本手册将深入解析每个指标的技术原理，并提供可操作的优化策略。

## 引言：Core Web Vitals 的前世今生

### 1.1 什么是 Core Web Vitals

![A dashboard screenshot from Ahrefs Brand Radar showing an overview of Tesla's AI visibility. It displays key metrics like AI Share of Voice (65.0%), and a line graph comparing Tesla's share of voice against competitors like BYD, Lucid, and Rivian over the past year. ](https://ahrefs.com/blog/wp-content/uploads/2025/09/a-dashboard-screenshot-from-ahrefs-brand-radar-sho.png)


Core Web Vitals 是 Google Page Experience 信号的核心组成部分，用于量化用户在网页上的真实体验。这些指标基于 Chrome 用户体验报告（CrUX）的真实用户数据，而非实验室模拟环境。

Google 之所以推出 CWV，是因为传统的性能指标（如"页面加载完成时间"）无法准确反映用户的感知体验。用户可能在页面完全加载之前就开始与内容交互，或者在技术上已"加载完成"的页面上仍然感到卡顿。

自 2021 年 5 月起，移动端页面体验信号（包括 CWV）已正式成为排名因素；2022 年 2 月起，桌面端信号也纳入考量。

### 1.2 三大指标：LCP、CLS、INP

Core Web Vitals 包含三个核心指标：

| 指标 | 衡量维度 | 良好 | 需改进 | 较差 |
|------|----------|------|--------|------|
| **LCP** | 视觉加载速度 | ≤2.5s | >2.5s - ≤4s | >4s |
| **CLS** | 视觉稳定性 | ≤0.1 | >0.1 - ≤0.25 | >0.25 |
| **INP** | 交互响应性 | ≤200ms | >200ms - ≤500ms | >500ms |

- **LCP（Largest Contentful Paint）**：最大内容绘制时间，衡量页面主要内容的加载速度
- **CLS（Cumulative Layout Shift）**：累积布局偏移，衡量页面视觉稳定性
- **INP（Interaction to Next Paint）**：交互到下一次绘制，衡量页面响应用户交互的速度

### 1.3 INP 取代 FID（2024年3月）

2024 年 3 月 12 日，Google 正式用 INP 取代了 FID（First Input Delay，首次输入延迟）作为核心指标。

**为什么做出这个改变？**

FID 只衡量用户**首次**交互的响应时间，忽略了后续交互。一个页面可能首次点击响应很快，但后续操作却很卡顿——FID 无法捕捉这种情况。

INP 则衡量页面**整个生命周期**内所有交互的响应时间，选取响应最慢的交互（或接近最慢的值）作为最终得分。这更全面地反映了用户的真实体验。

### 1.4 CWV 对排名的真实影响

**重要提醒：CWV 对 SEO 排名的影响很小。**

Ahrefs 的研究明确指出："CWV 对 SEO 排名影响很小，更多是微排名因素（tie-breaker）。"这意味着：
- 当两个页面内容质量和相关性相当时，CWV 更好的页面可能略有优势
- 但优质内容 + 糟糕的 CWV 仍然可以超越劣质内容 + 完美的 CWV
- 不要为了追求 CWV 完美分数而牺牲其他更重要的 SEO 工作

**那为什么还要优化 CWV？**
- 用户体验本身就很重要，影响跳出率和转化率
- 是网站质量的信号
- 是值得做的基础优化

---

## 第一章：LCP（Largest Contentful Paint）优化

LCP 是最大内容绘制时间，也是三个指标中**最难优化**的——因为它涉及的技术环节最多。

### 2.1 LCP 的定义与阈值

**定义**：LCP 是视口内最大可见元素完成渲染所需的时间。这个"最大元素"代表页面的主要内容，通常是：
- `<img>` 图片元素
- `<svg>` 内的 `<image>` 元素
- `<video>` 元素的封面图或首帧
- 通过 `url()` 加载的背景图
- 大块文本内容（H1 标题等）

**阈值**：
- **良好**：≤2.5 秒（需要 75% 以上的页面访问达到此标准）
- **需改进**：>2.5 秒且 ≤4 秒
- **较差**：>4 秒

### 2.2 LCP 元素识别方法

优化 LCP 的第一步是知道你的 LCP 元素是什么。

**方法一：Chrome DevTools**
1. 打开 Chrome DevTools（F12）
2. 进入 Performance 面板
3. 录制页面加载过程
4. 查找 "LCP" 标记，悬停可看到对应元素

**方法二：PageSpeed Insights**
1. 访问 [PageSpeed Insights](https://pagespeed.web.dev/)
2. 输入页面 URL
3. 在诊断结果中查看 "Largest Contentful Paint element"

**方法三：Ahrefs Site Audit**
使用 Ahrefs Site Audit 可以批量检测网站所有页面的 CWV 数据，高效发现问题页面。

### 2.3 服务器响应时间优化

LCP 从服务器响应时间开始计时。如果服务器响应慢，一切优化都是徒劳。

**优化策略**：

**1. 使用 CDN**
CDN 将内容缓存到离用户更近的服务器，大幅减少延迟。

**2. 优化服务器配置**
- 升级服务器硬件或更换更快的主机
- 使用更高效的数据库查询
- 启用服务器端缓存

**3. 启用 HTTP/2 或 HTTP/3**
相比 HTTP/1.1，新协议支持多路复用，可并行加载资源。

**4. 预连接关键资源**
```html
<link rel="preconnect" href="https://cdn.example.com">
<link rel="dns-prefetch" href="https://cdn.example.com">
```

### 2.4 图片优化策略

对于大多数网站，LCP 元素是图片。图片优化是 LCP 优化的核心。

![15 reports 2](https://ahrefs.com/blog/wp-content/uploads/2020/02/15-reports-2.png)


#### 2.4.1 图片格式选择（WebP/AVIF）

现代图片格式可以在保持视觉质量的同时大幅减小文件大小：

| 格式 | 压缩率 | 浏览器支持 | 建议 |
|------|--------|------------|------|
| JPEG | 基准 | 所有 | 兜底方案 |
| WebP | 比 JPEG 小 25-34% | 95%+ | 推荐使用 |
| AVIF | 比 WebP 小 20% | 90%+ | 新项目优先 |

```html
<picture>
  <source srcset="image.avif" type="image/avif">
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="描述">
</picture>
```

#### 2.4.2 图片压缩

使用工具压缩图片，平衡质量和大小：
- **Squoosh**（Google 开源，在线使用）
- **TinyPNG/TinyJPG**（在线批量压缩）
- **ImageOptim**（Mac 桌面应用）

#### 2.4.3 响应式图片（srcset）

为不同设备提供不同尺寸的图片：

```html
<img 
  srcset="image-320.jpg 320w,
          image-640.jpg 640w,
          image-1200.jpg 1200w"
  sizes="(max-width: 600px) 100vw, 50vw"
  src="image-640.jpg"
  alt="描述"
>
```

#### 2.4.4 预加载关键图片

对于 LCP 图片，使用 `preload` 让浏览器提前发现和加载：

```html
<link rel="preload" as="image" href="hero-image.jpg">
```

**注意**：只预加载 LCP 图片，过多预加载会适得其反。

### 2.5 渲染阻塞资源消除

CSS 和 JavaScript 可能阻塞页面渲染，延迟 LCP。

**CSS 优化**：
- 内联关键 CSS（首屏所需的最小 CSS）
- 延迟加载非关键 CSS
- 移除未使用的 CSS

**JavaScript 优化**：
- 使用 `async` 或 `defer` 加载非关键脚本
- 将关键脚本内联
- 代码分割，延迟加载非必要模块

```html
<!-- 异步加载，不阻塞解析 -->
<script src="analytics.js" async></script>

<!-- 延迟到 DOM 解析完成后执行 -->
<script src="app.js" defer></script>
```

### 2.6 CDN 配置优化

CDN 不仅加速静态资源，还可以优化 LCP：
- 确保 LCP 图片通过 CDN 分发
- 配置合适的缓存策略
- 使用 CDN 的图片优化功能（自动格式转换、压缩）

### 2.7 字体加载优化

自定义字体可能延迟文本渲染：

**策略一：font-display: swap**
```css
@font-face {
  font-family: 'CustomFont';
  src: url('custom-font.woff2') format('woff2');
  font-display: swap; /* 先显示后备字体，加载完成后切换 */
}
```

**策略二：预加载关键字体**
```html
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>
```

---

## 第二章：CLS（Cumulative Layout Shift）优化

CLS 衡量页面的视觉稳定性——用户最讨厌的体验之一就是"我想点的东西突然跑了"。

### 3.1 CLS 的定义与阈值

**计算公式**：
```
布局偏移分数 = 影响比例 × 距离比例
```
即：偏移元素占视口的比例 × 元素移动的距离占视口的比例

**阈值**：
- **良好**：≤0.1
- **需改进**：>0.1 且 ≤0.25
- **较差**：>0.25

**注意**：用户触发的布局偏移（如点击按钮后出现内容）不计入 CLS。只有意外的、非用户触发的偏移才算。

### 3.2 常见布局偏移原因

#### 3.2.1 无尺寸图片和视频

最常见的 CLS 元凶是没有设置尺寸的图片：

**问题**：
```html
<!-- 图片加载前，浏览器不知道预留多少空间 -->
<img src="image.jpg" alt="描述">
```

**解决**：
```html
<!-- 方法一：直接设置宽高属性 -->
<img src="image.jpg" alt="描述" width="800" height="600">

<!-- 方法二：CSS aspect-ratio -->
<img src="image.jpg" alt="描述" style="aspect-ratio: 4/3; width: 100%;">
```

#### 3.2.2 动态注入内容

异步加载的内容插入页面会推挤现有元素：

**解决方案**：
- 为动态内容预留空间（使用占位符或骨架屏）
- 使用 CSS `min-height` 设置容器最小高度
- 避免在现有内容上方插入内容

#### 3.2.3 字体加载闪烁（FOIT/FOUT）

- **FOIT**（Flash of Invisible Text）：字体加载前文字不可见
- **FOUT**（Flash of Unstyled Text）：字体加载前使用后备字体，加载后切换导致偏移

**解决方案**：
```css
@font-face {
  font-family: 'CustomFont';
  src: url('custom-font.woff2') format('woff2');
  font-display: optional; /* 如果字体在极短时间内未加载，放弃使用 */
}
```

或者使用 `size-adjust` 属性让后备字体和自定义字体大小接近。

#### 3.2.4 广告和嵌入内容

广告是 CLS 的重灾区，因为广告尺寸常常不固定：

**解决方案**：
- 为广告位预留固定空间
- 使用 CSS `min-height` 设置最小高度
- 如果广告加载失败，用占位内容填充

### 3.3 预留空间策略

为所有异步加载的内容预留空间是防止 CLS 的核心策略：

```css
/* 为广告预留空间 */
.ad-slot {
  min-height: 250px;
  background: #f0f0f0;
}

/* 为图片预留空间 */
.image-container {
  aspect-ratio: 16/9;
  background: #f0f0f0;
}
```

### 3.4 字体优化（font-display）

`font-display` 属性控制字体加载行为：

| 值 | 行为 | CLS 影响 |
|----|------|----------|
| `auto` | 浏览器默认 | 不确定 |
| `block` | 短暂隐藏文字，等待字体 | 可能导致 FOIT |
| `swap` | 立即显示后备字体，字体就绪后切换 | 可能导致 CLS |
| `fallback` | 极短等待后使用后备字体 | 平衡方案 |
| `optional` | 极短等待，不保证使用自定义字体 | 最小 CLS |

**建议**：对于大多数网站，`fallback` 或 `optional` 是最佳选择。

### 3.5 bfcache 利用

bfcache（后退/前进缓存）允许浏览器缓存整个页面状态，用户点击后退/前进时立即恢复。

![google-search-console-clicks-performance-dashboard](https://ahrefs.com/blog/wp-content/uploads/2024/03/google-search-console-clicks-performance-dashboard.jpg)


**启用 bfcache 的要点**：
- 不使用 `unload` 事件监听器
- 避免 `Cache-Control: no-store`
- 确保所有资源可以被缓存

bfcache 不仅提升用户体验，还能改善 CLS——因为页面从缓存恢复时不会有布局偏移。

---

## 第三章：INP（Interaction to Next Paint）优化

INP 是 2024 年新加入的核心指标，衡量页面对用户交互的响应速度。

### 4.1 INP 的定义与阈值

**定义**：INP 衡量从用户交互（点击、轻触、按键）到下一次页面更新的时间。

**阈值**：
- **良好**：≤200ms
- **需改进**：>200ms 且 ≤500ms
- **较差**：>500ms

### 4.2 从 FID 到 INP 的转变

FID 和 INP 的关键区别：

| 特性 | FID | INP |
|------|-----|-----|
| 衡量范围 | 首次交互 | 所有交互 |
| 衡量内容 | 输入延迟 | 从输入到视觉更新 |
| 通过难度 | 较易 | 较难 |

Ahrefs 指出，"FID 几乎不需要担心"——因为大多数网站都能轻松通过 FID。但 INP 要求更高，需要更多优化工作。

### 4.3 JavaScript 执行优化

JavaScript 是 INP 问题的主要根源。当主线程被 JavaScript 占用时，页面无法响应用户交互。

#### 4.3.1 代码拆分

将大型 JavaScript 包拆分成小块，按需加载：

```javascript
// 动态导入，只在需要时加载
const module = await import('./heavy-module.js');
```

#### 4.3.2 长任务分解

浏览器将超过 50ms 的任务视为"长任务"，会阻塞主线程。使用 `setTimeout` 或 `requestIdleCallback` 分解长任务：

```javascript
// 将大任务分解成小块
function processLargeArray(items) {
  const chunk = items.splice(0, 100);
  // 处理当前块
  process(chunk);
  
  if (items.length > 0) {
    // 让出主线程，稍后继续
    setTimeout(() => processLargeArray(items), 0);
  }
}
```

#### 4.3.3 主线程优化

- 将计算密集型任务移到 Web Worker
- 使用 `requestAnimationFrame` 进行视觉更新
- 避免同步的 DOM 读取和写入交替（强制重排）

### 4.4 事件处理优化

优化事件处理函数，减少执行时间：

```javascript
// 使用事件委托，减少监听器数量
document.body.addEventListener('click', (e) => {
  if (e.target.matches('.button')) {
    handleClick(e);
  }
});

// 防抖/节流高频事件
const throttledScroll = throttle(handleScroll, 100);
window.addEventListener('scroll', throttledScroll, { passive: true });
```

### 4.5 第三方脚本管理

第三方脚本（分析、广告、聊天工具）是 INP 的隐形杀手：

**策略**：
1. 审计所有第三方脚本，移除不必要的
2. 延迟加载非关键脚本
3. 使用 `loading="lazy"` 加载非必要的 iframe
4. 考虑使用 Partytown 等工具将第三方脚本移到 Web Worker

```html
<!-- 延迟加载第三方脚本 -->
<script>
  window.addEventListener('load', () => {
    const script = document.createElement('script');
    script.src = 'https://third-party.com/widget.js';
    document.body.appendChild(script);
  });
</script>
```

---

## 第四章：测量与监控

"无法测量就无法优化"——建立正确的测量和监控体系是 CWV 优化的基础。

### 5.1 PageSpeed Insights 使用详解

[PageSpeed Insights](https://pagespeed.web.dev/) 是 Google 官方工具，提供：

**真实用户数据（Field Data）**：
- 来自 CrUX 的真实数据
- 反映实际用户体验
- 需要足够流量才有数据

**实验室数据（Lab Data）**：
- Lighthouse 模拟测试
- 可重复，便于调试
- 可能与真实数据有差异

**使用建议**：
- 优先关注真实用户数据
- 使用实验室数据定位问题
- 同时测试移动端和桌面端

### 5.2 CrUX 真实用户数据解读

Chrome User Experience Report（CrUX）是 CWV 数据的权威来源。

![Three traits for effective content marketing reports. ](https://ahrefs.com/blog/wp-content/uploads/2024/03/three-traits-for-effective-content-marketing-repor.png)


**访问 CrUX 数据**：
- PageSpeed Insights（单页面）
- CrUX Dashboard（趋势分析）
- BigQuery（原始数据，高级分析）

**理解数据**：
- CrUX 数据按 75 百分位统计
- 即 75% 的用户体验达到该水平
- 数据按月更新，有一定延迟

### 5.3 Lighthouse 实验室测试

Lighthouse 是 Chrome 内置的性能测试工具：

**使用方法**：
1. 打开 Chrome DevTools
2. 切换到 Lighthouse 面板
3. 选择类别（Performance、Accessibility 等）
4. 点击"Generate report"

**注意事项**：
- 使用隐身模式排除扩展干扰
- 模拟真实网络条件
- 多次测试取平均值

### 5.4 Ahrefs Site Audit 批量检测

Ahrefs 的研究显示，"仅 11.4% 的页面有 CWV 数据"——这是因为 CrUX 只收集有足够流量的页面数据。

Ahrefs Site Audit 可以：
- 批量测试所有页面
- 发现 CrUX 中没有数据的页面问题
- 追踪历史趋势

### 5.5 持续监控与警报设置

建立持续监控机制：

**工具选择**：
- Google Search Console（免费，CrUX 集成）
- WebPageTest（免费，详细分析）
- SpeedCurve / Calibre（付费，全面监控）

**警报策略**：
- CWV 指标降级到"需改进"时报警
- 设置每周/每月报告
- 重大变更后立即测试

---

## 第五章：WordPress 专项优化

WordPress 驱动了超过 40% 的网站，了解其特定优化方法非常重要。

### 6.1 插件精简策略

插件是 WordPress 性能问题的主要来源：

**原则**：
- 每个插件都会增加 JavaScript/CSS 和数据库查询
- 定期审计，删除未使用或可替代的插件
- 选择轻量级、维护良好的插件

**推荐保留**：
- 缓存插件（必需）
- SEO 插件（必需）
- 安全插件（必需）

**考虑删除**：
- 与主题功能重复的插件
- 可用代码片段替代的简单功能
- 长期未更新的插件

### 6.2 缓存插件配置（WPRocket）

缓存是 WordPress 优化的第一步。WP Rocket 是最受推荐的付费缓存插件。

**关键设置**：
- 启用页面缓存
- 启用 GZIP 压缩
- 合并和最小化 CSS/JS
- 延迟加载 JavaScript
- 预加载缓存

**免费替代**：
- LiteSpeed Cache（需要 LiteSpeed 服务器）
- W3 Total Cache
- WP Super Cache

### 6.3 图片延迟加载

WordPress 5.5+ 内置了原生图片延迟加载，但可能需要优化：

```html
<!-- WordPress 默认添加 -->
<img src="image.jpg" loading="lazy" alt="描述">
```

**优化建议**：
- 首屏图片不应延迟加载（会延迟 LCP）
- 使用插件如 Perfmatters 精确控制哪些图片延迟加载

### 6.4 主题选择与优化

主题对性能影响巨大：

**选择标准**：
- 轻量级（避免臃肿的多用途主题）
- 良好的代码质量
- 定期更新
- 最小依赖

**推荐轻量主题**：
- GeneratePress
- Astra
- Kadence
- Blocksy

**优化已有主题**：
- 删除未使用的 CSS/JS
- 禁用不需要的功能
- 使用子主题进行修改

---

## 第六章：常见误区与优先级

### 7.1 不要追求100分

![referring domains top ranking page](https://ahrefs.com/blog/wp-content/uploads/2018/09/referring-domains-top-ranking-page.png)


**误区**：必须让 PageSpeed Insights 达到 100 分。

**现实**：
- 100 分是边际递减的投入
- Ahrefs 研究表明，达到"良好"即可
- 过度优化可能牺牲功能和用户体验
- Google 只区分"良好"、"需改进"、"较差"，不会因为 95 vs 100 给你额外奖励

**正确姿势**：确保 75% 以上的用户体验达到"良好"阈值。

### 7.2 用户所在国家对 CWV 影响

Ahrefs 的研究揭示了一个重要发现："用户所在国家对 CWV 影响很大，与设备偏好和网络基础设施相关。"

**数据**：
- 约 33% 的网站通过 CWV 阈值
- 美国排名第 38 位，通过率 41%
- 3G 或更慢连接的网站几乎无法通过 CWV

**启示**：
- 了解你的用户主要来自哪里
- 针对目标市场的网络条件优化
- 在目标地区部署 CDN 节点

### 7.3 移动端 vs 桌面端数据差异

移动端 CWV 通常比桌面端差：
- 处理能力更低
- 网络条件更不稳定
- 屏幕尺寸导致不同的 LCP 元素

**策略**：
- 优先优化移动端（Google 使用移动优先索引）
- 不要只看桌面端数据就认为万事大吉

### 7.4 投入产出比评估框架

**优先级排序**：

| 优先级 | 问题类型 | 投入 | 产出 |
|--------|----------|------|------|
| P0 | 服务器响应慢 | 中 | 高（影响所有指标） |
| P1 | 未设置图片尺寸 | 低 | 高（直接改善 CLS） |
| P1 | LCP 图片未优化 | 中 | 高 |
| P2 | 第三方脚本过多 | 中 | 中 |
| P3 | 字体优化 | 低 | 低 |

**原则**：先解决影响范围大、修复成本低的问题。

---

## 结语：CWV 优化的正确姿势

Core Web Vitals 优化是一场马拉松，不是冲刺。以下是总结的最佳实践：

### 核心原则

1. **关注真实用户数据**：CrUX 数据比 Lighthouse 分数更重要
2. **设定合理目标**：达到"良好"即可，不必追求完美
3. **优先移动端**：Google 使用移动优先索引
4. **持续监控**：性能会随代码变更而退化

### 快速检查清单

**LCP 优化**：
- [ ] LCP 图片使用现代格式（WebP/AVIF）
- [ ] LCP 图片已预加载
- [ ] 服务器响应时间 <200ms
- [ ] 使用 CDN

**CLS 优化**：
- [ ] 所有图片和视频设置了尺寸
- [ ] 广告位预留了空间
- [ ] 字体使用 font-display: optional/fallback

**INP 优化**：
- [ ] 无超过 50ms 的长任务
- [ ] 第三方脚本已延迟加载
- [ ] 关键事件处理优化

### 记住

CWV 只是 SEO 的一小部分。Ahrefs 明确指出它对排名的影响有限。把 CWV 优化好是专业的体现，但不要让它占用应该用于内容创作和外链建设的时间。

---

## 参考来源

1. [What Are Core Web Vitals (CWVs) & How To Improve Them](https://ahrefs.com/blog/core-web-vitals/) - Ahrefs Blog
2. [Core Web Vitals Data Study w/ CrUX & 5.2M Pages](https://ahrefs.com/blog/core-web-vitals-study/) - Ahrefs Blog
3. [What Is Largest Contentful Paint (LCP) & How To Improve It](https://ahrefs.com/blog/largest-contentful-paint-lcp/) - Ahrefs Blog
4. [What Is Cumulative Layout Shift (CLS) & How To Improve It](https://ahrefs.com/blog/cumulative-layout-shift-cls/) - Ahrefs Blog
5. [Improving First Input Delay (FID): Tips For Faster Interactions](https://ahrefs.com/blog/first-input-delay-fid/) - Ahrefs Blog
6. [Google PageSpeed Insights For SEOs & Developers](https://ahrefs.com/blog/pagespeed-insights/) - Ahrefs Blog
7. [How to Speed Up Your WordPress Website in 20 Minutes](https://ahrefs.com/blog/speed-up-wordpress/) - Ahrefs Blog
8. [Mobile SEO: 10 Optimization Tips](https://ahrefs.com/blog/mobile-seo/) - Ahrefs Blog
