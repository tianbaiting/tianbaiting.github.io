# 网络检测工具与跨运营商路由排障手册

> 适用：Linux / macOS / Windows；包括无 `sudo` 权限的学校或实验室主机。  
> 示例目标：Hostwinds `104.168.141.83`；域名 `tbt73.duckdns.org`。  
> 更新：2026-11-07。在线平台的节点和配额会变化，使用前确认页面实际可选的探针。

## 0. 先理解：各层工具在测什么

| 层次 / 问题 | 典型工具 | 成功说明 | 边界 |
|---|---|---|---|
| DNS：名字→地址 | `dig`、`nslookup` | 拿到 A / AAAA 记录 | 地址可达性另测 |
| ICMP：回声响应 | `ping` | ICMP 往返正常，有 RTT | ICMP 被过滤 ≠ TCP 也不通 |
| TCP：能否握手 | `nc`、`curl`、`Test-NetConnection`、在线 TCPing | SYN→SYN-ACK→ACK 完成 | 握手成功 ≠ 应用层正常 |
| UDP：应用收发 | 协议专用客户端、双端抓包 | 特定 UDP 应用响应 | `nc -u` 不报错不代表对端收到 |
| 路径：经过哪些节点 | `traceroute`、`tracepath`、`tracert` | 部分路径节点 IP/RTT | `* * *` 只是该跳未回应探测 |
| 路由归属 | BGP.tools、RIPEstat、Team Cymru | IP 前缀 / 起源 ASN / AS_PATH | 查归属，查不出封锁名单 |
| 应用层 | `curl`、`ssh`、VPN 客户端 | 该业务可用 | 一种业务的结果不覆盖其他端口/协议 |

**连接有去程和回程。** TCP 三次握手需要 SYN、SYN-ACK、ACK 分别在两个方向完成。服务器收到 SYN 但客户端始终 `SYN-SENT`，要靠服务器抓包判断 SYN-ACK 有没有发出、发出后是否被回程丢弃。同理，两端发起的 traceroute 走的是不同方向，探测包也未必跟着真实 TCP 流量。

---

## 1. 不用 sudo 的常用命令

### 1.1 Linux / macOS：先按问题选择工具

```bash
# 问题 A：目标 IPv4 是否回应 ICMP？
ping -c 5 104.168.141.83

# 问题 B：443 端口的 TCP 能不能连接？
nc -vz -w 8 104.168.141.83 443

# 问题 C：普通路径经过哪些路由器？
traceroute 104.168.141.83

# 问题 D：Linux 上更适合无 sudo 用户的路径检测（若已安装）
tracepath 104.168.141.83

# 问题 E：域名的 IPv4 和 IPv6 分别是什么？
dig +short A tbt73.duckdns.org
dig +short AAAA tbt73.duckdns.org

# 问题 F：从当前网络出去时，自己呈现的公网 IPv4 是多少？
curl -4 https://api.ipify.org
```

`ping -c 5` 是 Linux/macOS 写法。`traceroute`/`tracepath` 通常不需管理员权限，但 TCP 模式可能需要。`nc` 有多种实现，先 `nc -h` 看支持什么；不支持 `-4` 就直接用 IPv4 数字地址。

### 1.2 Windows（普通 PowerShell，不要求管理员）

```powershell
# 5 次 ICMP 测试
ping -n 5 104.168.141.83

# TCP 443 连通性；关心输出 TcpTestSucceeded
Test-NetConnection 104.168.141.83 -Port 443

# 路径追踪
tracert 104.168.141.83

# 查询 A / AAAA
nslookup -type=A tbt73.duckdns.org
nslookup -type=AAAA tbt73.duckdns.org

# 查看公网 IPv4
curl.exe -4 https://api.ipify.org
```

`Test-NetConnection` 是 PowerShell 命令。`tracert` 用 ICMP，Linux `traceroute` 默认 UDP，协议不同，结果别直接对比。

### 1.3 强制对比 IPv4 和 IPv6

