from collections import Counter, defaultdict
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = defaultdict(lambda:0)
        cp = Counter(p)
        start = 0
        res = []
        i = 0
        while i <len(s):
            if s[i] in cp and d[s[i]]<cp[s[i]]:
                d[s[i]]+=1
                if d == cp:
                    res.append(start)
                    d[s[start]]-=1
                    start+=1
            elif s[i] in cp and d[s[i]] == cp[s[i]]:
                while start<i and s[start] != s[i]:
                    d[s[start]]-=1
                    start+=1
                start+=1
            else:
                start=i+1
                d = defaultdict(lambda:0)
            i+=1
        return res
                
                               

if __name__ == "__main__":
    sol = Solution().findAnagrams 
    assert sol(s="cbaebabacd", p = "abc") == [0,6]
    assert sol(s="abab", p="ab") == [0,1,2]
    assert sol(s="abaacbabc", p="abc") == [3,4,6]
    print("All tests passed successfully!")
