# ROOT THttpServer：在线直方图的 Web API

THttpServer 是 ROOT 内置的 HTTP 服务器，可将内存中的 ROOT 对象（直方图、Canvas 等）通过 Web 接口实时暴露。核物理实验的在线监控系统广泛使用它。

## 基本原理

```
┌──────────────────────────────────────────────────────┐
│  在线分析器进程 (C++ / ROOT macro)                     │
│                                                      │
│  THttpServer *server = new THttpServer("port:8080"); │
│  server->Register("/", hHOD_idqu);                   │
│  server->Register("/", hHOD_idqd);                   │
│                                                      │
│  ... 每个事件 Fill 直方图 ...                          │
│  hHOD_idqu->Fill(detectorID, charge);                │
└──────────────┬───────────────────────────────────────┘
               │ HTTP (内置 civetweb)
               ▼
┌──────────────────────────────────────────────────────┐
│  http://hostname:8080/                               │
│                                                      │
│  /                        → JSROOT GUI (浏览器可视化) │
│  /HOD_idqu/root.json      → TH2F 完整 JSON 序列化    │
│  /HOD_idqu/root.png       → PNG 图片                 │
│  /HOD_idqu/root.bin       → ROOT 二进制格式           │
│  /h.json                  → 对象层级 JSON             │
│  /StreamerInfo/root.json  → 类型信息                  │
└──────────────────────────────────────────────────────┘
```

- 服务端：分析器进程中运行的 `THttpServer`，基于 civetweb 嵌入式 HTTP 库。
- 前端：JSROOT 提供浏览器端交互式可视化 GUI。
- 数据格式：每个注册对象可通过 URL 后缀选择输出格式（`.json`、`.png`、`.bin`）。

## 服务端：发布直方图

```cpp
// 创建服务器，监听 8080 端口
THttpServer *server = new THttpServer("http:8080");

// 创建直方图
TH2F *hHOD_idqu = new TH2F("HOD_idqu", "HOD ID-QUraw", 40, 0.5, 40.5, 100, 0, 4000);
hHOD_idqu->GetXaxis()->SetTitle("ID");
hHOD_idqu->GetYaxis()->SetTitle("QUraw");

// 注册到服务器——之后每次 Fill 都会自动反映到 Web 接口
server->Register("/", hHOD_idqu);

// 在事件循环中正常 Fill
while (read_next_event()) {
    hHOD_idqu->Fill(det_id, charge);
}
```

`Register` 的第一个参数是 URL 路径前缀，`"/"` 表示直方图直接挂在根路径下。

## 客户端：浏览 GUI

浏览器访问 `http://hostname:port/` 即可看到 JSROOT GUI，展示所有注册对象的层级树，点击可交互式查看直方图。

首页 HTML 中嵌入了完整的对象层级信息（`getCachedHierarchy`），包含每个对象的类型和标题，例如：

```
HOD_idqu   ROOT.TH2F   "HOD ID-QUraw"
HOD_idqd   ROOT.TH2F   "HOD ID-QDraw"
BDC1_xy    ROOT.TH2F   "BDC1 XY"
Coin       ROOT.TH1F   "Coin"
```

## 客户端：抓取 JSON 数据

核心端点格式：`http://hostname:port/<对象名>/root.json`

返回 ROOT 对象的完整 JSON 序列化，结构如下：

```json
{
  "_typename": "TH2F",
  "fName": "HOD_idqu",
  "fTitle": "HOD ID-QUraw",
  "fNcells": 4284,
  "fEntries": 271330,
  "fXaxis": {
    "_typename": "TAxis",
    "fNbins": 40,
    "fXmin": 0.5,
    "fXmax": 40.5,
    "fTitle": "ID"
  },
  "fYaxis": {
    "_typename": "TAxis",
    "fNbins": 100,
    "fXmin": 0,
    "fXmax": 4000,
    "fTitle": "QUraw"
  },
  "fArray": [0, 0, 3, 15, ...]
}
```

关键字段：

| 字段 | 含义 |
|------|------|
| `_typename` | ROOT 类名，如 `TH2F`、`TH1F` |
| `fArray` | 所有 bin 的计数（一维展开，含 underflow/overflow） |
| `fNcells` | `(fNbinsX+2) * (fNbinsY+2)`，即 fArray 长度 |
| `fEntries` | 总填入次数 |
| `fXaxis`/`fYaxis` | 轴信息：bin 数、范围、标题 |

用 curl 抓取：

```bash
curl http://ribfana04:10101/HOD_idqu/root.json -o HOD_idqu.json
```

## 在 ROOT 中反序列化 JSON

`TBufferJSON::ConvertFromJSON` 可将 JSON 还原为内存中的 ROOT 对象：

```cpp
#include "TBufferJSON.h"

// 读取 JSON 文件
std::ifstream input("HOD_idqu.json");
std::ostringstream buf;
buf << input.rdbuf();
std::string json = buf.str();

// 反序列化为 ROOT 对象
TObject *obj = TBufferJSON::ConvertFromJSON(json.c_str());
TH2 *histogram = dynamic_cast<TH2 *>(obj);

// 脱离文件所有权，防止意外销毁
histogram->SetDirectory(nullptr);

// 正常使用：投影、拟合等
TH1D *proj = histogram->ProjectionY("proj", 32, 32);
proj->Fit("gaus", "RQ");
```

