# **日版索尼 Xperia 1 II 刷机后 FeliCa NFC 及 Suica 使用情况分析**

**1\. 引言**  
FeliCa NFC 技术是由索尼公司开发的一种非接触式 RFID 智能卡系统，在日本被广泛应用于电子货币、公共交通等领域 1。该技术以其快速的交易速度和高度的安全性而闻名，非常适合需要处理大量交易的场景 2。例如，在交通出行方面，FeliCa 技术被用于各种电子交通卡，其中最著名的当属由东日本旅客铁道株式会社（JR East）发行的 Suica（西瓜卡）1。Suica 不仅可以用作乘坐火车和公交的支付工具，还可以在许多商店作为电子货币使用 7。鉴于 FeliCa 和 Suica 在日本日常生活中扮演着重要的角色，用户对于日版手机刷入非日本版本系统后是否会影响其 FeliCa NFC 功能（特别是 Suica 的使用）非常关注。同时，用户也希望了解刷回原始日版系统是否能够保证 FeliCa NFC 功能的恢复。本报告将以索尼 Xperia 1 II 为例，深入分析刷机操作对 FeliCa NFC 功能的影响以及恢复的可能性。  
**2\. FeliCa NFC 技术原理及应用**

* **2.1 技术基础**  
  FeliCa 是一种近距离无线通信（NFC）技术，更具体地说是 NFC Type-F，其技术规范符合日本工业标准 JIS X 6319-4 1。在 NFC 的框架下，存在 Type-A、Type-B 和 Type-C 等标准，而 FeliCa 则属于 Type-F 3。FeliCa 与其他 NFC 技术共享 13.56 MHz 的工作频率，其无线通信距离通常在 2 至 10 厘米以内 1。FeliCa 的独特之处在于其优化的安全结构和更高的通信速度 3。例如，FeliCa 的数据传输速度可以高达 424 kbit/s 甚至 847 kbps，这使得交易能够在约 0.1 秒内完成 2。这种高速特性是其在日本高流量场景（如火车站）被广泛采用的关键原因 8。值得注意的是，无论是 FeliCa 卡片还是移动设备中的 FeliCa 实现，都依赖于读卡器提供的外部电源进行工作，自身无需电池 1。安全性方面，FeliCa 采用了动态生成的加密密钥，每次相互认证时都会生成新的密钥，有效防止欺诈行为 1。较新版本的 FeliCa IC 芯片还采用了先进的加密标准（AES）以提升安全性 1。FeliCa 技术不仅符合 JIS X 6319-4 标准，并由日本 IC 卡系统应用委员会（JICSAP）监管，同时也被纳入 NFC 论坛规范的合规性要求中 1。  
* **2.2 在日本的应用与普及**  
  FeliCa 在日本是事实上的非接触式智能卡系统标准 1。其应用范围极其广泛，涵盖了人们日常生活的多个方面 1。主要的电子货币包括 Edy、Rakuten Edy、nanaco 和 WAON 等 1。在公共交通领域，Suica、PASMO 和 ICOCA 等都是基于 FeliCa 技术的交通卡 1。此外，FeliCa 还被用作电子身份证（如学生证、员工卡和住宅门禁卡）、电子票务和会员卡（如登机牌、零售店和体育俱乐部会员卡）、电子申请以及消费电子和物联网设备的授权 2。特别值得一提的是“Mobile FeliCa”和“Osaifu-Keitai”（手机钱包）系统 1。Mobile FeliCa 是索尼针对移动设备开发的 FeliCa 技术 1，而 Osaifu-Keitai 则是日本标准的移动支付系统，它利用 Mobile FeliCa IC 芯片，允许用户在一台手机上使用多种 FeliCa 服务，例如 Suica 和 Edy 1。Osaifu-Keitai 系统的便利性使其在日本的移动支付生态系统中占据核心地位。为了适应日本市场，包括苹果和谷歌在内的主要智能手机平台都已将 FeliCa 技术集成到其产品中。例如，在日本销售的 iPhone 和 Apple Watch 支持通过 Apple Pay 使用 Suica 1，而日本销售的 Pixel 手机也通过 Google Pay 和 Osaifu-Keitai 系统支持 FeliCa 1。然而，这种支持通常仅限于在日本购买的型号 1。FeliCa 在日本的广泛应用和深度集成，使得拥有 FeliCa 功能对于在日本生活或旅行的用户来说至关重要。

