---
title: RIKEN RIDF 文件构成详解：数据块 (Block) 说明
---

# RIKEN RIDF 文件构成详解：数据块 (Block) 说明

RIKEN的RIDF（RIBF数据格式）文件是一种**二进制文件**，其基本构成单元是**数据块（Block）**。整个文件就是由一系列这样的数据块串行组成的。每个数据块都描述了一部分特定的信息，例如原始探测器数据、事件信息、计数器数据、注释或状态信息等。

[block[segment[data point]]]的嵌套结构

[事件 [[事件头], [数据段1 [[段头1], [数据点集合1]]], [数据段2 [[段头2], [数据点集合2]]], ...]]


---

## 通用数据块结构 (General Block Structure)

每个数据块都以一个或多个**头部字（Header Word(s)）**开始，这些头部字定义了这个数据块的属性和类型。最核心的是第一个头部字，通常为32位（4字节），其结构如下：

1.  **第一个头部字 (First Header Word - 32 bits)**:
    * **`Revision` (2 bits)**: 块格式的版本号。通常为 `0b00` (即十进制0)，代表版本1。
    * **`Layer` (2 bits)**: 定义了该数据块在层级结构中的深度。例如，顶层块可能是Layer 0，它包含的子块可能是Layer 1，以此类推。
    * **`Class ID` (6 bits)**: **这是区分数据块类型的关键字段**。不同的 `Class ID` 代表了不同种类的数据块，例如事件数据、原始数据段、注释等。下面我们会详细介绍一些常见的 `Class ID`。
    * **`Block Size` (22 bits)**: 定义了**整个数据块的总大小**，单位是**短字（short words, 即2字节）**。这个大小包括了头部字本身以及后续的所有数据。通过这个字段，读取程序知道需要读取多少数据才能完整地获取当前块，并找到下一个块的起始位置。

2.  **地址字 (Address Word - 32 bits) (通常紧随第一个头部字之后)**:
    * 这个32位的字通常用于标识数据的来源。对于由前端电子学模块（如VME模块）产生的数据块（例如事件片段），这个地址字通常是**事件片段ID (Event Fragment ID)**，有时也可能是产生该数据的前端计算机的IP地址或其他标识符。

**因此，一个典型的数据块通常至少包含 8 字节的头部信息（第一个头部字 + 地址字）。** 之后的内容则完全由 `Class ID` 来决定。

---

## `Class ID` 决定的数据块内容 - “每块block是什么”

`Class ID` 告诉我们这个数据块里装的是什么样的数据。以下是一些在RIDF中常见且重要的 `Class ID` 及其对应的数据块含义：

* **`Class ID = 0`: 事件片段 (Event Fragment)**
    * **用途**: 代表从一个独立的数据源（例如一个采集卡、一个前端计算机或一个子系统）发送过来的关于一个“事件”的数据包。
    * **典型内容**:
        * 标准的头部字和地址字（地址字通常是此片段的唯一ID）。
        * 可能包含一个此片段特有的头部，例如包含时间戳或触发信息。
        * **核心内容**: 通常包含一个或多个**数据段块 (Segment Block, `Class ID = 4`)**，这些数据段块里装着来自不同探测器或电子学模块的原始数据。

* **`Class ID = 1`: 事件汇编 (Event Assembly)**
    * **用途**: 将来自不同数据源（即多个不同的事件片段，`Class ID = 0`）的、属于同一个物理事件的数据组合在一起。这是事件重建（event building）过程的产物。
    * **典型内容**:
        * 标准的头部字和地址字。
        * 可能包含一个全局事件头部，例如全局事件号、全局时间戳等。
        * 包含多个之前描述的**事件片段块 (Event Fragment)**。

* **`Class ID = 4`: 数据段 (Segment)**
    * **用途**: **这是包含实际原始探测器数据的最基本单位，非常重要！**
    * **典型内容**:
        * 标准的头部字和地址字（地址字可能在此层级有特定含义，或继承自父块）。
        * **段头部 (Segment Header)**: 这是一个此数据段特有的头部，通常包含：
            * **`Segment ID` (段标识符)**: 一个整数，唯一标识了这个数据段的来源（例如，哪个探测器、哪个模块）。`Segment ID` 本身常常又被结构化地定义，包含设备、焦平面、探测器类型和模块号等信息。
            * 数据类型指示符：指明后续数据的具体格式（例如，是ADC数据、TDC数据、模式字等）。
            * 通道数或数据字计数等。
        * **数据负载 (Data Payload)**: 实际的原始数据值（例如，ADC的转换结果列表、TDC的时间测量值列表等）。

* **`Class ID = 5`: 注释块 (Comment Block)**
    * **用途**: 用于在数据文件中嵌入文本注释，例如运行编号、实验条件、操作员笔记等。
    * **典型内容**:
        * 标准的头部字和地址字。
        * 一个指定注释长度的字段。
        * 实际的ASCII或UTF-8文本字符串。

