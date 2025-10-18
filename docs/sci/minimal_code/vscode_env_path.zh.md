需要通过 `source` 命令来配置 ROOT、Geant4 等软件的编译环境非常熟悉。

你遇到的核心问题是：**VSCode 及其 CMake Tools 插件在一个“干净”的、独立的环境中运行 `cmake` 命令，这个环境并没有加载你终端里通过 `source your_script.sh` 设置的环境变量**。因此，当 CMake 试图读取 `$TARTSYS` 这个变量时，它发现这个变量没有被定义，从而导致配置失败并报错。

下面我将为你提供几种解决方案，从最简单快捷到最规范、一劳永逸的方法。

### 解决方案 1：最快最简单的临时方法

这是解决当前问题的最快方法，但每次打开项目可能都需要重复操作。

1.  **打开一个常规的Linux终端** (而不是VSCode内置的终端)。
2.  **首先，`source` 你的环境设置脚本**，加载所有必要的环境变量：
    ```bash
    source /path/to/your/setup_script.sh 
    ```
    (请将 `/path/to/your/setup_script.sh` 替换为你提供的那个脚本的实际路径)。
3.  **从这个已经配置好环境的终端里启动 VSCode**，并打开你的项目文件夹：
    ```bash
    code /home/tbt/workspace/kondo-smsimulator
    ```

通过这种方式启动，VSCode 会完全继承启动它的那个终端的环境变量。这样，当 CMake Tools 插件运行时，它就能够找到 `$TARTSYS`、`$LD_LIBRARY_PATH` 等所有必需的变量了。

### 解决方案 2：推荐的、一劳永逸的方法 (配置工作区 `settings.json`)

这个方法是将项目所需的环境变量作为项目配置的一部分，这样无论你如何启动VSCode，该项目总能找到正确的环境。这对于管理多个具有不同环境依赖的项目来说是最佳实践。

1.  **获取环境变量的最终值**:
    首先，你需要知道在 `source` 了你的设置脚本后，那些关键环境变量的最终值是什么。打开一个终端，运行以下命令：

    ```bash
    # 先加载你的环境
    source /path/to/your/setup_script.sh

    # 然后逐个打印出需要的值并复制它们
    echo $TARTSYS
    echo $LD_LIBRARY_PATH
    echo $PATH
    echo $SMSIMDIR 
    ```

    你会得到几行输出，请将这些输出的字符串复制下来，后续步骤会用到。

2.  **在VSCode项目中创建配置文件**:

      * 在你的项目根目录 `/home/tbt/workspace/kondo-smsimulator` 下，创建一个名为 `.vscode` 的文件夹 (如果尚不存在)。
      * 在 `.vscode` 文件夹内，创建一个名为 `settings.json` 的文件。

3.  **编辑 `settings.json` 文件**:
    将以下内容粘贴到 `settings.json` 文件中，并把你第一步中复制的那些环境变量的值填入相应位置：

    ```json
    {
        "cmake.configureEnvironment": {
            "TARTSYS": "这里粘贴你从 'echo $TARTSYS' 得到的值",
            "LD_LIBRARY_PATH": "这里粘贴你从 'echo $LD_LIBRARY_PATH' 得到的值",
            "PATH": "这里粘贴你从 'echo $PATH' 得到的值",
            "SMSIMDIR": "/home/tbt/workspace/kondo-smsimulator/smsimulator"
        }
    }
    ```

    **示例：**
    假设你运行 `echo $TARTSYS` 得到 `/home/tbt/Software/anaroot/install`，那么你的 `settings.json` 文件看起来会是这样：

    ```json
    {
        "cmake.configureEnvironment": {
            "TARTSYS": "/home/tbt/Software/anaroot/install",
            "LD_LIBRARY_PATH": "/home/tbt/workspace/kondo-smsimulator/smsimulator/install/lib:/home/tbt/Software/anaroot/install/lib:/home/tbt/Software/root/lib:...",
            "PATH": "/home/tbt/Software/root/bin:/home/tbt/Software/geant4/install/bin:...",
            "SMSIMDIR": "/home/tbt/workspace/kondo-smsimulator/smsimulator"
        }
    }
    ```

    *注意：`LD_LIBRARY_PATH` 和 `PATH` 的值通常很长，请确保完整复制。*

4.  **清理并重新配置CMake**:

      * 保存 `settings.json` 文件。
      * 在VSCode中，按 `Ctrl+Shift+P` 打开命令面板。
      * 输入并选择 `CMake: Delete Cache and Reconfigure` (CMake: 删除缓存并重新配置)。
      * CMake现在应该会使用你在 `settings.json` 中定义的环境变量进行配置，并成功找到 `$TARTSYS`。



-----

信息来源:

  * [Visual Studio Code CMake Tools Documentation: Environment variables](https://www.google.com/search?q=https://vector-of-bool.github.io/docs/vscode-cmake-tools/environments.html)
  * [Visual Studio Code Documentation: Workspace settings](https://www.google.com/search?q=https://code.visualstudio.com/docs/getstarted/settings%23_workspace-settings)