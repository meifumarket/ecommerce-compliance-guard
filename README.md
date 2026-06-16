# 🛡️ Ecommerce Compliance Guard / 电商合规防火墙

**English: Protect your store from Google SEO penalties and platform bans.**
**中文：保护您的店铺免受 Google SEO 降权和平台封禁。**

---

## 🚀 Why you need this? / 为什么需要此工具？

**English:**
When using AI (like GPT or DeepSeek) to generate product descriptions, the AI often uses "power words" that are actually **forbidden** in e-commerce compliance:
- ❌ "Cure" $\rightarrow$ 🚩 **High Risk** (Medical claim)
- ❌ "Guaranteed" $\rightarrow$ 🚩 **Medium Risk** (Exaggerated promise)
- ❌ "Miracle" $\rightarrow$ 🚩 **High Risk** (Spammy/Fake)

**中文：**
在使用 AI（如 GPT 或 DeepSeek）生成产品描述时，AI 经常会使用一些在电商合规中**被禁用**的“强力词汇”：
- ❌ "Cure" (治愈) $\rightarrow$ 🚩 **高风险** (医疗声明)
- ❌ "Guaranteed" (保证) $\rightarrow$ 🚩 **中风险** (夸大承诺)
- ❌ "Miracle" (奇迹) $\rightarrow$ 🚩 **高风险** (垃圾内容/虚假宣传)

**This tool acts as a "Compliance Firewall" between your AI and your Store.**
**本工具在您的 AI 生成内容与店铺之间充当“合规防火墙”。**

---

## ✨ Key Features / 核心特性

- **Multi-Level Filtering / 分级过滤**: 
  - `Absolute Ban` (绝对禁用): Global replacements for the most dangerous words. / 全局替换最危险的词汇。
  - `Category-Specific` (品类专用): Specialized rules for Medical, Skincare, and Beauty products. / 针对医疗、护肤和美容类产品的专项规则。
- **Smart Softening / 智能软化**: Instead of just deleting words (which kills SEO), it replaces them with compliant alternatives (e.g., `Cure` $\rightarrow$ `Support`). / 不再简单地删除词汇（这会破坏 SEO），而是将其替换为合规的替代词（例如：`Cure` $\rightarrow$ `Support`）。
- **Force-Retain Mechanism / 强制保留机制**: Ensures critical industry terms (e.g., "TCM", "Acne") are preserved to maintain search traffic. / 确保核心行业术语（如“中医”、“痤疮”）得以保留，以维持搜索流量。
- **Risk Scoring / 风险评分**: Quantifies the compliance risk of any text from `0.0` (Safe) to `1.0` (Dangerous). / 将文本的合规风险量化为 `0.0`（安全）到 `1.0`（危险）的分数。

## 🛠️ Quick Start / 快速上手

```python
from compliance_guard import ComplianceGuard

# Initialize for a specific category / 为特定品类初始化
guard = ComplianceGuard(category="skincare")

text = "This miracle cream will cure your acne forever!"
cleaned_text, logs = guard.clean_text(text)

print(cleaned_text) 
# Output: "This advanced cream will support your acne lasting!"
```

## 💼 Business Value / 商业价值

**English:**
For agencies and freelance developers, integrating this guard into your automation pipeline means:
1. **Zero Bans**: Protect your clients' stores from being flagged as "Medical/Pharmacy" without a license.
2. **Higher Trust**: Professional, understated language increases customer conversion rates (CVR).
3. **Scalable Safety**: Process 10,000+ product descriptions with a consistent safety standard.

**中文：**
对于代理商和自由职业开发者，将此防火墙集成到自动化流水线中意味着：
1. **零封禁**：防止客户的店铺在没有许可证的情况下被标记为“医疗/药店”。
2. **更高信任度**：专业、克制的语言描述能提升客户转化率 (CVR)。
3. **可扩展的安全**：以统一的安全标准处理 10,000+ 条产品描述。

---
*Designed for high-volume Shopify and Amazon automation pipelines.*
*专为高频 Shopify 和 Amazon 自动化流水线设计。*