**3\. FeliCa 在日版手机中的集成**

* **3.1 硬件组件**  
  日版手机实现 FeliCa 功能通常依赖于设备内部嵌入的专用硬件芯片 12。这个芯片与用于其他非接触式技术（如 Visa/Mastercard PayWave）的标准 NFC 芯片是不同的 12。虽然一些全球发售的手机型号可能配备了能够进行部分 FeliCa 通信（NFC-F）的 NFC 芯片，但在日本完整的 FeliCa 生态系统，特别是涉及金融数据（如 Suica 余额）的安全交易，往往需要这个专用的 FeliCa 硬件 12。例如，尽管全球版本的某些手机可能拥有能够支持 FeliCa 的 NFC 芯片，但在其全球 ROM 中，此功能并未被配置或启用 17。对于安卓手机而言，是否支持 FeliCa 通常取决于制造商是否获得了相关的 FeliCa 授权，并在为日本市场生产的手机中集成了必要的硬件 12。值得注意的是，并非所有在日本销售的安卓手机都具备 FeliCa 功能，这表明制造商在为不同市场和型号配置硬件时会做出特定的选择 12。  
* **3.2 软件与中间件**  
  除了硬件之外，软件驱动程序和中间件在实现 FeliCa 功能方面也起着至关重要的作用。这些组件通常是针对日本市场特定的，可能不会包含在全球 ROM 中 18。Osaifu-Keitai 框架的重要性不容忽视，它为各种基于 FeliCa 的服务提供了必要的 API 和系统级集成 1。Osaifu-Keitai 系统是日本标准的移动支付系统，它使用索尼的 Mobile FeliCa IC 芯片 1。该框架通过查找系统路径中的特定配置文件来判断是否支持 FeliCa 19。如果非日版 ROM 中缺少这些文件，系统将报告不支持 FeliCa。诸如 Mobile Suica 这样的应用程序也依赖于 Osaifu-Keitai 框架才能与 FeliCa 硬件进行交互 1。这些应用程序通常是为日本的软件生态系统设计的，可能无法在运行非日版 ROM 的手机上正常安装或使用。此外，即使硬件存在，ROM 也需要进行适当的配置以正确路由 FeliCa（Type F）通信。由于不同 SKU 的配置差异，这种路由在自定义 ROM 中可能会中断，导致手机无法作为虚拟卡使用 18。

**4\. 刷入非日版 ROM 对 FeliCa 功能的影响**

* **4.1 缺少驱动和配置**  
  对于日版索尼 Xperia 1 II 而言，刷入全球版或其他非日本版本的 ROM 很可能导致 FeliCa 功能失效。这是因为非日版 ROM 通常不包含与日版手机中 FeliCa 硬件进行交互所需的特定驱动程序 18。此外，启用 Android 系统中 FeliCa 路由和功能的系统级配置文件也可能不同或完全缺失 18。用户报告也证实了这一点。例如，有用户反映在将日版索尼 Xperia XZ2 Premium 刷入全球版 ROM 后，NFC 功能完全失效 20。这表明，全球版 ROM 由于缺少特定的驱动和配置，无法支持日版手机中的 FeliCa 硬件。  
