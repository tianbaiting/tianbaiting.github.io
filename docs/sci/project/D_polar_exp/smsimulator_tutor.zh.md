---
title: smsimulator 教学
tag:
    - smsimulator
    - geant4
    - anroot
    - root
    - c++
---


## 目录层级

该目录位于thinkpad tbt: wsl:

```
/home/tbt/workspace/dpol
```

- **README、setup.sh**
  - `README`：项目说明文档，包含编译、运行、输入输出等使用说明。
  - `setup.sh`：环境变量设置脚本，配置 Geant4、ANAROOT、路径等，编译和运行前需 source。

- **bin/**
  - 存放编译生成的可执行文件（如 `sim_deuteron`），用于实际运行模拟。

- **geant4_sim/**
  - Geant4 仿真相关目录，包含宏文件（如 `vis.mac`）、几何描述文件（`geometry/`），以及用于自动生成参数的脚本（如 `CreatePara_NEBULAFull.pl`）。

- **lib/**
  - 存放编译生成的共享库（`.so` 文件），供主程序和其他模块调用。

- **sim_deuteron/**
  - sim_deuteron 子项目源码目录，包含：
    - `sim_deuteron.cc`：主程序源码。
    - `Makefile`：编译脚本。
    - `include/`：头文件。
    - `src/`：源文件。
    - `libsim_deuteron.so`：本模块生成的共享库。
    - `log2.txt`：编译或运行日志。

- **smg4lib/**
  - Geant4 相关的核心库源码，包含：
    - `Makefile`、`GNUmakefile.in`：编译脚本。
    - `action/`、`construction/`、`physics/`、`data/`：不同功能模块的源码和头文件。
    - `include/`：公共头文件。
    - `lib/`：编译生成的库文件。

- **smg4lib/data/**
  - 数据相关的源码、头文件、Makefile，主要用于数据管理、ROOT 相关操作等。