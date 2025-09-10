
查看当前目录下所有目录的大小，并限制深度为 1 (以人类可读的格式):
```
du -dh 1 .
```


## wget


wget -r -p -np -k https://example.com


1. 从 https://example.com 开始递归下载所有内容；
2. 下载页面所需的所有资源（如图片、CSS 等）；
3. 限制下载范围，不会超出指定目录；
4. 将 HTML 文件中的链接转换为本地链接，便于离线浏览。

## 文本操作

cat ~/Software/setup_zsh.sh | iconv -f utf-8 -t utf-16le | clip.exe

传递给win的剪切板

## 模糊检索

fzf