* **4.2 Osaifu-Keitai 及相关应用缺失**  
  Osaifu-Keitai 应用程序及其底层框架通常预装在日版 ROM 中或可以方便地获取到。然而，这些组件可能不会包含在全球版 ROM 中，或者即使存在也可能由于缺少必要的依赖项而无法正常工作 18。自定义 ROM 的开发者甚至可能会移除这些应用程序或通过移除内核或设备节点中的驱动程序来破坏其功能 18。由于 Suica 等应用程序依赖于 Osaifu-Keitai 框架进行安全的交易管理，因此，即使某些基本的 NFC-F 通信在刷入全球版 ROM 后仍然可能存在，但由于缺少 Osaifu-Keitai 框架，FeliCa 的主要功能（如使用 Suica）将无法实现。  
* **4.3 区域锁定和软件标志**  
  日版 ROM 中可能存在特定的软件标志或区域锁定，专门用于启用 FeliCa 功能。这些标志在非日版 ROM 中可能不存在或设置不同，从而阻止 FeliCa 功能的激活 16。例如，有用户提到，尽管某些手机可能已经具备必要的硬件，但谷歌可能会通过型号和功能标志来锁定 FeliCa 功能 21。此外，在日本销售并支持 NFC 的安卓手机通常都应该支持 NFC-F，但这通常指的是为日本市场销售的手机，而非全球市场版本 21。这暗示了软件配置对于启用 FeliCa 功能的重要性。即使某些全球版手机的 NFC 芯片可能在硬件上支持 FeliCa，但由于缺少相应的软件标志和配置，该功能也可能无法使用 16。

**5\. 索尼 Xperia 1 II 与 FeliCa 支持**

* **5.1 日版型号与 FeliCa 硬件**  
  可以确认的是，日版索尼 Xperia 1 II 型号（如 SO-51A、SOG01 和 XQ-AT42）确实配备了 FeliCa 硬件 14。有明确指出，所有日版型号都支持“Felica”支付，这暗示了相关硬件的存在 14。与之相反，全球发售的 Xperia 1 II 型号通常不包含这种专用的 FeliCa 硬件 14。有用户提到，FeliCa 芯片仅存在于日版型号中 22。值得注意的是，日本运营商（如 Docomo 和 KDDI）销售的型号与 SIM 卡无锁的全球版型号在型号编号上有所不同 23。例如，SOG01 和 SO-51A 是日本市场的型号 23。这些不同的型号编号暗示了这些为日本市场定制的版本可能拥有特定的硬件配置（包括 FeliCa）和针对日本市场的软件。  
* **5.2 日版与全球版 ROM 的软件差异**  
  日版 Xperia 1 II 的 ROM 中包含了 Osaifu-Keitai 框架以及 FeliCa 功能所需的其他相关系统应用程序，而这些组件在全球版 ROM 中通常是不存在的 17。有信息表明，尽管全球版 Xperia 1V 的 NFC 芯片可能在硬件上支持 FeliCa，但在其全球版 ROM 中，此功能并未被配置或启用 17，这说明了软件配置的缺失。此外，日版和全球版 ROM 在预装应用程序、运营商特定的定制（对于运营商锁定的日版型号）以及可能针对日本市场优化的性能方面也存在差异 14。例如，有用户提到，与全球版相比，日版索尼设备的整体体验可能存在服务不佳、发热和性能较低等问题 14，这可能与软件优化有关。软件更新的发布时间也因运营商、市场和地区而异 29。最重要的是，即使将日版固件刷入全球版 Xperia 1 II，如果该全球版手机本身缺少 FeliCa 硬件，也无法启用 FeliCa 功能 14。

**6\. 刷回日版原厂系统恢复 FeliCa 功能的可能性**

* **6.1 硬件完整性**  
  假设刷机过程正确无误，且没有对手机硬件造成物理损坏，那么日版索尼 Xperia 1 II 中原有的 FeliCa 芯片应该仍然存在并且功能完好 18。有数据表明，与 Mobile FeliCa 相关的应用程序在刷机过程中不会受到影响，FeliCa 功能也不会被故意破坏，并且 FeliCa 数据在刷机后仍然保留 18。这说明，只要刷机操作规范，FeliCa 硬件本身不太可能在刷入非日版 ROM 后损坏。  
