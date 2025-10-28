/**
 * 知识图谱可视化组件
 * 支持中英文分离显示，交互式节点操作
 */
class KnowledgeGraph {
  constructor(containerId, options = {}) {
    this.container = d3.select(containerId);
    this.width = options.width || 800;
    this.height = options.height || 600;
    this.currentLanguage = options.language || 'all';
    this.searchTerm = '';
    
    this.data = { nodes: [], links: [] };
    this.filteredData = { nodes: [], links: [] };
    
    this.init();
  }

  init() {
    this.createControls();
    this.createSVG();
    this.createTooltip();
    this.createLegend();
    this.setupSimulation();
    this.loadData();
  }

  createControls() {
    // 语言切换控制
    const controls = this.container.append('div')
      .attr('class', 'graph-controls');
    
    // 语言过滤按钮
    controls.append('button')
      .text('🌐 全部')
      .attr('class', 'active')
      .on('click', () => this.setLanguageFilter('all'));
    
    controls.append('button')
      .text('🇨🇳 中文')
      .on('click', () => this.setLanguageFilter('zh'));
    
    controls.append('button')
      .text('🇺🇸 English')
      .on('click', () => this.setLanguageFilter('en'));
    
    // 适应画布按钮
    controls.append('button')
      .text('📐 适应画布')
      .on('click', () => this.fitToContainer());
    
    // 全屏按钮
    controls.append('button')
      .text('🔍 全屏')
      .attr('class', 'fullscreen-btn')
      .on('click', () => this.toggleFullscreen());

    // 搜索框
    const searchDiv = this.container
      .insert('div', '*')
      .attr('class', 'graph-search');

    searchDiv.append('input')
      .attr('type', 'text')
      .attr('placeholder', '搜索节点... Search nodes...')
      .on('input', (event) => {
        this.searchTerm = event.target.value.toLowerCase();
        this.updateVisualization();
      });
  }

  createSVG() {
    this.svg = this.container
      .append('div')
      .attr('class', 'graph-container')
      .append('svg')
      .attr('class', 'graph-svg')
      .attr('viewBox', `0 0 ${this.width} ${this.height}`);

    // 创建缩放行为
    this.zoom = d3.zoom()
      .scaleExtent([0.1, 4])
      .on('zoom', (event) => {
        this.g.attr('transform', event.transform);
      });

    this.svg.call(this.zoom);

    // 创建主绘图组
    this.g = this.svg.append('g');

    // 创建链接组
    this.linkGroup = this.g.append('g').attr('class', 'links');
    
    // 创建节点组
    this.nodeGroup = this.g.append('g').attr('class', 'nodes');
  }

  createTooltip() {
    this.tooltip = d3.select('body').append('div')
      .attr('class', 'graph-tooltip')
      .style('position', 'absolute')
      .style('visibility', 'hidden');
  }

  createLegend() {
    const legend = this.container.select('.graph-container')
      .append('div')
      .attr('class', 'graph-legend');

    legend.append('div')
      .attr('class', 'graph-legend-item')
      .html('<span class="graph-legend-color" style="background: #3f51b5;"></span>中文内容');

    legend.append('div')
      .attr('class', 'graph-legend-item')
      .html('<span class="graph-legend-color" style="background: #e91e63;"></span>English Content');

    legend.append('div')
      .attr('class', 'graph-legend-item')
      .html('<span class="graph-legend-color" style="background: #ff9800;"></span>高亮/Highlighted');
  }

  setupSimulation() {
    this.simulation = d3.forceSimulation()
      .force('link', d3.forceLink().id(d => d.id).distance(100))
      .force('charge', d3.forceManyBody().strength(-300))
      .force('center', d3.forceCenter(this.width / 2, this.height / 2))
      .force('collision', d3.forceCollide().radius(30));
  }

  async loadData() {
    try {
      // 首先尝试从生成的JSON文件加载数据
      const response = await fetch('/js/graph-data.json');
      if (response.ok) {
        this.data = await response.json();
      } else {
        // 如果没有找到JSON文件，使用示例数据
        this.data = this.getExampleData();
      }
    } catch (error) {
      console.warn('Failed to load graph data, using example data:', error);
      this.data = this.getExampleData();
    }
    
    this.updateVisualization();
  }