```bash
ping -4 -c 5 tbt73.duckdns.org  # Linux：IPv4 ICMP
ping -6 -c 5 tbt73.duckdns.org  # Linux：IPv6 ICMP

curl --ipv4 --connect-timeout 8 -v https://tbt73.duckdns.org/
curl --ipv6 --connect-timeout 8 -v https://tbt73.duckdns.org/

ssh -4 user@tbt73.duckdns.org
ssh -6 user@tbt73.duckdns.org
```

`--ipv4`/`--ipv6` 是 curl 长选项，比短参数好记。如果 443 跑的是 VLESS，curl 会报 TLS/HTTP 错误，但只要看到 `Connected to ...` 就说明 TCP 通了。

---

## 2. `nc`（netcat）怎么理解，不用死记短参数

`nc` 是一个简单的 TCP/UDP 连接工具，**不是固定一种实现**。OpenBSD nc、GNU netcat、BusyBox nc 等支持的选项会不同。

```bash
nc -h          # 先看自己的版本支持什么
nc -vz -w 8 104.168.141.83 443
```

拆开看：

| 符号 | 英文原意 | 实际作用 |
|---|---|---|
| `nc` | netcat | 建立网络连接、监听或测试端口 |
| `-v` | verbose | 详细输出成功或失败 |
| `-z` | zero-I/O | 只检查连接，不传应用数据 |
| `-w 8` | wait | 等待/超时上限设为 8 秒（实现有差别） |
| `104.168.141.83` | host | 目标地址；IPv4 数字地址不需再加 `-4` |
| `443` | port | 要访问的 TCP 端口 |

你遇到的 `nc: invalid option -- '4'` **只说明该 nc 版本不支持 `-4`，不是 IPv4 网络故障**。

如何看结果：

- **succeeded / open**：TCP 握手成功。
- **Connection refused**：目标发了 RST，端口没监听或被防火墙拒绝。
- **timed out**：连接超时，可能是去程、回程丢包或防火墙静默丢弃。
- **invalid option**：命令语法或版本问题，和网络无关。

`nc -u` 走 UDP，但 UDP 没报错不代表对端收到。测 OpenVPN、Hysteria2 直接用实际客户端加抓包更可靠。

---

## 3. `curl`：把“连不上”和“应用报错”分开

```bash
# 限制连接阶段最多等待 8 秒，并显示连接过程
curl --ipv4 --connect-timeout 8 --verbose https://tbt73.duckdns.org/

# 测试原始 IPv4，但证书校验和 HTTPS 虚拟主机可能与域名不同
curl --ipv4 --connect-timeout 8 --verbose https://104.168.141.83/

# 强制使用特定 IPv4，同时保留域名、Host、TLS SNI（仅 HTTPS 服务）
curl --resolve tbt73.duckdns.org:443:104.168.141.83 \
  --connect-timeout 8 --verbose https://tbt73.duckdns.org/
```

- `--connect-timeout 8`：包括 DNS、TCP 与 TLS 协商等连接建立过程的总等待上限（以 curl 版本和协议行为为准）。
- `--verbose`：显示解析到哪个 IP、是否出现 `Connected to ...`、TLS 过程等。
- `--resolve 域名:端口:IP`：临时指定该域名的解析，适合排除 DNS 引起的差异。
- 看到 `Connected to ...` 说明 TCP 已建立。之后的证书错误、HTTP 错误属于更上层的问题。

443 上跑 VLESS 时 curl 拿不到正常 HTTP 响应，但仍然能观察 TCP/TLS 握手阶段是否成功。

---

## 4. `traceroute` / `tracepath` / `mtr`：路由怎么看

```bash
# macOS/Linux：普通追踪
traceroute 104.168.141.83

# Linux：无 root 友好的路径追踪（需系统已有此命令）
tracepath 104.168.141.83

# Linux：若版本及权限支持，使用与实际业务更接近的 TCP 443 探测
traceroute -T -p 443 104.168.141.83

# Linux：若已安装 mtr，观察延迟和丢包趋势
mtr 104.168.141.83

# Windows
tracert 104.168.141.83
```

`traceroute` 利用递增 TTL / IPv6 Hop Limit 触发中间设备的超时回应。Linux 的 `tracepath` 还能帮助观察 Path MTU。`mtr` 则反复探测并展示路径状态，部分系统/模式需要额外权限或预配置。

**怎么读每一跳？**

