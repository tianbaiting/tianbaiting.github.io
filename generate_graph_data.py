#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MkDocs 知识图谱数据生成器

该脚本分析docs目录下的Markdown文件，提取文档结构和内部链接关系，
生成用于知识图谱可视化的JSON数据文件。

功能特性：
- 自动识别中英文文档
- 提取内部链接和Roam-style链接 [[]]
- 生成分层的文档结构
- 支持自定义过滤规则

作者: TBT
日期: 2025-10-28
"""

import os
import json
import re
import logging
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from urllib.parse import unquote

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GraphDataGenerator:
    """知识图谱数据生成器"""
    
    def __init__(self, docs_path: str = 'docs', output_path: str = 'docs/js/graph-data.json'):
        self.docs_path = Path(docs_path)
        self.output_path = Path(output_path)
        self.nodes = []
        self.links = []
        self.processed_files = set()
        # 默认语言（用于生成站点 URL）
        self.default_language = 'zh'
        
        # 文件类型映射
        self.category_mapping = {
            'index': 'main',
            'README': 'main',
            '首页': 'main',
            'Home': 'main',
        }
        
        # 需要排除的文件和目录
        self.exclude_patterns = {
            '*.tmp', '*.pdf', '*.gz', '*.zip', '*.tar',
            '__pycache__', '.git', '.vscode', 'node_modules',
            'site', '.pytest_cache', '*.pyc'
        }
        
        # 需要排除的文件名
        self.exclude_files = {
            'google0ec64d869ee59589.html',
            'robots.txt',
            'base.html.txt'
        }

    def should_exclude(self, path: Path) -> bool:
        """检查路径是否应该被排除"""
        # 检查文件名
        if path.name in self.exclude_files:
            return True
            
        # 检查扩展名和模式
        for pattern in self.exclude_patterns:
            if path.match(pattern) or any(part.startswith('.') for part in path.parts):
                return True
                
        return False

    def detect_language(self, file_path: Path) -> str:
        """检测文件语言"""
        path_str = str(file_path)
        name = file_path.name
        
        # 基于文件名后缀判断
        if name.endswith('.zh.md') or '.zh.' in name:
            return 'zh'
        elif name.endswith('.en.md') or '.en.' in name:
            return 'en'
            
        # 基于路径判断
        if '/zh/' in path_str or path_str.startswith('zh/'):
            return 'zh'
        elif '/en/' in path_str or path_str.startswith('en/'):
            return 'en'
            
        # 基于内容判断（简单的启发式方法）
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read(500)  # 只读取前500字符
                
            # 计算中文字符比例
            chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', content))
            total_chars = len(re.findall(r'[a-zA-Z\u4e00-\u9fff]', content))
            
            if total_chars > 0:
                chinese_ratio = chinese_chars / total_chars
                return 'zh' if chinese_ratio > 0.3 else 'en'
        except Exception as e:
            logger.warning(f"Error detecting language for {file_path}: {e}")
            
        # 默认为中文（根据网站主要语言）
        return 'zh'

    def determine_category(self, file_path: Path, content: str = "") -> str:
        """确定节点类别"""
        name = file_path.stem
        
        # 主页面
        for main_keyword in self.category_mapping:
            if main_keyword.lower() in name.lower():
                return 'main'
                
        # 根据路径深度和位置判断
        relative_path = file_path.relative_to(self.docs_path)
        path_parts = relative_path.parts
        
        # 一级目录下的index文件
        if len(path_parts) == 2 and name.lower() in ['index', 'readme']:
            return 'category'
            
        # 目录级别的页面
        if len(path_parts) <= 2:
            return 'category'
            
        return 'page'

    def extract_title(self, file_path: Path, content: str) -> str:
        """提取页面标题"""
        # 从内容中提取H1标题
        h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if h1_match:
            return h1_match.group(1).strip()
            
        # 从文件名生成标题
        name = file_path.stem
        
        # 移除语言后缀
        name = re.sub(r'\.(zh|en)$', '', name)
        
        # 替换常见分隔符
        name = re.sub(r'[-_]', ' ', name)
        
        # 首字母大写
        return name.title() if name else "未命名页面"

    def extract_links(self, file_path: Path, content: str) -> List[Tuple[str, str]]:
        """从markdown内容中提取链接"""
        links = []
        
        # 提取标准markdown链接 [text](link.md)
        md_links = re.findall(r'\[([^\]]+)\]\(([^)]+\.md(?:#[^)]*)?)\)', content)
        for text, link in md_links:
            # 清理链接
            link = unquote(link.split('#')[0])  # 移除锚点
            if not link.startswith('http'):  # 只处理相对链接
                links.append((text, link))
                
        # 提取Roam-style链接 [[link]]
        roam_links = re.findall(r'\[\[([^\]]+)\]\]', content)
        for link in roam_links:
            links.append((link, f"{link}.md"))
            
        # 提取Obsidian-style链接 [[link|alias]]
        obsidian_links = re.findall(r'\[\[([^|\]]+)\|([^\]]+)\]\]', content)
        for link, alias in obsidian_links:
            links.append((alias, f"{link}.md"))
            
        return links

    def resolve_link_target(self, source_path: Path, link_path: str) -> Optional[str]:
        """解析链接目标的实际路径"""
        try:
            # 处理相对路径
            if link_path.startswith('./') or link_path.startswith('../'):
                target_path = (source_path.parent / link_path).resolve()
            else:
                # 尝试在docs目录下查找
                target_path = self.docs_path / link_path
                if not target_path.exists():
                    # 尝试相对于源文件的路径
                    target_path = (source_path.parent / link_path).resolve()
                    
            if target_path.exists() and target_path.suffix == '.md':
                return str(target_path.relative_to(self.docs_path))
                
        except Exception as e:
            logger.debug(f"Error resolving link {link_path} from {source_path}: {e}")
            
        return None

    def generate_node_id(self, file_path: Path) -> str:
        """生成节点ID"""
        relative_path = file_path.relative_to(self.docs_path)
        return str(relative_path).replace('.md', '').replace('\\', '/')

    def scan_directory(self) -> None:
        """扫描docs目录生成节点和链接"""
        logger.info(f"Scanning directory: {self.docs_path}")
        
        # 遍历所有markdown文件
        for md_file in self.docs_path.rglob('*.md'):
            if self.should_exclude(md_file):
                logger.debug(f"Excluding file: {md_file}")
                continue
                
            try:
                # 读取文件内容
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # 生成节点信息
                node_id = self.generate_node_id(md_file)
                language = self.detect_language(md_file)
                category = self.determine_category(md_file, content)
                title = self.extract_title(md_file, content)
                
                node = {
                    'id': node_id,
                    'title': title,
                    'language': language,
                    'category': category,
                    'path': str(md_file.relative_to(self.docs_path)),
                    'size': len(content)  # 文件大小，可用于调整节点大小
                }
                
                self.nodes.append(node)
                self.processed_files.add(node_id)
                
                # 提取链接
                links = self.extract_links(md_file, content)
                for link_text, link_path in links:
                    target_id = self.resolve_link_target(md_file, link_path)
                    if target_id:
                        target_id = target_id.replace('.md', '').replace('\\', '/')
                        
                        link = {
                            'source': node_id,
                            'target': target_id,
                            'type': 'internal',
                            'text': link_text
                        }
                        self.links.append(link)
                        
                logger.debug(f"Processed: {md_file} -> {node_id}")
                        
            except Exception as e:
                logger.error(f"Error processing file {md_file}: {e}")

    def add_directory_structure_links(self) -> None:
        """添加基于目录结构的链接"""
        # 按目录分组节点
        directory_groups = {}
        
        for node in self.nodes:
            path_parts = Path(node['path']).parts
            if len(path_parts) > 1:
                directory = '/'.join(path_parts[:-1])
                if directory not in directory_groups:
                    directory_groups[directory] = []
                directory_groups[directory].append(node['id'])
                
        # 为同目录下的页面添加连接
        for directory, node_ids in directory_groups.items():
            if len(node_ids) > 1:
                # 查找目录的index页面
                index_candidates = [nid for nid in node_ids 
                                  if any(keyword in nid.lower() 
                                        for keyword in ['index', 'readme'])]
                
                if index_candidates:
                    index_node = index_candidates[0]
                    # 连接index页面到同目录的其他页面
                    for node_id in node_ids:
                        if node_id != index_node:
                            link = {
                                'source': index_node,
                                'target': node_id,
                                'type': 'structural',
                                'text': 'directory'
                            }
                            self.links.append(link)

    def filter_orphaned_nodes(self) -> None:
        """过滤孤立节点（可选）"""
        # 获取所有在链接中出现的节点ID
        connected_nodes = set()
        for link in self.links:
            connected_nodes.add(link['source'])
            connected_nodes.add(link['target'])
            
        # 保留主页和分类页，即使它们可能是孤立的
        important_nodes = set()
        for node in self.nodes:
            if node['category'] in ['main', 'category']:
                important_nodes.add(node['id'])
                
        # 过滤节点（保留连接的节点和重要节点）
        keep_nodes = connected_nodes | important_nodes
        self.nodes = [node for node in self.nodes if node['id'] in keep_nodes]
        
        # 过滤无效链接
        valid_node_ids = {node['id'] for node in self.nodes}
        self.links = [link for link in self.links 
                     if link['source'] in valid_node_ids and link['target'] in valid_node_ids]

    def generate_statistics(self) -> Dict:
        """生成统计信息"""
        stats = {
            'total_nodes': len(self.nodes),
            'total_links': len(self.links),
            'languages': {},
            'categories': {},
            'generated_at': str(Path.cwd()),
            'source_directory': str(self.docs_path.absolute())
        }
        
        # 语言统计
        for node in self.nodes:
            lang = node['language']
            stats['languages'][lang] = stats['languages'].get(lang, 0) + 1
            
        # 类别统计
        for node in self.nodes:
            category = node['category']
            stats['categories'][category] = stats['categories'].get(category, 0) + 1
            
        return stats

    def compute_node_url(self, node_id: str, language: str) -> str:
        """根据节点 id 和语言计算站点上的 URL。

        规则：
        - node_id 是相对于 docs 的路径，且不包含 .md（例如："sci/cheatshet/docker.zh" 或 "index"）
        - 如果文件名里包含语言后缀（.zh/.en），在生成 URL 时去掉该后缀
        - 如果语言是默认语言（self.default_language），URL 不带语言前缀；否则在路径前加上 /<lang>/
        - 目录索引（以 index 结尾）会被映射到上级目录或根路径
        - 返回以 "/" 开头且以 "/" 结尾的路径（根页面为 "/"）
        """
        # 清理并分段
        parts = node_id.split('/') if node_id else []
        if parts:
            # 去掉最后一段的语言后缀（如 filename.zh）
            parts[-1] = re.sub(r'\.(zh|en)$', '', parts[-1])

        # 处理 index 情况
        if parts and parts[-1].lower() in ('index', 'readme'):
            parts = parts[:-1]

        url_path = '/'.join(parts)

        if url_path == '':
            url = '/'
        else:
            url = '/' + url_path.strip('/') + '/'

        # 非默认语言需要加语言前缀
        if language and language != self.default_language:
            url = '/' + language.strip('/') + url

        # 规范化连续斜杠
        url = re.sub(r'//+', '/', url)
        return url

    def save_data(self) -> None:
        """保存数据到JSON文件"""
        # 确保输出目录存在
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        # 为每个节点生成 URL 字段
        for node in self.nodes:
            node['url'] = self.compute_node_url(node['id'], node.get('language', self.default_language))

        # 生成最终数据
        data = {
            'nodes': self.nodes,
            'links': self.links,
            'statistics': self.generate_statistics(),
            'metadata': {
                'version': '1.0',
                'generator': 'MkDocs Knowledge Graph Generator',
                'generated_at': str(__import__('datetime').datetime.now()),
            }
        }
        
        # 保存到文件
        with open(self.output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        logger.info(f"Graph data saved to: {self.output_path}")
        
        # 打印统计信息
        stats = data['statistics']
        logger.info(f"Generated graph with {stats['total_nodes']} nodes and {stats['total_links']} links")
        logger.info(f"Languages: {stats['languages']}")
        logger.info(f"Categories: {stats['categories']}")

    def run(self) -> None:
        """运行数据生成流程"""
        logger.info("Starting knowledge graph data generation...")
        
        try:
            # 检查输入目录
            if not self.docs_path.exists():
                raise FileNotFoundError(f"Docs directory not found: {self.docs_path}")
                
            # 扫描目录
            self.scan_directory()
            
            # 添加结构性链接
            self.add_directory_structure_links()
            
            # 过滤孤立节点（可选）
            # self.filter_orphaned_nodes()
            
            # 保存数据
            self.save_data()
            
            logger.info("Knowledge graph data generation completed successfully!")
            
        except Exception as e:
            logger.error(f"Error during generation: {e}")
            raise

def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate knowledge graph data for MkDocs')
    parser.add_argument('--docs', '-d', default='docs', 
                       help='Path to docs directory (default: docs)')
    parser.add_argument('--output', '-o', default='docs/js/graph-data.json',
                       help='Output JSON file path (default: docs/js/graph-data.json)')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose logging')
    parser.add_argument('--default-language', '-L', default='zh',
                       help='Default site language (used to generate URLs), e.g. zh or en')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # 创建生成器并运行
    generator = GraphDataGenerator(args.docs, args.output)
    generator.default_language = args.default_language or 'zh'
    generator.run()

if __name__ == '__main__':
    main()