  getExampleData() {
    // 基于当前文档结构的示例数据
    return {
      nodes: [
        // 主页面
        { id: 'index.zh', title: '首页', language: 'zh', category: 'main', path: 'index.zh.md' },
        { id: 'index.en', title: 'Home', language: 'en', category: 'main', path: 'index.en.md' },
        
        // 主要分类
        { id: 'life', title: '生活', language: 'zh', category: 'category', path: 'life/' },
        { id: 'sci', title: '科研', language: 'zh', category: 'category', path: 'sci/' },
        { id: 'MickeyMiaoMiao', title: '技术分享', language: 'zh', category: 'category', path: 'MickeyMiaoMiao/' },
        { id: 'japanese', title: '日本生存指南', language: 'zh', category: 'category', path: '日本生存指南/' },
        
        // 生活分类下的页面
        { id: 'anxiety', title: '焦虑', language: 'zh', category: 'page', path: 'life/焦虑.zh.md' },
        { id: 'food-safety', title: '食物安全温度', language: 'zh', category: 'page', path: 'life/食物安全温度.zh.md' },
        { id: 'flavor', title: '调味', language: 'zh', category: 'page', path: 'life/flavor.zh.md' },
        { id: 'workout', title: '健身饮食', language: 'zh', category: 'page', path: 'life/健康/workout_diet.zh.md' },
        
        // 科研分类下的页面
        { id: 'docker', title: 'Docker使用', language: 'zh', category: 'page', path: 'sci/cheatshet/docker.zh.md' },
        { id: 'git', title: 'Git使用', language: 'zh', category: 'page', path: 'sci/cheatshet/git.zh.md' },
        { id: 'python-class', title: 'Python类定义', language: 'zh', category: 'page', path: 'sci/minimal_code/python_def_class.zh.md' },
        { id: 'latex-graphics', title: 'LaTeX绘图', language: 'zh', category: 'page', path: 'sci/minimal_code/latex_graphics.zh.md' },
        
        // 英文页面示例
        { id: 'docker-en', title: 'Docker Guide', language: 'en', category: 'page', path: 'sci/cheatshet/docker.en.md' },
        { id: 'git-en', title: 'Git Guide', language: 'en', category: 'page', path: 'sci/cheatshet/git.en.md' },
        { id: 'jupyter-en', title: 'Jupyter Notebook', language: 'en', category: 'page', path: 'sci/minimal_code/jupyternotebook.en.md' },
      ],
      links: [
        // 主页连接到分类
        { source: 'index.zh', target: 'life' },
        { source: 'index.zh', target: 'sci' },
        { source: 'index.zh', target: 'MickeyMiaoMiao' },
        { source: 'index.zh', target: 'japanese' },
        
        // 分类连接到页面
        { source: 'life', target: 'anxiety' },
        { source: 'life', target: 'food-safety' },
        { source: 'life', target: 'flavor' },
        { source: 'life', target: 'workout' },
        
        { source: 'sci', target: 'docker' },
        { source: 'sci', target: 'git' },
        { source: 'sci', target: 'python-class' },
        { source: 'sci', target: 'latex-graphics' },
        
        // 英文页面连接
        { source: 'index.en', target: 'docker-en' },
        { source: 'index.en', target: 'git-en' },
        { source: 'index.en', target: 'jupyter-en' },
        
        // 相关页面之间的连接
        { source: 'docker', target: 'docker-en' },
        { source: 'git', target: 'git-en' },
        { source: 'food-safety', target: 'flavor' },
      ]
    };
  }

  filterData() {
    let nodes = [...this.data.nodes];
    let links = [...this.data.links];

    // 语言过滤
    if (this.currentLanguage !== 'all') {
      nodes = nodes.filter(node => node.language === this.currentLanguage);
      const nodeIds = new Set(nodes.map(node => node.id));
      links = links.filter(link => 
        nodeIds.has(link.source.id || link.source) && 
        nodeIds.has(link.target.id || link.target)
      );
    }

    // 搜索过滤
    if (this.searchTerm) {
      const matchedNodes = nodes.filter(node => 
        node.title.toLowerCase().includes(this.searchTerm) ||
        node.id.toLowerCase().includes(this.searchTerm)
      );
      
      // 包含匹配节点和它们的邻居
      const matchedIds = new Set(matchedNodes.map(node => node.id));
      const neighborIds = new Set();
      
      links.forEach(link => {
        const sourceId = link.source.id || link.source;
        const targetId = link.target.id || link.target;
        
        if (matchedIds.has(sourceId)) {
          neighborIds.add(targetId);
        }
        if (matchedIds.has(targetId)) {
          neighborIds.add(sourceId);
        }
      });
      
      matchedIds.forEach(id => neighborIds.add(id));
      
      nodes = nodes.filter(node => neighborIds.has(node.id));
      const finalNodeIds = new Set(nodes.map(node => node.id));
      links = links.filter(link => 
        finalNodeIds.has(link.source.id || link.source) && 
        finalNodeIds.has(link.target.id || link.target)
      );
    }

    return { nodes, links };
  }

  updateVisualization() {
    this.filteredData = this.filterData();
    this.render();
  }

