# Gemini 使用限制与付费模式解析

本文档旨在澄清 Gemini 在不同平台（网页版、CLI、API）上的使用限制，以及 Google AI Pro 订阅与 API 付费之间的关系。

---

## 核心结论

1.  **产品分离**：**Google AI Pro 订阅**（消费者产品）和 **Gemini API**（开发者产品）是两个完全独立的服务和计费体系。
2.  **权益范围**：AI Pro 订阅的权益**仅限于**网页版 `gemini.google.com` 及集成的 Google 应用，**不适用于** API 或 CLI。
3.  **CLI 登录福利**：通过个人 Google 账户登录 CLI，可享受一个非常慷慨的免费套餐，这与是否订阅 AI Pro 无关。

---

## 各平台限制对比总表

| 平台 | 使用方式 | 主要可用模型 | 请求/问答限制 | 其他关键限制 |
| :--- | :--- | :--- | :--- | :--- |
| **网页版** | **免费版** | Gemini 2.5 Pro | 每天 **5** 次提问 | 图片: 100张/天<br>上下文: 32k tokens |
| | **付费版 (AI Pro)** | Gemini 2.5 Pro | 每天 **100** 次提问 | 图片: 1000张/天<br>上下文: 1M tokens<br>视频: 3个/天 |
| **CLI/API** | **个人 Google 账户登录** | Gemini 2.5 Pro | **60** RPM / **1000** RPD | 上下文: 1M tokens |
| | **免费 API 密钥** | Flash 模型 | **10** RPM / **250** RPD | 模型能力相对基础 |
| | **付费 API 密钥** | Gemini 1.5/2.5 Pro 等 | 根据购买的配额 | 按量付费 (Pay-as-you-go) |

*RPM: 每分钟请求数; RPD: 每天请求数*

---

## 场景分析

### 场景一：我是 AI Pro 用户，如果取消订阅会怎样？

您的 AI Pro 订阅状态**仅影响网页版**的限额，不影响通过账户登录的 CLI。

#### **网页版**限额变化

| 功能 | 订阅中 (Pro 用户) | 取消后 (变为免费用户) |
| :--- | :--- | :--- |
| **模型问答** | 每天 100 次 | 每天 5 次 |
| **图片生成** | 每天 1,000 张 | 每天 100 张 |
| **上下文窗口** | 100万 tokens | 32,000 tokens |

#### **CLI 版 (账户登录)** 限额变化

| 功能 | 订阅中 (Pro 用户) | 取消后 (变为免费用户) |
| :--- | :--- | :--- |
| **请求频率** | 60 RPM / 1000 RPD | **60 RPM / 1000 RPD (不变)** |
| **可用模型** | Gemini 2.5 Pro | **Gemini 2.5 Pro (不变)** |

---

### 场景二：如何在 Python 中使用 Pro 模型？

使用免费 API 密钥**无法**调用 Pro 模型。您必须使用与**启用了结算功能的 Google Cloud 项目**关联的 API 密钥。

```python
import google.generativeai as genai

# 必须使用与付费GCP项目关联的API Key
genai.configure(api_key="YOUR_PAID_API_KEY")

# 明确指定要使用的Pro模型
# 如果API Key是免费版，执行这行代码会失败
model = genai.GenerativeModel('gemini-1.5-pro-latest')

response = model.generate_content("讲一个关于程序员的笑话")
print(response.text)
```

---

## 常见问题解答 (FAQ)

**问：我的 AI Pro 订阅能让我在使用 API 时有折扣或免费额度吗？**

**答：不能。** AI Pro 订阅和 API 付费是两条完全独立的付费路径。前者是为增强网页体验，后者是为程序化开发。

**问：我的 AI Pro 订阅能提升我用谷歌账号登录 CLI 时的限额吗？**

**答：不能。** 通过账户登录 CLI 的限额（60 RPM / 1000 RPD）是 Google 提供给开发者的免费福利，已经非常慷慨。AI Pro 订阅不会在此基础上产生叠加效应。
