class Solution:
    def reverseVowels(self, s: str) -> str:
        i,j = 0, len(s)-1
        vowels = {'a':1,'e':1,'i':1,'u':1,'o':1}
        left, right = "",""
        while i<=j:
            if i==j:
                left+=s[i]
                i+=1
            elif s[i].lower() in vowels and s[j].lower() in vowels:
                left+=s[j]
                right+=s[i]
                i+=1
                j-=1
            elif s[i].lower() in vowels:
                while i<j and s[j].lower() not in vowels:
                    right+=s[j]
                    j-=1
            elif s[j].lower() in vowels:
                while i<j and s[i].lower() not in vowels:
                    left+=s[i]
                    i+=1
            else:
                left+=s[i]
                right+=s[j]
                i+=1
                j-=1
        return left+right[::-1] 
