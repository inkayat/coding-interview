class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        from collections import defaultdict
        d = defaultdict(lambda:-1)
        res = set()
        for i in range(len(s)-9):
            if s[i:i+10] in d:
                res.add(s[i:i+10])
            else:
                d[s[i:i+10]] = i+9
        return list(res)
        
