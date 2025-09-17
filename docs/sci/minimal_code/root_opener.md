# 设置 ROOT 文件默认浏览器教程

本文档总结了在Linux系统上设置一个自定义程序以通过ROOT TBrowser打开`.root`文件的完整步骤。

## 最终目标

目标是实现当用户执行 `xdg-open your_file.root` 或在文件管理器中双击`.root`文件时，能够自动启动ROOT TBrowser来浏览该文件的内容。

---

### 步骤 1: 创建执行脚本

首先，我们创建一个简单的shell脚本，它会调用ROOT来打开指定的文件。

该脚本被保存在 `~/.local/bin/root-browser`。`~/.local/bin` 是存放用户自定义脚本的标准目录，通常已包含在系统的`PATH`环境变量中。

**脚本内容:**
```bash
#!/bin/bash
# Script to open a ROOT file in a TBrowser

if [ -z "$1" ]; then
    echo "Usage: $0 <path_to_root_file>"
    exit 1
fi

# Check if the file exists
if [ ! -f "$1" ]; then
    echo "Error: File not found at $1"
    exit 1
fi

# Launch ROOT, open the file, and start a TBrowser.
# The -l flag prevents the splash screen.
root -l -e "new TBrowser()" "$1"
```

---

### 步骤 2: 授予脚本执行权限

为了让系统能够运行这个脚本，我们必须为其添加可执行权限。

**执行的命令:**
```sh
chmod +x /home/tbt/.local/bin/root-browser
```

---

### 步骤 3: 定义新的MIME类型

为了让桌面环境知道`.root`文件是什么，我们为它定义一个自定义的MIME类型：`application/x-root`。

这通过在 `~/.local/share/mime/packages/` 目录下创建一个XML文件来完成。

**文件路径:** `/home/tbt/.local/share/mime/packages/application-x-root.xml`

**文件内容:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
  <mime-type type="application/x-root">
    <comment>CERN ROOT File</comment>
    <glob pattern="*.root"/>
  </mime-type>
</mime-info>
```

---

### 步骤 4: 更新MIME数据库

创建了MIME定义文件后，需要更新系统的MIME数据库来注册这个新类型。

**执行的命令:**
```sh
update-mime-database ~/.local/share/mime
```

---

### 步骤 5: 创建 .desktop 入口文件

`.desktop` 文件是Linux桌面环境用来定义应用程序快捷方式和文件关联的标准。我们创建一个文件来描述我们的`root-browser`程序。

**文件路径:** `/home/tbt/.local/share/applications/root-browser.desktop`

**文件内容:**
```ini
[Desktop Entry]
Type=Application
Name=ROOT Browser
Exec=/home/tbt/.local/bin/root-browser %f
MimeType=application/x-root
Terminal=false
```
- `Exec=/home/tbt/.local/bin/root-browser %f`: 定义了如何执行程序。`%f` 会被替换为要打开的文件的路径。
- `MimeType=application/x-root`: 声明此程序可以处理`application/x-root`类型的文件。

---

### 步骤 6: 设置为默认应用程序

最后一步是告诉系统，所有`application/x-root`类型的文件都应该默认使用我们刚刚定义的`root-browser.desktop`来打开。

**执行的命令:**
```sh
xdg-mime default root-browser.desktop application/x-root
```

---

## 结论

完成以上所有步骤后，您的系统现在已经配置完毕。任何通过`xdg-open`或桌面文件管理器打开`.root`文件的操作都会触发执行我们的自定义脚本，从而在TBrowser中显示文件内容。
