# 现代核物理模拟项目管理与目录结构教程

本教程总结一个适用于 **Geant4 + ROOT + C++ + CMake + GoogleTest** 的现代科研项目结构，并给出实践经验与最佳实践。非常适用于核物理模拟、探测器重建、大型 C++ 科学代码开发。

---

# 1. 总体架构理念

一个良好的科研模拟项目应满足：

- **模块化**：模拟（Geant4）、数据结构（datatypes）、重建（reconstruction）互相解耦。
- **可测试性**：每个模块可单独做单元测试，全链路可做集成测试。
- **运行时与构建时分离**：配置、宏、几何、参数文件不参与编译。
- **清晰的数据流**：data/raw → data/sim → data/reco → scripts/analysis。
- **可扩展**
---

# 2. 推荐目录结构

```
your_project/
│
├── CMakeLists.txt
├── cmake/                        # FindXXX.cmake, 工具CMake脚本
│
├── libs/                         # 所有核心 C++ 库
│   ├── datatypes/                # 事件、Hit、Track 等核心数据类型
│   │   ├── include/
│   │   ├── src/
│   │   └── tests/
│   ├── g4sim/                    # Geant4 模拟库
│   │   ├── include/
│   │   ├── src/
│   │   ├── tests/
│   │   └── macros/ (可选)
│   └── reconstruction/           # 重建算法库（tracking, clustering）
│       ├── include/
│       ├── src/
│       └── tests/
│
├── apps/                         # 可执行程序
│   ├── run_sim/                  # 调用 g4sim 的主程序
│   ├── run_reco/                 # 调用 reconstruction 的主程序
│   └── run_optimize/             # 参数优化程序（C++）
│
├── configs/                      # 所有运行时配置（不参与编译）
│   ├── geant4/
│   │   ├── macros/               # G4 宏
│   │   ├── materials/
│   │   └── geometry/
│   ├── reconstruction/           # 重建参数 YAML/JSON
│   └── optimize/                 # 优化脚本所需参数
│
├── data/                         # 运行所得数据
│   ├── raw/                      # 外部输入数据
│   ├── sim/                      # Geant4 输出文件
│   ├── reco/                     # 重建后的数据
│   └── calib/                    # 标定参数（gain, offset）
│
├── scripts/                      # Python 工具脚本
│   ├── analysis/
│   ├── optimize/
│   ├── visualize/
│   └── utils/
│
├── tests/                        # 集成测试（非单元测试）
│   ├── unit/
│   └── integration/
│
└── results/                      # 输出图片、拟合结果（未纳入git）
```

---

# 3. 顶层 CMakeLists.txt 结构

```cmake
cmake_minimum_required(VERSION 3.20)
project(YourProject LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)

# 引入 cmake/ 下的模块
list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake")

# 寻找依赖包
find_package(Geant4 REQUIRED)
find_package(ROOT REQUIRED)

# 开启测试框架
enable_testing()

# 子模块
add_subdirectory(libs)
add_subdirectory(apps)
add_subdirectory(tests)
```

CMake 的职责：
- 管理库（libs）
- 编译可执行（apps）
- 建立测试（tests）
- 不处理任何数据文件

---

# 4. datatypes 库

职责：
- 定义 Event / Hit / Track 等基本结构
- 无 Geant4 或 ROOT 依赖（保持“纯净”）

目录：
```
libs/datatypes/
  include/yourproj/
  src/
  tests/
```

CMake：
```cmake
add_library(datatypes
    src/Event.cpp
    src/Hit.cpp
)

target_include_directories(datatypes PUBLIC include)

add_subdirectory(tests)
```

单元测试：
```cmake
add_executable(test_datatypes test_event.cpp)
target_link_libraries(test_datatypes PRIVATE datatypes GTest::gtest_main)
add_test(NAME test_datatypes COMMAND test_datatypes)
```

---

# 5. Geant4 模拟库 g4sim

职责：
- DetectorConstruction
- PhysicsList
- RunAction / EventAction
- 输入/输出管理

目录：
```
libs/g4sim/
  include/
  src/
  tests/
  macros/ (可选)
```

CMake：
```cmake
add_library(g4sim
    src/DetectorConstruction.cpp
    src/PhysicsList.cpp
    src/PrimaryGenerator.cpp
)

target_link_libraries(g4sim PUBLIC datatypes Geant4::G4run Geant4::G4vis)
```

单元测试只做：
- 初始化成功否
- Geometry 构建是否报错
（不跑真实模拟，因为耗时太长）

---

# 6. reconstruction 库

职责：
- cluster / tracking / PID
- calibration
- energy reconstruction

目录：
```
libs/reconstruction/
  include/
  src/
  tests/
```

CMake：
```cmake
add_library(reconstruction
    src/TrackerReconstruction.cpp
    src/CalorimeterReconstruction.cpp
)

target_include_directories(reconstruction PUBLIC include)
target_link_libraries(reconstruction PUBLIC datatypes ROOT::Core)
```

---

# 7. 可执行程序 apps/

示例：
```
apps/run_sim/main.cpp
apps/run_reco/main.cpp
apps/run_optimize/main.cpp
```

CMake：
```cmake
add_executable(run_sim main.cpp)
target_link_libraries(run_sim PRIVATE g4sim datatypes)

add_executable(run_reco main.cpp)
target_link_libraries(run_reco PRIVATE reconstruction datatypes)
```

运行：
```
./build/apps/run_sim/run_sim -m configs/geant4/macros/run.mac -o data/sim/out.root
```

---

# 8. configs/（非常重要）

配置与代码分离，将宏、几何、重建参数全部放这里：

```
configs/
  geant4/
    macros/run.mac
    geometry/detector.gdml
    materials/materials.txt
  reconstruction/
    tracker.yaml
    calibration.yaml
  optimize/
    grid_search.yaml
```

优点：
- 不触发重新编译
- 参数可版本管理
- apps/ 可以灵活调用

---

# 9. data/（统一管理模拟与重建数据）

```
data/
  raw/
  sim/
  reco/
  calib/
```

所有模拟输出、重建结果都按阶段放置。

---

# 10. scripts/（Python 工具）

分类建议：
```
scripts/
  analysis/         数据分析
  optimize/         参数优化（scipy/numba）
  visualize/        可视化（matplotlib/root_numpy）
  utils/            辅助代码
```

---

# 11. tests/（单元 + 集成测试）

```
tests/
  unit/             调用各库的测试
  integration/      全链路：G4 → Reco → Output
```

集成测试示例：
```
test_full_pipeline.cpp
```
内容：
- 用微型宏生成 2~3 个 event
- 跑重建
- 检查输出 Tree 是否包含期望 branch

---

# 12. results/（不纳入 git）

用于保存：
- 图像
- 拟合结果
- 优化输出

在 .gitignore 中添加：
```
results/
data/sim/
data/reco/
```

---

# 13. 最终数据流

```
configs/geant4/macros → run_sim → data/sim/*.root

data/sim/*.root + configs/reconstruction/*.yaml
    → run_reco → data/reco/*.root

scripts/analysis/*.py → produce results/
```

---

# 14. 总结

一个现代核物理模拟项目需要：

- 清晰的模块边界（datatypes / sim / reco）
- 完整的构建系统（CMake）
- 可测试性（GoogleTest + CTest）
- 运行配置尽量放 configs/
- 数据与代码解耦
- Python 辅助分析脚本 standards