* **6.2 软件配置恢复**  
  理论上，将日版索尼 Xperia 1 II 刷回其原始的日版 ROM 应该能够恢复 FeliCa 功能所需的所有必要驱动程序、中间件（包括 Osaifu-Keitai）、配置文件和预装应用程序 18。有信息表明，如果在使用自定义 ROM 时 FeliCa 功能出现问题，可以通过恢复到官方安卓版本来修复 18。然而，恢复成功的关键在于使用与该特定日版型号（例如 SO-51A、SOG01）完全匹配的原始 ROM 30。刷入与型号不符的 ROM 可能会导致设备变砖等严重问题 30。因此，务必确保刷机过程能够完全覆盖非日版 ROM，并重新安装原始系统的所有必要分区和组件 30。刷入 ROM 的过程通常会擦除设备上的所有数据，因此，刷回原厂系统也应该能够清除之前刷入的非日版 ROM，并恢复到出厂时的软件状态 33。  
* **6.3 潜在的复杂情况**  
  在极少数情况下，如果用户之前解锁了手机的引导程序并进行了某些底层修改，那么刷回原厂系统后可能会出现一些小问题。尽管如此，有信息表明，解锁引导程序本身通常不会不可逆地破坏 FeliCa 功能 18。此外，如果用户之前已经设置了 Suica 或其他 FeliCa 服务，那么在刷回原厂系统后，可能需要重新注册或重新配置这些服务，具体取决于数据的存储方式 1。总的来说，刷回正确的原始日版 ROM 是恢复 FeliCa 功能最可靠的方法，因为它能够恢复手机出厂时预设的、与 FeliCa 硬件完美匹配的软件环境。

**7\. 引导程序解锁和自定义 ROM 的影响**

* **7.1 引导程序解锁**  
  解锁手机的引导程序通常是刷入自定义 ROM 的先决条件 18。需要注意的是，解锁引导程序可能会导致手机失去保修，并且通常会擦除设备上的所有数据 37。此外，解锁引导程序还会带来一定的安全风险，因为它会禁用“安全启动”这一重要的安全功能 38。值得注意的是，在某些日本运营商锁定的 Xperia 手机型号上，引导程序可能无法解锁 14。例如，有信息表明，某些 au、docomo 或 softbank 版本的 Xperia 手机理论上无法在日本境外使用其他运营商的服务，并且其引导程序也无法解锁 14。  
* **7.2 自定义 ROM 上的 FeliCa 功能**  
  在自定义 ROM 上使用 FeliCa 功能并不能得到保证，其支持情况因 ROM 而异 18。例如，有明确指出，对于日本用户而言，小米的某些自定义 ROM 不支持 FeliCa 40。自定义 ROM 的开发者可能不会包含 FeliCa 所需的驱动程序或配置，特别是如果该 ROM 不是专门为日本市场构建的 18。然而，也有一些高级用户尝试在非日版 ROM 上启用 FeliCa 功能（例如在 Google Pixel 手机上），但这通常需要 root 权限、解锁引导程序以及一定的技术专业知识，例如修改系统文件或使用自定义模块 17。尽管如此，由于安全考虑，与 FeliCa 相关的金融服务应用程序（如 Suica）可能无法在已解锁引导程序或运行自定义 ROM 的设备上正常工作（SafetyNet/Play Integrity 检测可能会失败）18。

