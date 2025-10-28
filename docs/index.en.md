---
comments: true
---

<link rel="stylesheet" href="css/graph.css">

# main

hello, world.

I'am Tian Baiting.

## Knowledge Graph

<div class="graph-container">
    <div class="graph-controls">
        <div class="control-group">
            <label for="language-filter">Language Filter:</label>
            <select id="language-filter">
                <option value="all">All</option>
                <option value="zh">Chinese</option>
                <option value="en" selected>English</option>
            </select>
        </div>
        <div class="control-group">
            <label for="search-input">Search:</label>
            <input type="text" id="search-input" placeholder="Enter node name...">
        </div>
        <div class="control-group">
            <button id="reset-zoom">Reset View</button>
        </div>
    </div>
    <div id="knowledge-graph"></div>
    <div class="graph-info">
        <div class="info-panel">
            <h3>Graph Info</h3>
            <p>Nodes: <span id="node-count">0</span></p>
            <p>Links: <span id="link-count">0</span></p>
        </div>
    </div>
</div>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="js/graph.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
    // Initialize graph after page load
    if (typeof KnowledgeGraph !== 'undefined') {
        fetch('js/graph-data.json')
            .then(response => response.json())
            .then(data => {
                const graph = new KnowledgeGraph('knowledge-graph', data);
                // Default to show English content
                graph.filterByLanguage('en');
            })
            .catch(error => {
                console.error('Error loading graph data:', error);
            });
    }
});
</script>

## Preface




## my web
- [bilibili](https://space.bilibili.com/255797047)
- [zhihu](https://www.zhihu.com/people/tian-bu-ding-45-77)