  render() {
    const { nodes, links } = this.filteredData;

    // 更新链接
    const link = this.linkGroup
      .selectAll('line')
      .data(links, d => `${d.source.id || d.source}-${d.target.id || d.target}`);

    link.exit().remove();

    const linkEnter = link.enter().append('line')
      .attr('class', 'link');

    const linkMerge = linkEnter.merge(link);

    // 更新节点
    const node = this.nodeGroup
      .selectAll('g')
      .data(nodes, d => d.id);

    node.exit().remove();

    const nodeEnter = node.enter().append('g')
      .attr('class', 'node-group');

    // 添加圆形节点
    nodeEnter.append('circle')
      .attr('class', d => `node ${d.language} ${d.category}`)
      .attr('r', d => this.getNodeRadius(d))
      .on('mouseover', (event, d) => this.showTooltip(event, d))
      .on('mouseout', () => this.hideTooltip())
      .on('click', (event, d) => this.onNodeClick(event, d))
      .call(this.drag());

    // 添加文本标签
    nodeEnter.append('text')
      .attr('class', 'node-text')
      .attr('dy', '.35em')
      .text(d => d.title);

    const nodeMerge = nodeEnter.merge(node);

    // 更新节点样式
    nodeMerge.select('circle')
      .attr('class', d => {
        let classes = `node ${d.language} ${d.category}`;
        if (this.searchTerm && (
          d.title.toLowerCase().includes(this.searchTerm) ||
          d.id.toLowerCase().includes(this.searchTerm)
        )) {
          classes += ' highlighted';
        }
        return classes;
      });

    // 更新仿真
    this.simulation.nodes(nodes);
    this.simulation.force('link').links(links);

    this.simulation.on('tick', () => {
      linkMerge
        .attr('x1', d => d.source.x)
        .attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x)
        .attr('y2', d => d.target.y);

      nodeMerge
        .attr('transform', d => `translate(${d.x},${d.y})`);
    });

