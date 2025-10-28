---
comments: true
---

<link rel="stylesheet" href="css/graph.css">

# 主页

hello, world.

我是田柏汀。

这里网站也许会放一些东西。

## 知识图谱

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

## 序




## 我的站点
- [bilibili](https://space.bilibili.com/255797047)
- [zhihu](https://www.zhihu.com/people/tian-bu-ding-45-77)


