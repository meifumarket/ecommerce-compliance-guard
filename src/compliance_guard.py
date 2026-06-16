
import re
import logging
from typing import Dict, Tuple, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ComplianceGuard")

class ComplianceGuard:
    """
    Ecommerce Compliance Guard
    专门用于电商领域的合规性检查与文本软化工具。
    防止 AI 生成导致 Google SEO 降权或平台封号的违规词汇。
    """
    
    def __init__(self, category: str = "general"):
        self.category = category.lower()
        
        # V43 绝对禁用词库 (所有品类通用)
        self.ABSOLUTE_BAN = {
            'cure': 'support', 'cures': 'supports', 'miracle': 'advanced', 'magic': 'effective',
            'guaranteed': 'designed to deliver', 'guarantee result': 'designed for results',
            'anti-cancer': 'wellness', 'prevent disease': 'support health',
            'burn fat': 'support fitness goals', 'fat burning': 'fitness support',
            'lose weight': 'support your wellness journey', 'weight loss': 'wellness support',
            'permanent': 'lasting', 'forever': 'long-lasting',
        }
        
        # V43 医疗/功效类专用替换 (仅在 category="medical" 或 "skincare" 时触发)
        self.MEDICAL_REPLACEMENTS = {
            'treat': 'care for', 'treats': 'cares for', 'prevent': 'help maintain',
            'prevents': 'helps maintain', 'heal': 'soothe', 'heals': 'soothes',
            'pain relief': 'comfort', 'therapeutic': 'relaxing',
            'back pain': 'back tension', 'neck pain': 'neck tension',
            'muscle recovery': 'muscle relaxation', 'remedy': 'solution',
        }

        # 强制保留词库 (避免过度拦截导致流量丢失)
        self.FORCE_RETAIN = {
            'acne', 'scar', 'wrinkle', 'brightening', 'anti-aging', 'firming', 'lifting', 'removal',
            'dredge', 'meridian', 'tcm', 'acupuncture', 'qi'
        }

    def clean_text(self, text: str) -> Tuple[str, List[str]]:
        """
        对文本进行合规化处理
        Returns: (cleaned_text, replaced_logs)
        """
        if not text: return "", []
        
        cleaned = text
        replaced_logs = []

        # 1. 执行绝对禁用词替换 (Case-Insensitive)
        for banned, replacement in self.ABSOLUTE_BAN.items():
            pattern = re.compile(re.escape(banned), re.IGNORECASE)
            if pattern.search(cleaned):
                cleaned = pattern.sub(replacement, cleaned)
                replaced_logs.append(f"Replaced '{banned}' -> '{replacement}'")

        # 2. 如果是医疗/护肤品类，执行专项替换
        if self.category in ["medical", "skincare", "beauty"]:
            for medical, replacement in self.MEDICAL_REPLACEMENTS.items():
                # 检查是否在强制保留词库中
                if any(retain in medical.lower() for retain in self.FORCE_RETAIN):
                    continue
                    
                pattern = re.compile(re.escape(medical), re.IGNORECASE)
                if pattern.search(cleaned):
                    cleaned = pattern.sub(replacement, cleaned)
                    replaced_logs.append(f"Medical-specific replacement: '{medical}' -> '{replacement}'")

        return cleaned, replaced_logs

    def get_risk_score(self, text: str) -> float:
        """
        评估文本的合规风险分 (0.0 - 1.0)
        1.0 代表极高风险 (包含大量绝对禁用词)
        """
        if not text: return 0.0
        
        hits = 0
        total_words = len(text.split())
        
        for banned in self.ABSOLUTE_BAN.keys():
            if re.search(re.escape(banned), text, re.IGNORECASE):
                hits += 1
        
        score = hits / (total_words / 10 + 1) # 简单的加权评分
        return min(score, 1.0)

if __name__ == "__main__":
    # 测试用例
    guard = ComplianceGuard(category="medical")
    test_text = "This miracle cream will cure your acne and remove scars forever. Guaranteed result!"
    
    print(f"Original: {test_text}")
    cleaned, logs = guard.clean_text(test_text)
    print(f"Cleaned: {cleaned}")
    print(f"Logs: {logs}")
    print(f"Risk Score: {guard.get_risk_score(test_text):.2f}")
