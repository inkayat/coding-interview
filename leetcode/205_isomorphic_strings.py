from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        imap = {}
        isMapped = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in imap:
                if t[i] in isMapped:
                    return False
                else:
                    imap[s[i]] = t[i]
                    isMapped[t[i]] = s[i]
            else:
                if t[i] != imap[s[i]]:
                    return False
        return True 
        
        
        