| 输出 | 正确含义 |
|---|---|
| `1  192.168.1.1` | 第一跳往往是本地/内网网关 |
| `2  10.x.x.x` | 运营商/学校的私有地址段，查 ASN 无意义 |
| `8  203.0.113.1` | 示例 IP；真实输出需要再查 ASN（`203.0.113.0/24` 是文档示例网段） |
| `* * *` | 该跳未回应探测（限速、策略等），不等于封锁 |
| 某跳延迟高、下一跳正常 | 多半是路由器控制面限速，转发面未必慢 |

traceroute 每跳同时依赖去程和超时回复的回程，ECMP 还可能让探测包和真实 TCP 走不同路径。第一处 `*` 不代表封锁点。

---

## 5. DNS、IP、ASN、BGP 的区别

- **A 记录**：域名 → IPv4，例如 `104.168.141.83`。
- **AAAA 记录**：域名 → IPv6。
- **IP 地址**：一台主机或路由器接口的地址。
- **前缀/CIDR**：一段地址，如 `x.y.z.0/24`（包含 256 个 IPv4 地址）。
- **ASN（自治系统号）**：在 BGP 中代表一个独立路由管理域。CERNET 常见 `AS4538`，电信常见 `AS4134`，但实际出口可能有其他 AS。
- **BGP**：网络之间交换“这个 IP 前缀应该从哪个 AS 方向走”的路由信息。
- **AS_PATH**：某个观察点所见到的 BGP AS 序列；它并不是逐台路由器的物理转发轨迹。

查询某跳 IP 的起源 ASN：

```bash
whois -h whois.cymru.com " -v 166.111.26.31"
```

这里 `-h` 是 whois 的参数（指定查询服务器），`" -v ..."` 是发给 Team Cymru 的查询串，和 `nc -v` 没关系。

---

## 6. 在线检测网站总表

| 平台 | 地址 | 适合做什么 | CERNET 注意事项 |
|---|---|---|---|
| **17CE（一起测）** | https://www.17ce.com/traceroute | 分地区/运营商路由追踪、Ping、TCPing 等 | 有"教育网"筛选，但不保证当时有在线节点 |
| **ITDOG** | https://www.itdog.cn/ | 电信、联通、移动及港澳台/海外的 Ping、TCPing、路由追踪、DNS | 截图所示选项没有教育网，电信节点 ≠ CERNET |
| **RIPE Atlas** | https://atlas.ripe.net/ | 从全球分布式探针运行 Ping / traceroute / DNS 等 | 可尝试选择 `AS4538`；须有可用探针；自定义测量需要积分 |
| **Globalping** | https://globalping.io/ | 全球社区探针 Ping、traceroute、MTR、DNS、HTTP | 支持按地点、运营商、**ASN** 等条件查找探针；并非保证存在 AS4538 探针 |
| **BGP.tools** | https://bgp.tools/as/4538 | 查询 CERNET ASN、前缀、BGP 邻接、路由 | BGP 数据，不等于实时封锁名单 |
| **RIPEstat** | https://stat.ripe.net/ | 查询 IP/ASN、BGP 可见性、历史、Looking Glass | 可看 BGP 路由，定位丢包设备需结合其他方法 |
| **Hurricane Electric BGP Toolkit** | https://bgp.he.net/ | ASN、前缀、Peers/Upstreams、路由注册信息 | BGP 视图，不等同于实际 TCP 路径 |
| **Team Cymru IP→ASN** | https://www.team-cymru.com/ip-asn-mapping | 将 traceroute 跳点 IP 批量映射成 ASN 和前缀 | 起源 AS ≠ 物理设备所属运营商 |

**按问题选平台：**

1. 想知道“**国内哪些运营商能连 `104.168.141.83:443`**”：ITDOG TCPing。
2. 想看“**教育网节点能否连接、路由怎么走**”：优先查看 17CE 的教育网筛选实际有没有在线节点；再试 RIPE Atlas / Globalping 的 `AS4538` 探针。
3. 想知道“**某跳 IP 属于哪个 ASN、有哪些上游**”：Team Cymru、BGP.tools、RIPEstat。
4. 想看“**来自美国 Hostwinds 的回程**”：从 Hostwinds 或美国侧探针发起测量，教育网去程 traceroute 看不到回程路径。