**8\. 结论与建议**  
综上所述，日版索尼 Xperia 1 II 手机是配备了 FeliCa 硬件的。然而，刷入非日本版本的 ROM 很可能会导致 FeliCa 功能失效，这主要是由于缺少必要的驱动程序、系统配置以及 Osaifu-Keitai 框架。对于已经刷入非日版 ROM 并丢失 FeliCa 功能的用户，最有效的解决办法是刷回与该设备型号相匹配的原始日版 ROM。这样做应该能够恢复 FeliCa 功能，前提是刷机过程正确且硬件没有损坏。用户需要注意使用正确的固件版本，并确保刷机过程完整覆盖之前的系统。解锁引导程序和安装自定义 ROM 会进一步增加 FeliCa 支持的不确定性，可能无法保证功能的正常使用，并且可能带来安全风险，甚至影响相关应用程序的运行。因此，如果用户非常依赖 FeliCa 功能（特别是 Suica 的使用），建议避免在日版索尼 Xperia 1 II 上刷入非日版 ROM。如果已经刷入，则应谨慎地刷回正确的原始日版 ROM。在进行任何刷机操作之前，务必仔细阅读相关教程，并使用与设备型号完全匹配的固件，以避免对手机造成不可挽回的损坏。刷回原厂系统后，用户可能需要重新注册或配置其 FeliCa 服务。

| 应用类别 | 示例 | 相关 Snippet |
| :---- | :---- | :---- |
| 电子货币 | Edy, Rakuten Edy, nanaco, WAON, QUICPay | 1, 1, 1 |
| 公共交通支付 | Suica, PASMO, ICOCA, Kitaca, TOICA 等 | 1, 2, 7, 1, 8, 1, 5 |
| 电子身份证 | 学生证, 员工卡, 住宅门禁卡 | 2, 2, 5 |
| 电子票务/会员卡 | 登机牌, 零售店和体育俱乐部会员卡 | 2, 2, 5 |

| 型号 | 地区 | FeliCa 支持 | 相关 Snippet |
| :---- | :---- | :---- | :---- |
| SO-51A | 日本 (Docomo) | 是 | 23, 25 |
| SOG01 | 日本 (KDDI) | 是 | 23, 25, 43 |
| XQ-AT42 | 日本 (SIM-Free) | 是 | 23, 44, 25 |
| (Global) | 全球 | 否 | 14, 14, 22 |

#### **引用的著作**

