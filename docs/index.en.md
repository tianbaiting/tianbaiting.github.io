---
comments: true
---

<link rel="stylesheet" href="css/graph.css">

# main

hello, world.

I'am Tian Baiting.


## Preface




## my web
- [bilibili](https://space.bilibili.com/255797047)
- [zhihu](https://www.zhihu.com/people/tian-bu-ding-45-77)
 - [google scholar](https://scholar.google.com/citations?hl=zh-CN&user=Wb4CcQ8AAAAJ)
 - [orcid](https://orcid.org/0000-0002-9018-6480)

<!-- ORCID card placeholder -->
<div id="orcid-card" data-orcid="0000-0002-9018-6480" style="margin:0.6rem 0;"></div>

<!-- Google Scholar card placeholder -->
<div id="scholar-card" data-user="Wb4CcQ8AAAAJ" style="margin:0.6rem 0;"></div>



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
<script src="js/orcid-card.js"></script>
<script src="js/scholar-card.js"></script>
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