---
title: 主页
comments: true
---

<link rel="stylesheet" href="css/graph.css">

# 主页

hello, world.

我是田柏汀。一个兴趣使然的**。

![alt text](assets/image.png)

这里网站也许会放一些东西。


## 序

我觉得应该有另外一些方式组织知识的结构。

我不喜欢视频,pdf，检索起来十分费劲。而且有太多冗余信息了。

## 博文网格

<div class="graph-container">
    <div class="graph-controls">
        <div class="control-group">
            <label for="language-filter">语言过滤:</label>
            <select id="language-filter">
                <option value="all">全部</option>
                <option value="zh" selected>中文</option>
                <option value="en">英文</option>
            </select>
        </div>
        <div class="control-group">
            <label for="search-input">搜索:</label>
            <input type="text" id="search-input" placeholder="输入节点名称...">
        </div>
        <div class="control-group">
            <button id="reset-zoom">重置视图</button>
        </div>
    </div>
    <div id="knowledge-graph"></div>
    <div class="graph-info">
        <div class="info-panel">
            <h3>图谱信息</h3>
            <p>节点数量: <span id="node-count">0</span></p>
            <p>连接数量: <span id="link-count">0</span></p>
        </div>
    </div>
</div>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="js/graph.js"></script>
<script src="js/orcid-card.js"></script>
<script src="js/scholar-card.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
    // 确保在页面加载完成后初始化图谱
    if (typeof KnowledgeGraph !== 'undefined') {
        fetch('js/graph-data.json')
            .then(response => response.json())
            .then(data => {
                const graph = new KnowledgeGraph('knowledge-graph', data);
                // 默认显示中文内容
                graph.filterByLanguage('zh');
            })
            .catch(error => {
                console.error('Error loading graph data:', error);
            });
    }
});
</script>




## 我的站点

- [bilibili](https://space.bilibili.com/255797047)
- [zhihu](https://www.zhihu.com/people/tian-bu-ding-45-77)

- [github](https://github.com/tianbaiting)


<div align="center">
  <a href="https://github.com/tianbaiting">
    <img src="https://github-readme-stats.vercel.app/api?username=tianbaiting&show_icons=true&theme=radical&include_all_commits=true&count_private=true&line_height=25" alt="GitHub Stats" height="180px"/>
  </a>
  <a href="https://github.com/tianbaiting">
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=tianbaiting&layout=compact&theme=radical&langs_count=8" alt="Top Languages" height="180px"/>
  </a>
</div>



### 科研相关的主页

### ORCID
<!-- ORCID card placeholder -->
<div id="orcid-card" data-orcid="0000-0002-9018-6480" style="margin:0.6rem 0;"></div>

### 谷歌学术

[google scholar](https://scholar.google.com/citations?hl=zh-CN&user=Wb4CcQ8AAAAJ)

<!-- Google Scholar card placeholder -->
<div id="scholar-card" data-user="Wb4CcQ8AAAAJ" style="margin:0.6rem 0;"></div>


以上都是自动抓取的论文列表