---

## 7. 专项案例：Hostwinds IPv4 对 CERNET 不通，但电信可通

### 已知观察

- Hostwinds 目标 IPv4：`104.168.141.83`。
- 清华、复旦、上交相关校园网对该 IPv4 的连接失败；另一位同学使用中国电信和公司 Wi-Fi 可以访问。
- 某受影响客户端发出的 TCP SYN 到达 Hostwinds（服务器上观察到 `SYN-RECV`）。
- 客户端未完成 TCP 三次握手，443 和 39999 曾出现超时。
- 部分其他网络及 IPv6 访问正常。

### 尚待排除的可能性

- 多所学校不通，但各校出口、校园策略可能不同，不能直接推出"整个 CERNET 屏蔽了该 IP"。
- 服务器 `SYN-RECV` 只说明 SYN 到了内核，SYN-ACK 是否真正从公网接口发出、回程是否被丢，仍需抓包确认。
- ICMP 丢包和 TCP 丢包的过滤位置和策略可以完全不同。

### 不需要管理员权限的最小实验

每位同学用当前实际网络，在同一时间段跑下面三条：

**Linux / macOS**

```bash
curl -4 https://api.ipify.org
nc -vz -w 8 104.168.141.83 443
traceroute 104.168.141.83
```

**Windows PowerShell**

```powershell
curl.exe -4 https://api.ipify.org
Test-NetConnection 104.168.141.83 -Port 443
tracert 104.168.141.83
```

记录实验表：

| 时间（注明时区） | 来源地点/运营商 | 公网出口 IPv4 | 出口 ASN | 目标 IP/端口 | TCP 成功？ | 路由报告链接/文件 |
|---|---|---|---|---|---|---|
| 待填 | 清华校园网 | 待填 | 待查 | `104.168.141.83:443` | 失败（已有报告） | 待填 |
| 待填 | 复旦校园网 | 待填 | 待查 | 同上 | 失败（已有报告） | 待填 |
| 待填 | 上交校园网 | 待填 | 待查 | 同上 | 失败（已有报告） | 待填 |
| 待填 | 中国电信 | 待填 | 待查 | 同上 | 成功（已有报告） | 待填 |
| 待填 | 公司 Wi-Fi | 待填 | 待查 | 同上 | 成功（已有报告） | 待填 |

共享截图或日志前给公网 IP 打码。确认没开代理/WARP/VPN，否则出口 IP 不是本地运营商的。

### Hostwinds 侧的验证（**需要管理员/root 权限**）

```bash
# 先看发往客户端公网 IP 选择哪条路由
ip -4 route get CLIENT_PUBLIC_IPV4

# 目标连接时抓包：核实 SYN 是否到达、SYN-ACK 是否真正发出
sudo tcpdump -nni any 'host CLIENT_PUBLIC_IPV4 and tcp port 443'

# 反方向路由探测（不是 SYN-ACK 的完全等价替代）
traceroute CLIENT_PUBLIC_IPV4
```

**抓包阅读方法：**

- 客户端 `SYN` 到服务器、服务器无 `SYN-ACK`：优先检查本机防火墙、监听端口、策略路由。
- 服务器网卡出现 `SYN-ACK`、客户端网卡没有：回程链路/入口过滤问题；仍需上游或校园网网关协助进一步精确定位。
- 客户端收到 `SYN-ACK` 但没有回 `ACK`：检查客户端系统、防火墙、连接跟踪、抓包位置。
- 服务器抓到完整三次握手：再检查 TLS、SSH、VLESS、OpenVPN 等应用层。

### 判断哪些 Hostwinds IP 被 CERNET 阻断

在自己有授权的目标之间做对照：同一 CERNET 测点、同一端口、相近时间，测试不同的 Hostwinds IPv4；再用电信节点验证。同一前缀普遍失败说明前缀相关异常，但不等于黑名单。别对别人的 IP 段做大规模扫描。

### 可能的解决办法