1. FeliCa \- Wikipedia, 访问时间为 三月 25, 2025， [https://en.wikipedia.org/wiki/FeliCa](https://en.wikipedia.org/wiki/FeliCa)  
2. Overview of FeliCa \- What is FeliCa \- Sony Corporation, 访问时间为 三月 25, 2025， [https://www.sony.net/Products/felica/about/](https://www.sony.net/Products/felica/about/)  
3. Differences between NFC and Felica \- The world smallest RFID tag by SK-Electronics, 访问时间为 三月 25, 2025， [https://www.sk-el.co.jp/sales/rfid/en/glossary/b04.html](https://www.sk-el.co.jp/sales/rfid/en/glossary/b04.html)  
4. Host card emulation of FeliCa \- Android Open Source Project, 访问时间为 三月 25, 2025， [https://source.android.com/docs/core/connect/felica](https://source.android.com/docs/core/connect/felica)  
5. FeliCa \- Glossary \- DevX, 访问时间为 三月 25, 2025， [https://www.devx.com/terms/felica/](https://www.devx.com/terms/felica/)  
6. ​​​​​​​Introduction to FeliCa technology \- YouTube, 访问时间为 三月 25, 2025， [https://www.youtube.com/watch?v=q-GE0py4Mh4](https://www.youtube.com/watch?v=q-GE0py4Mh4)  
7. Suica \- Wikipedia, 访问时间为 三月 25, 2025， [https://en.wikipedia.org/wiki/Suica](https://en.wikipedia.org/wiki/Suica)  
8. Convenient electronic money cards FeliCa/Suica: Two cashless payment systems spreading in Japan \- WorkInJapan.today, 访问时间为 三月 25, 2025， [https://workinjapan.today/hightech/cashless-payment-systems-spreading-japan/](https://workinjapan.today/hightech/cashless-payment-systems-spreading-japan/)  
9. FeliCa \- About NFC \- Relationship between NFC and FeliCa \- Sony Corporation, 访问时间为 三月 25, 2025， [https://www.sony.net/Products/felica/NFC/relation.html](https://www.sony.net/Products/felica/NFC/relation.html)  
10. Osaifu-Keitai \- Wikipedia, 访问时间为 三月 25, 2025， [https://en.wikipedia.org/wiki/Osaifu-Keitai](https://en.wikipedia.org/wiki/Osaifu-Keitai)  
11. Advances with Osaifu-Keitai ―Starting Services Supporting NFC (Type A/B) on NTT DOCOMO UIM Cards―, 访问时间为 三月 25, 2025， [https://www.docomo.ne.jp/english/binary/pdf/corporate/technology/rd/technical\_journal/bn/vol15\_1/vol15\_1\_022en.pdf](https://www.docomo.ne.jp/english/binary/pdf/corporate/technology/rd/technical_journal/bn/vol15_1/vol15_1_022en.pdf)  
12. Suica Card for Android? : r/JapanTravelTips \- Reddit, 访问时间为 三月 25, 2025， [https://www.reddit.com/r/JapanTravelTips/comments/1adf4o8/suica\_card\_for\_android/](https://www.reddit.com/r/JapanTravelTips/comments/1adf4o8/suica_card_for_android/)  
13. Apple Pay to debut in Japan with FeliCa tap-to-pay support in 2016, report says, 访问时间为 三月 25, 2025， [https://appleinsider.com/articles/16/09/06/apple-pay-to-debut-in-japan-via-felica-tap-to-pay-in-2016-report-says](https://appleinsider.com/articles/16/09/06/apple-pay-to-debut-in-japan-via-felica-tap-to-pay-in-2016-report-says)  
14. Question \- Japan vs global | XDA Forums, 访问时间为 三月 25, 2025， [https://xdaforums.com/t/japan-vs-global.4543557/](https://xdaforums.com/t/japan-vs-global.4543557/)  
15. NFC-F / FeliCa support on rooted pixel 5? \- XDA Forums, 访问时间为 三月 25, 2025， [https://xdaforums.com/t/nfc-f-felica-support-on-rooted-pixel-5.4462157/](https://xdaforums.com/t/nfc-f-felica-support-on-rooted-pixel-5.4462157/)  
16. How To Guide \- How to enable FeliCa's Osaifu-Keitai in a Non-Japanese Google Pixel 6a (step by step tutorial) | XDA Forums, 访问时间为 三月 25, 2025， [https://xdaforums.com/t/how-to-enable-felicas-osaifu-keitai-in-a-non-japanese-google-pixel-6a-step-by-step-tutorial.4662302/](https://xdaforums.com/t/how-to-enable-felicas-osaifu-keitai-in-a-non-japanese-google-pixel-6a-step-by-step-tutorial.4662302/)  
17. NFC Felica in the 1V? : r/SonyXperia \- Reddit, 访问时间为 三月 25, 2025， [https://www.reddit.com/r/SonyXperia/comments/15hcvwb/nfc\_felica\_in\_the\_1v/](https://www.reddit.com/r/SonyXperia/comments/15hcvwb/nfc_felica_in_the_1v/)  
18. Mobile FeliCa support with custom ROM : u/FelicaDude \- Reddit, 访问时间为 三月 25, 2025， [https://www.reddit.com/user/FelicaDude/comments/ktmnf0/mobile\_felica\_support\_with\_custom\_rom/](https://www.reddit.com/user/FelicaDude/comments/ktmnf0/mobile_felica_support_with_custom_rom/)  
19. Enabling Osaifu-Keitai function on non-Japanese Google Pixel phones. \- GitHub, 访问时间为 三月 25, 2025， [https://github.com/kormax/osaifu-keitai-google-pixel](https://github.com/kormax/osaifu-keitai-google-pixel)  
20. How to Install global ROM on a Japan Sony XPERIA device I FixandMore I WINDOWS PC, 访问时间为 三月 25, 2025， [https://www.youtube.com/watch?v=nj7dkFb4A50](https://www.youtube.com/watch?v=nj7dkFb4A50)  
21. Nfc felicia Android Compatible phone. : r/japanlife \- Reddit, 访问时间为 三月 25, 2025， [https://www.reddit.com/r/japanlife/comments/148ekhp/nfc\_felicia\_android\_compatible\_phone/](https://www.reddit.com/r/japanlife/comments/148ekhp/nfc_felicia_android_compatible_phone/)  
22. Which models have the FeliCa Chip? : r/SonyXperia \- Reddit, 访问时间为 三月 25, 2025， [https://www.reddit.com/r/SonyXperia/comments/1hjoh20/which\_models\_have\_the\_felica\_chip/](https://www.reddit.com/r/SonyXperia/comments/1hjoh20/which_models_have_the_felica_chip/)  
23. Sony Xperia 1 II \- Wikipedia, 访问时间为 三月 25, 2025， [https://en.wikipedia.org/wiki/Sony\_Xperia\_1\_II](https://en.wikipedia.org/wiki/Sony_Xperia_1_II)  
24. Xperia 1ii Variants and Regions \- XDA Forums, 访问时间为 三月 25, 2025， [https://xdaforums.com/t/xperia-1ii-variants-and-regions.4112083/](https://xdaforums.com/t/xperia-1ii-variants-and-regions.4112083/)  
25. Is getting a second hand xperia 1 mk ii(Japan Variant) in 2023 worth it? \- XDA Forums, 访问时间为 三月 25, 2025， [https://xdaforums.com/t/is-getting-a-second-hand-xperia-1-mk-ii-japan-variant-in-2023-worth-it.4528349/](https://xdaforums.com/t/is-getting-a-second-hand-xperia-1-mk-ii-japan-variant-in-2023-worth-it.4528349/)  
26. Xperia 1 vs Xperia 1 II \- How do they perform with Android 11? \- YouTube, 访问时间为 三月 25, 2025， [https://www.youtube.com/watch?v=kkHH9SGEF9g](https://www.youtube.com/watch?v=kkHH9SGEF9g)  
27. Xperia 1 II vs Galaxy S20 Ultra \- I've made my decision\! Do you agree? \- YouTube, 访问时间为 三月 25, 2025， [https://www.youtube.com/watch?v=M8TwXEm0uXk](https://www.youtube.com/watch?v=M8TwXEm0uXk)  
28. Any Xperia 1iii region-specific differences? : r/SonyXperia \- Reddit, 访问时间为 三月 25, 2025， [https://www.reddit.com/r/SonyXperia/comments/pz7atz/any\_xperia\_1iii\_regionspecific\_differences/](https://www.reddit.com/r/SonyXperia/comments/pz7atz/any_xperia_1iii_regionspecific_differences/)  
29. Xperia 1 II software release overview \- Sony UK, 访问时间为 三月 25, 2025， [https://www.sony.co.uk/electronics/support/articles/00293714](https://www.sony.co.uk/electronics/support/articles/00293714)  
30. Changing roms \- Sony, 访问时间为 三月 25, 2025， [https://community.sony.com.mk/t5/1-series/changing-roms/td-p/3919163](https://community.sony.com.mk/t5/1-series/changing-roms/td-p/3919163)  
31. Does flashing roms again and again it effect hardware health \- XDA Forums, 访问时间为 三月 25, 2025， [https://xdaforums.com/t/does-flashing-roms-again-and-again-it-effect-hardware-health.3253844/](https://xdaforums.com/t/does-flashing-roms-again-and-again-it-effect-hardware-health.3253844/)  
32. Is it possible to kill your phone by installing wrong system software? \[duplicate\], 访问时间为 三月 25, 2025， [https://android.stackexchange.com/questions/55866/is-it-possible-to-kill-your-phone-by-installing-wrong-system-software](https://android.stackexchange.com/questions/55866/is-it-possible-to-kill-your-phone-by-installing-wrong-system-software)  
33. Xperia X10: Flashing Wolf's Tweaked v2.3 Gingerbread Firmware \- YouTube, 访问时间为 三月 25, 2025， [https://www.youtube.com/watch?v=zHBYJW2verg](https://www.youtube.com/watch?v=zHBYJW2verg)  
34. Android's E-Waste Problem Can't Be Solved With Custom ROMs \- VICE, 访问时间为 三月 25, 2025， [https://www.vice.com/en/article/androids-e-waste-problem-cant-be-solved-with-custom-roms/](https://www.vice.com/en/article/androids-e-waste-problem-cant-be-solved-with-custom-roms/)  
35. Unlocking Bootloaders \- postmarketOS Wiki, 访问时间为 三月 25, 2025， [https://wiki.postmarketos.org/wiki/Unlocking\_Bootloaders](https://wiki.postmarketos.org/wiki/Unlocking_Bootloaders)  
36. Lock and unlock the bootloader | Android Open Source Project, 访问时间为 三月 25, 2025， [https://source.android.com/docs/core/architecture/bootloader/locking\_unlocking](https://source.android.com/docs/core/architecture/bootloader/locking_unlocking)  
37. How to unlock bootloader on Android \- MOBILedit Forensic, 访问时间为 三月 25, 2025， [https://forensic.manuals.mobiledit.com/MM/how-to-unlock-bootloader-on-android](https://forensic.manuals.mobiledit.com/MM/how-to-unlock-bootloader-on-android)  
38. A discussion about bootloader locking/unlocking... AKA I want to relock my bootloader, should I? : r/LineageOS \- Reddit, 访问时间为 三月 25, 2025， [https://www.reddit.com/r/LineageOS/comments/n7yo7u/a\_discussion\_about\_bootloader\_lockingunlocking/](https://www.reddit.com/r/LineageOS/comments/n7yo7u/a_discussion_about_bootloader_lockingunlocking/)  
39. What "exactly" are the risks of an unlocked bootloader? : r/privacy \- Reddit, 访问时间为 三月 25, 2025， [https://www.reddit.com/r/privacy/comments/v8brr7/what\_exactly\_are\_the\_risks\_of\_an\_unlocked/](https://www.reddit.com/r/privacy/comments/v8brr7/what_exactly_are_the_risks_of_an_unlocked/)  
40. Does the POCO F6Pro purchased in Japan still support Felica after installing xiaomi.eu firmware?, 访问时间为 三月 25, 2025， [https://xiaomi.eu/community/threads/does-the-poco-f6pro-purchased-in-japan-still-support-felica-after-installing-xiaomi-eu-firmware.73517/](https://xiaomi.eu/community/threads/does-the-poco-f6pro-purchased-in-japan-still-support-felica-after-installing-xiaomi-eu-firmware.73517/)  
41. Felica hardware support for Japanese models? \- GrapheneOS Discussion Forum, 访问时间为 三月 25, 2025， [https://discuss.grapheneos.org/d/11697-felica-hardware-support-for-japanese-models](https://discuss.grapheneos.org/d/11697-felica-hardware-support-for-japanese-models)  
42. jjyao88/unlock-felica-pixel: Unlock Felica on non-Japanese Pixel devices that you can use Felica cards in Japan\! \- GitHub, 访问时间为 三月 25, 2025， [https://github.com/jjyao88/unlock-felica-pixel](https://github.com/jjyao88/unlock-felica-pixel)  
43. Xperia 1 II driver \- Developer World \- Sony, 访问时间为 三月 25, 2025， [https://developer.sony.com/file/download/xperia-1-ii-driver](https://developer.sony.com/file/download/xperia-1-ii-driver)  
44. Sim-free ver. of Xperia's Latest High-end Model "Xperia 1 II"\! \- Saiga NAK, 访问时间为 三月 25, 2025， [https://saiganak.com/product/sony-xperia-1-ii-sim-free/](https://saiganak.com/product/sony-xperia-1-ii-sim-free/)