* **`Class ID = 11, 12, 13`: 计数器块 (Scaler Block)**
    * **用途**: 存储各种计数器的值（例如，束流强度计数、触发率计数等）。
    * `Class ID = 11`: 非清零计数器 (24位)
    * `Class ID = 12`: 清零计数器 (24位)
    * `Class ID = 13`: 非清零计数器 (32位)
    * **典型内容**:
        * 标准的头部字和地址字。
        * 通常包含一个指示计数器通道数量的字段。
        * 一系列计数器的值。

* **`Class ID = 16`: 时间戳块 (Timestamp Block)**
    * **用途**: 记录时间戳信息，常用于事件同步、死时间计算等。
    * **典型内容**:
        * 标准的头部字和地址字。
        * 一个或多个高精度的时间戳值。

* **`Class ID = 21`: 状态块 (Status Block)**
    * **用途**: 记录DAQ系统或实验的状态信息。
    * **典型内容**:
        * 标准的头部字和地址字。
        * **`Status ID`**: 进一步细分状态类型。
            * `Status ID = 11`: 运行开始状态 (Run start status)，其内容通常是**XML格式的文本**，描述了运行开始时的各种配置和参数。
            * `Status ID = 12`: 运行结束状态 (Run end status)，内容也是**XML格式的文本**，记录运行结束时的信息。
        * 状态数据本身（例如，XML文本内容）。

---

## 层级结构 (Hierarchical Nature)

重要的是要理解RIDF的层级结构。一个高层的数据块（例如 `Class ID = 1` 的事件汇编块）可以包含多个低层的数据块（例如多个 `Class ID = 0` 的事件片段块），而一个事件片段块又可以包含多个 `Class ID = 4` 的数据段块。`Block Size` 字段确保了解码软件可以正确地跳过或进入这些嵌套的块。

这种结构使得数据既有组织性，又非常灵活，能够适应RIKEN各种复杂核物理实验的需求。解码RIDF文件的软件（如ANAROOT）就是通过逐个解析这些数据块的头部信息，识别其 `Class ID`，然后根据不同类型块的定义来提取有效数据。


你可以通过这个宏来把ridf转成人类可读的结构来了解其是什么。
```
#include <fstream> // Add file stream header
#include <iostream> // Add to use std::cerr

void convertRIDFtoReadable(const char* ridfFile = "/home/s057/exp/exp2505_s057/anaroot/users/tbt/ridf/data0013.ridf") {
    // Load necessary libraries
    gSystem->Load("libanacore.so");

    // Open RIDF file
    TArtEventStore *estore = new TArtEventStore();
    if (!estore->Open(ridfFile)) {
        std::cerr << "Error: Failed to open RIDF file: " << ridfFile << std::endl;
        return;
    }

    TArtRawEventObject *rawevent = estore->GetRawEventObject();

    // Open output file
    std::ofstream outFile("readable.txt");
    if (!outFile.is_open()) {
        std::cerr << "Error: Failed to open output file: readable.txt" << std::endl;
        return;
    }

    int neve = 0; // Event counter
    while (estore->GetNextEvent() && neve < 10) { // Only process the first 10 blocks
        outFile << "==================== Event " << neve + 1 << " ====================" << std::endl;

        // Iterate over all segments in the current event
        for (int i = 0; i < rawevent->GetNumSeg(); i++) {
            TArtRawSegmentObject *seg = rawevent->GetSegment(i);
            outFile << "Segment " << i + 1 << ":" << std::endl;
            outFile << "  Device: " << seg->GetDevice() << std::endl;
            outFile << "  FP: " << seg->GetFP() << std::endl;
            outFile << "  Detector: " << seg->GetDetector() << std::endl;
            outFile << "  Module: " << seg->GetModule() << std::endl;
            outFile << "  NumData: " << seg->GetNumData() << std::endl;

            // Iterate over all data points in the segment
            for (int j = 0; j < seg->GetNumData(); j++) {
                TArtRawDataObject *d = seg->GetData(j);
                int geo = d->GetGeo();
                int ch = d->GetCh();
                int val = d->GetVal();
                int cat = d->GetCategoryID();
                int det = d->GetDetectorID();
                int id = d->GetDatatypeID();

                outFile << "    Data " << j + 1 << ":" << std::endl;
                outFile << "      Geo: " << geo << std::endl;
                outFile << "      Channel: " << ch << std::endl;
                outFile << "      Value: " << val << std::endl;
                outFile << "      Category ID: " << cat << std::endl;
                outFile << "      Detector ID: " << det << std::endl;
                outFile << "      Datatype ID: " << id << std::endl;
            }
        }

        estore->ClearData(); // Clear current event data
        neve++;
    }

    outFile << "Conversion completed. Processed " << neve << " blocks." << std::endl;

    // Close output file
    outFile.close();

    std::cout << "Conversion completed. Results saved to readable.txt" << std::endl;
}
```


source:

https://www-nh.scphys.kyoto-u.ac.jp/~yano/ws/en/docs/documents/daq/dataformat/ridf/

https://ribf.riken.jp/RIBFDAQ/index.php?plugin=attach&refer=DAQ%2FManual%2FDataformat&openfile=dataformat_101112e.pdf