    this.simulation.alpha(0.3).restart();
  }

  getNodeRadius(d) {
    switch (d.category) {
      case 'main': return 25;
      case 'category': return 20;
      case 'page': return 15;
      default: return 15;
    }
  }

  showTooltip(event, d) {
    this.tooltip
      .style('visibility', 'visible')
      .html(`
        <strong>${d.title}</strong><br/>
        语言: ${d.language === 'zh' ? '中文' : 'English'}<br/>
        类型: ${this.getCategoryName(d.category)}<br/>
        路径: ${d.path || 'N/A'}
      `)
      .style('left', (event.pageX + 10) + 'px')
      .style('top', (event.pageY - 10) + 'px');
  }

  hideTooltip() {
    this.tooltip.style('visibility', 'hidden');
  }

  getCategoryName(category) {
    const names = {
      'main': '主页/Main',
      'category': '分类/Category',
      'page': '页面/Page'
    };
    return names[category] || category;
  }

  onNodeClick(event, d) {
    // 如果节点有路径信息，尝试跳转
    // 优先使用后端生成的 url 字段（已经考虑了默认语言前缀），否则回退到 path 的推断
    let url = null;
    if (d.url) {
      url = d.url;
    } else if (d.path) {
      // 构建正确的URL
      url = d.path;
      if (!url.endsWith('/') && !url.endsWith('.md')) {
        url += '/';
      }
      if (url.endsWith('.md')) {
        url = url.replace('.md', '/');
      }
      // 如果是相对路径，添加基础路径
      if (!url.startsWith('http')) {
        url = '/' + url.replace(/^\/+/, '');
      }
    }

    if (url) {
      // 规范化
      url = url.replace(/\/\\+/g, '/');
      console.log('Navigating to:', url);
      window.open(url, '_blank');
    }
  }

  switchLanguage(language) {
    this.currentLanguage = language;
    
    // 更新按钮状态
    this.container.selectAll('.graph-controls button')
      .classed('active', false);
    
    const buttons = this.container.selectAll('.graph-controls button').nodes();
    if (language === 'all') {
      d3.select(buttons[0]).classed('active', true);
    } else if (language === 'zh') {
      d3.select(buttons[1]).classed('active', true);
    } else if (language === 'en') {
      d3.select(buttons[2]).classed('active', true);
    }

    this.updateVisualization();
  }

  drag() {
    return d3.drag()
      .on('start', (event, d) => {
        if (!event.active) this.simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
      })
      .on('drag', (event, d) => {
        d.fx = event.x;
        d.fy = event.y;
      })
      .on('end', (event, d) => {
        if (!event.active) this.simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
      });
  }

  // 公共方法：重置缩放
  resetZoom() {
    this.svg.transition().duration(750).call(
      this.zoom.transform,
      d3.zoomIdentity
    );
  }

  // 公共方法：适应画布大小
  fitToContainer() {
    const bounds = this.g.node().getBBox();
    const fullWidth = this.width;
    const fullHeight = this.height;
    const width = bounds.width;
    const height = bounds.height;
    const midX = bounds.x + width / 2;
    const midY = bounds.y + height / 2;
    
    if (width === 0 || height === 0) return;
    
    const scale = Math.min(fullWidth / width, fullHeight / height) * 0.9;
    const translate = [fullWidth / 2 - scale * midX, fullHeight / 2 - scale * midY];
    
    this.svg.transition().duration(750).call(
      this.zoom.transform,
      d3.zoomIdentity.translate(translate[0], translate[1]).scale(scale)
    );
  }

  // 全屏功能
  toggleFullscreen() {
    const container = this.container.node();
    const isFullscreen = container.classList.contains('graph-fullscreen');
    
    if (isFullscreen) {
      this.exitFullscreen();
    } else {
      this.enterFullscreen();
    }
  }

  enterFullscreen() {
    const container = this.container.node();
    
    // 添加全屏样式类
    container.classList.add('graph-fullscreen');
    document.body.classList.add('graph-fullscreen-active');
    
    // 更新图谱尺寸
    const newWidth = window.innerWidth - 40;
    const newHeight = window.innerHeight - 120;
    this.width = newWidth;
    this.height = newHeight;
    
    // 更新SVG viewBox和仿真中心
    this.svg.attr('viewBox', `0 0 ${newWidth} ${newHeight}`);
    this.simulation.force('center', d3.forceCenter(newWidth / 2, newHeight / 2));
    this.simulation.alpha(0.3).restart();
    
    // 添加退出提示
    const hint = d3.select('body').append('div')
      .attr('class', 'fullscreen-hint')
      .text('按 ESC 键或点击 × 退出全屏');
    
    // 3秒后自动移除提示
    setTimeout(() => {
      hint.remove();
    }, 3000);
    
    // 更新全屏按钮文字
    this.container.select('.fullscreen-btn')
      .text('× 退出全屏');
    
    // 添加ESC键监听
    this.escKeyHandler = (event) => {
      if (event.key === 'Escape') {
        this.exitFullscreen();
      }
    };
    document.addEventListener('keydown', this.escKeyHandler);
    
    // 添加窗口大小变化监听
    this.resizeHandler = () => {
      if (container.classList.contains('graph-fullscreen')) {
        const newWidth = window.innerWidth - 40;
        const newHeight = window.innerHeight - 120;
        this.width = newWidth;
        this.height = newHeight;
        this.svg.attr('viewBox', `0 0 ${newWidth} ${newHeight}`);
        this.simulation.force('center', d3.forceCenter(newWidth / 2, newHeight / 2));
        this.simulation.alpha(0.1).restart();
      }
    };
    window.addEventListener('resize', this.resizeHandler);
  }

  exitFullscreen() {
    const container = this.container.node();
    
    // 移除全屏样式类
    container.classList.remove('graph-fullscreen');
    document.body.classList.remove('graph-fullscreen-active');
    
    // 恢复原始尺寸
    this.width = 800;
    this.height = 600;
    
    // 更新SVG viewBox和仿真中心
    this.svg.attr('viewBox', `0 0 ${this.width} ${this.height}`);
    this.simulation.force('center', d3.forceCenter(this.width / 2, this.height / 2));
    this.simulation.alpha(0.3).restart();
    
    // 更新全屏按钮文字
    this.container.select('.fullscreen-btn')
      .text('🔍 全屏');
    
    // 移除事件监听器
    if (this.escKeyHandler) {
      document.removeEventListener('keydown', this.escKeyHandler);
      this.escKeyHandler = null;
    }
    
    if (this.resizeHandler) {
      window.removeEventListener('resize', this.resizeHandler);
      this.resizeHandler = null;
    }
    
    // 移除可能残留的提示
    d3.selectAll('.fullscreen-hint').remove();
  }
}

// 页面加载完成后初始化图谱
document.addEventListener('DOMContentLoaded', function() {
  // 检查是否存在图谱容器
  const graphContainer = document.getElementById('knowledge-graph');
  if (graphContainer) {
    // 获取当前页面语言
    const currentLang = document.documentElement.lang || 'zh';
    
    // 初始化知识图谱
    const graph = new KnowledgeGraph('#knowledge-graph', {
      language: 'all', // 默认显示所有内容
      width: 800,
      height: 600
    });
    
    // 添加全局变量以便在控制台中调试
    window.knowledgeGraph = graph;
    
    // 添加键盘快捷键
    document.addEventListener('keydown', function(event) {
      if (event.ctrlKey || event.metaKey) {
        switch(event.key) {
          case '0':
            event.preventDefault();
            graph.resetZoom();
            break;
          case '9':
            event.preventDefault();
            graph.fitToContainer();
            break;
        }
      }
    });
  }
});

// 导出类以供其他模块使用
if (typeof module !== 'undefined' && module.exports) {
  module.exports = KnowledgeGraph;
}