## JSON 清洗

THttpServer 返回的 JSON 中，某些字段（如 `fLabels` 为 `null`、`fFunctions` 包含无法反序列化的子对象）会导致 `ConvertFromJSON` 失败。需要用 jq 预处理：

```bash
jq '
  def empty_list:   {"_typename":"TList","name":"TList","arr":[],"opt":[]};
  def empty_hashlist: {"_typename":"THashList","name":"THashList","arr":[],"opt":[]};

  .fXaxis.fLabels = empty_hashlist |
  .fXaxis.fModLabs = empty_list |
  .fYaxis.fLabels = empty_hashlist |
  .fYaxis.fModLabs = empty_list |
  .fZaxis.fLabels = empty_hashlist |
  .fZaxis.fModLabs = empty_list |
  .fFunctions = empty_list
' raw.json > cleaned.json
```

替换规则：将 `null` 或不兼容的集合字段替换为空的 TList/THashList 结构体，确保 ROOT 能完整反序列化。

## 完整示例：定时抓取 + 拟合 + 追踪

### Bash 主脚本

```bash
#!/usr/bin/env bash
set -euo pipefail

BASE_URL="http://ribfana04:10101"
timestamp="$(date +%Y%m%d_%H%M%S)"
snapshot_dir="output/online/$timestamp"
mkdir -p "$snapshot_dir"

# 下载 + 清洗
for hist in HOD_idqu HOD_idqd; do
    curl --fail --silent --max-time 15 \
        "$BASE_URL/$hist/root.json" \
        --output "$snapshot_dir/$hist.json"

    jq '
      def empty_list: {"_typename":"TList","name":"TList","arr":[],"opt":[]};
      def empty_hashlist: {"_typename":"THashList","name":"THashList","arr":[],"opt":[]};
      .fXaxis.fLabels = empty_hashlist | .fXaxis.fModLabs = empty_list |
      .fYaxis.fLabels = empty_hashlist | .fYaxis.fModLabs = empty_list |
      .fZaxis.fLabels = empty_hashlist | .fZaxis.fModLabs = empty_list |
      .fFunctions = empty_list
    ' "$snapshot_dir/$hist.json" > "$snapshot_dir/$hist.json.tmp"
    mv "$snapshot_dir/$hist.json.tmp" "$snapshot_dir/$hist.json"
done

# 更新 latest 符号链接
ln -sfn "$timestamp" "output/online/latest"

# ROOT 分析
root -l -b -q "BarPeakAnalysis_Online.C(\"$snapshot_dir\",false)"
```

### ROOT 分析宏

```cpp
// BarPeakAnalysis_Online.C
#include "TBufferJSON.h"
#include "TH2.h"
#include "TF1.h"

TH2 *ReadHistogram(const char *jsonPath) {
    std::ifstream f(jsonPath);
    std::ostringstream buf;
    buf << f.rdbuf();
    TObject *obj = TBufferJSON::ConvertFromJSON(buf.str().c_str());
    TH2 *h = dynamic_cast<TH2 *>(obj);
    h->SetDirectory(nullptr);
    return h;
}

void FitPeak(TH2 *h, int xbin) {
    TH1D *proj = h->ProjectionY(Form("proj_%d", xbin), xbin, xbin);
    TF1 *fit = new TF1("fit", "gaus", 1200, 2500);
    proj->Fit(fit, "RQ");
    printf("xbin=%d  mean=%.0f  sigma=%.0f  chi2/ndf=%.1f\n",
           xbin, fit->GetParameter(1), fit->GetParameter(2),
           fit->GetChisquare() / fit->GetNDF());
}

void BarPeakAnalysis_Online(const char *dir = "output/online/latest",
                            bool draw = false) {
    TH2 *idqu = ReadHistogram(Form("%s/HOD_idqu.json", dir));
    TH2 *idqd = ReadHistogram(Form("%s/HOD_idqd.json", dir));

    FitPeak(idqu, 32);
    FitPeak(idqd, 32);
    FitPeak(idqu, 33);
    FitPeak(idqd, 33);
}
```

### 定时执行（crontab）

```crontab
# 每 15 分钟抓取一次
*/15 * * * * cd /path/to/peak_analysis && ./run_bar_peak_online.sh >> log.txt 2>&1
```

## 其他输出格式

THttpServer 支持多种后缀，按需选择：

| URL 后缀 | 格式 | 用途 |
|----------|------|------|
| `root.json` | ROOT JSON 序列化 | 编程读取，可用 `TBufferJSON` 还原 |
| `root.bin` | ROOT 二进制 | 高效传输，可用 `TBufferFile` 还原 |
| `root.png` | PNG 图片 | 快速预览 |
| `root.svg` | SVG 矢量图 | 网页嵌入 |
| `root.exe` | JSON + 执行命令 | 带绘图选项的完整数据 |

## 参考文档

- [ROOT THttpServer 官方文档](https://root.cern/doc/master/classTHttpServer.html)
- [JSROOT 文档](https://root.cern/js/)
- [TBufferJSON 文档](https://root.cern/doc/master/classTBufferJSON.html)
