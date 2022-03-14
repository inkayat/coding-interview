from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc = Counter(magazine)
        mc = Counter(ransomNote)
        for key, val in mc.items():
            if key not in rc or rc[key]<val:
                return False
        return True
        
