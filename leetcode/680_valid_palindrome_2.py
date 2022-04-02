
class Solution:
    def validPalindrome(self, s: str) -> bool:
        x, y = 0, len(s)-1
        while x<y:
            if s[x] == s[y]:
                x+=1
                y-=1
            else:
                if s[x+1]==s[y] and s[y-1]==s[x]:
                    return (s[x+1:y+1]==s[x+1:y+1][::-1] or s[x:y]==s[x:y][::-1])
                elif s[x+1] == s[y]:
                    return s[x+1:y+1]==s[x+1:y+1][::-1]
                elif s[y-1] == s[x]:
                    return s[x:y]==s[x:y][::-1]
                else:
                    return False
        return True
                
