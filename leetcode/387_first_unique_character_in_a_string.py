from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        o = OrderedDict()
        for i in s:
            if i in o:
                o[i]+=1
            else:
                o[i] = 1
        for key, val in o.items():
            if val == 1:
                return s.find(key)
        return -1
        

assert Solution().firstUniqChar(s="aabb") == -1
