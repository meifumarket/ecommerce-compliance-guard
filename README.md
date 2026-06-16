
# 🛡️ Ecommerce Compliance Guard

**Protect your store from Google SEO penalties and platform bans.**

The `Ecommerce Compliance Guard` is a professional-grade text sanitization tool designed for e-commerce sellers. It automatically detects and "softens" high-risk medical claims, exaggerated promises, and banned keywords that often trigger AI-generated content flags or legal risks on platforms like Shopify, Amazon, and Google Shopping.

## 🚀 Why you need this?

When using AI (like GPT or DeepSeek) to generate product descriptions, the AI often uses "power words" that are actually **forbidden** in e-commerce compliance:
- ❌ "Cure" $\rightarrow$ 🚩 **High Risk** (Medical claim)
- ❌ "Guaranteed" $\rightarrow$ 🚩 **Medium Risk** (Exaggerated promise)
- ❌ "Miracle" $\rightarrow$ 🚩 **High Risk** (Spammy/Fake)

**This tool acts as a "Compliance Firewall" between your AI and your Store.**

## ✨ Key Features

- **Multi-Level Filtering**: 
  - `Absolute Ban`: Global replacements for the most dangerous words.
  - `Category-Specific`: Specialized rules for Medical, Skincare, and Beauty products.
- **Smart Softening**: Instead of just deleting words (which kills SEO), it replaces them with compliant alternatives (e.g., `Cure` $\rightarrow$ `Support`).
- **Force-Retain Mechanism**: Ensures critical industry terms (e.g., "TCM", "Acne") are preserved to maintain search traffic.
- **Risk Scoring**: Quantifies the compliance risk of any text from `0.0` (Safe) to `1.0` (Dangerous).

## 🛠️ Quick Start

```python
from compliance_guard import ComplianceGuard

# Initialize for a specific category
guard = ComplianceGuard(category="skincare")

text = "This miracle cream will cure your acne forever!"
cleaned_text, logs = guard.clean_text(text)

print(cleaned_text) 
# Output: "This advanced cream will support your acne lasting!"
```

## 💼 Business Value

For agencies and freelance developers, integrating this guard into your automation pipeline means:
1. **Zero Bans**: Protect your clients' stores from being flagged as "Medical/Pharmacy" without a license.
2. **Higher Trust**: Professional, understated language increases customer conversion rates (CVR).
3. **Scalable Safety**: Process 10,000+ product descriptions with a consistent safety standard.

---
*Designed for high-volume Shopify and Amazon automation pipelines.*
