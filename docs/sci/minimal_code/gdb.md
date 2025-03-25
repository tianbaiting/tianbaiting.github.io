# gdb 调试

本文档介绍了如何使用 gdb 进行调试，包括在命令行和 VSCode 中的使用方法。

## gdb 命令行

在命令行中使用 gdb 进行调试的基本步骤如下：

1. 编译程序时添加调试信息：
    ```sh
    gcc -g -o myprogram myprogram.c
    ```

2. 启动 gdb 并加载程序：
    ```sh
    gdb myprogram
    ```

3. 设置断点：
    ```sh
    break main
    ```

4. 运行程序：
    ```sh
    run
    ```

5. 单步执行代码：
    ```sh
    next
    ```

6. 查看变量值：
    ```sh
    print variable_name
    ```

7. 退出 gdb：
    ```sh
    quit
    ```

## gdb vscode

在 VSCode 中使用 gdb 进行调试的步骤如下：

1. 安装 C/C++ 插件（Microsoft 提供）。

2. 配置 launch.json 文件：
    ```json
    {
      "version": "0.2.0",
      "configurations": [
         {
            "name": "(gdb) Launch",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceFolder}/myprogram",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "setupCommands": [
              {
                 "description": "Enable pretty-printing for gdb",
                 "text": "-enable-pretty-printing",
                 "ignoreFailures": true
              }
            ],
            "preLaunchTask": "build",
            "miDebuggerPath": "/usr/bin/gdb",
            "logging": {
              "trace": true,
              "traceResponse": true,
              "engineLogging": true
            },
            "processId": "${command:pickProcess}",
            "setupCommands": [
              {
                 "description": "Enable pretty-printing for gdb",
                 "text": "-enable-pretty-printing",
                 "ignoreFailures": true
              }
            ],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "miDebuggerPath": "/usr/bin/gdb",
            "setupCommands": [
              {
                 "description": "Enable pretty-printing for gdb",
                 "text": "-enable-pretty-printing",
                 "ignoreFailures": true
              }
            ],
            "preLaunchTask": "build",
            "logging": {
              "trace": true,
              "traceResponse": true,
              "engineLogging": true
            },
            "processId": "${command:pickProcess}"
         }
      ]
    }
    ```

示例
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "g++ - 调试RLUD",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceFolder}/code/root_tranform/runPro",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}/code/root_tranform",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "setupCommands": [
                {
                    "description": "为 gdb 启用整齐打印",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ],
            "preLaunchTask": "C/C++: g++ build ROOT",
            "miDebuggerPath": "/usr/bin/gdb"
        }
    ]
}
```
task.json


```
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "C/C++: g++ build ROOT",
            "type": "shell",
            "command": "g++ -g -Iinclude -o runPro src/globals.cpp src/function.cpp src/R_LRUD.cpp $(root-config --cflags --glibs)",
            "options": {
                "cwd": "${workspaceFolder}/code/root_tranform"
            },
            "problemMatcher": ["$gcc"],
            "group": {
                "kind": "build",
                "isDefault": true
            }
        }
    ]
}
```


3. 按 F5 开始调试。

通过以上步骤，您可以在 VSCode 中使用 gdb 进行调试。`