# c++项目

Linux + VScode(vim,emacs) + git + gcc + makefile + cmake 最基本的要求。


[google c++风格指南](https://zh-google-styleguide.readthedocs.io/en/latest/google-cpp-styleguide/headers.html)




## C++ 项目构建流程：从 GCC 到 Makefile 到 CMake

在 Linux 环境下，使用 VS Code (或其他编辑器如 Vim, Emacs) 进行 C++ 项目开发，并结合 Git 进行版本控制，是常见的开发模式。  `gcc`, `makefile`, 和 `cmake` 是构建 C++ 项目的关键工具。

### 1. 使用 GCC 直接编译

#### 1.1 编写 C++ 源代码

首先，你需要创建包含 C++ 代码的 `.cpp` 文件。例如，我们创建 `main.cpp` 和 `myclass.cpp`，以及头文件 `myclass.h`。

*   `myclass.h`:

    ```cpp
    // filepath: myclass.h
    #ifndef MYCLASS_H
    #define MYCLASS_H

    class MyClass {
    public:
        MyClass();
        void printMessage();
    };

    #endif
    ```

*   `myclass.cpp`:

    ```cpp
    // filepath: myclass.cpp
    #include <iostream>
    #include "myclass.h"

    MyClass::MyClass() {}

    void MyClass::printMessage() {
        std::cout << "Hello from MyClass!" << std::endl;
    }
    ```

*   `main.cpp`:

    ```cpp
    // filepath: main.cpp
    #include "myclass.h"

    int main() {
        MyClass myObject;
        myObject.printMessage();
        return 0;
    }
    ```

#### 1.2 编译源代码

使用 `g++` 命令将源代码编译成目标文件（`.o` 文件）。

```bash
g++ -c myclass.cpp -o myclass.o
g++ -c main.cpp -o main.o
```