- **IPv6 正常就优先使用 IPv6**：如 `ssh -6`、应用配置 AAAA 直连。
- **换 Hostwinds IPv4 / 不同前缀**：如果怀疑当前地址或回程前缀问题，先验证新地址的 CERNET 可达性。
- **改变出口路径**：中转 VPS、Cloudflare Tunnel、WARP 等，选定后分别验证 TCP/UDP 可用性。
- **运营商排障**：提交双向抓包、时间、源/目的公网 IP、端口、TCP 四元组和路径报告给 Hostwinds 与校园网运维。

---

## 8. 一分钟选工具（按问题）

| 你的问题 | 首选方法 |
|---|---|
| 域名是 IPv4 还是 IPv6？ | `dig A` / `dig AAAA` |
| 远端 IP 完全不通？ | 先 `ping`，但紧跟 TCP 端口测试 |
| 443 端口能连吗？ | `nc -vz -w 8 IP 443` / Windows `Test-NetConnection IP -Port 443` |
| 不想记 nc 参数？ | Windows 用 `Test-NetConnection`；Linux/macOS 可用 `curl --connect-timeout 8 --verbose URL`（仅适合对应协议） |
| 没 sudo 想看路由？ | Linux `tracepath` / `traceroute`；Windows `tracert` |
| 想查学校出口公网 IP？ | `curl -4 https://api.ipify.org` |
| 想比较国内三大运营商？ | ITDOG TCPing / 路由追踪 |
| 专门测试 CERNET？ | 17CE 教育网筛选（先确认探针），RIPE Atlas / Globalping ASN 探针 |
| 想查某一跳属于哪家？ | Team Cymru IP→ASN，BGP.tools |
| 想证明第 2 次 TCP 握手丢在哪里？ | 两端 `tcpdump` + 网关/上游协助；单靠 traceroute 不够 |

## 9. 参数速记：优先记含义，不记字母

| 完整写法 / 缩写 | 含义 | 例子 |
|---|---|---|
| `--ipv4`（curl） | 只选 IPv4 | `curl --ipv4 URL` |
| `--ipv6`（curl） | 只选 IPv6 | `curl --ipv6 URL` |
| `--connect-timeout 8`（curl） | 连接阶段最长等 8 秒 | `curl --connect-timeout 8 URL` |
| `--verbose`（curl） | 显示详细过程 | `curl --verbose URL` |
| `-c 5`（Linux/macOS ping） | 发 5 个包，`count` | `ping -c 5 IP` |
| `-n 5`（Windows ping） | 发 5 个包 | `ping -n 5 IP` |
| `-v`（nc） | 详细输出，`verbose` | `nc -v ...` |
| `-z`（nc） | 零数据，仅探测连接 | `nc -z ...` |
| `-w 8`（nc） | 等待上限 8 秒，`wait` | `nc -w 8 ...` |
| `-T`（部分 Linux traceroute） | 使用 TCP 探测 | `traceroute -T -p 443 IP` |
| `-p 443`（traceroute） | 目标探测端口，`port` | `traceroute -T -p 443 IP` |
| `-n`（traceroute） | 数字地址，不反查名称 | `traceroute -n IP` |
| `-4` / `-6` | 在**支持该选项的命令**里选 IP 版本 | 不是所有 `nc` 都支持 |
| `-Port 443`（PowerShell） | 指定 TCP 端口 | `Test-NetConnection IP -Port 443` |

## 10. 参考链接

- 17CE 路由追踪：https://www.17ce.com/traceroute
- ITDOG：https://www.itdog.cn/
- RIPE Atlas 使用说明：https://atlas.ripe.net/docs/getting-started/user-defined-measurements
- Globalping：https://globalping.io/
- RIPEstat：https://stat.ripe.net/
- BGP.tools CERNET：https://bgp.tools/as/4538
- Hurricane Electric BGP Toolkit：https://bgp.he.net/
- Team Cymru IP→ASN：https://www.team-cymru.com/ip-asn-mapping
- Linux `tracepath` 手册：https://man7.org/linux/man-pages/man8/tracepath.8.html
- Linux `traceroute` 手册：https://man7.org/linux/man-pages/man8/traceroute.8.html
- Windows `Test-NetConnection` 官方文档：https://learn.microsoft.com/en-us/powershell/module/nettcpip/test-netconnection

> 一个测试回答一个问题。各层证据各管各的，拼起来才有意义。
