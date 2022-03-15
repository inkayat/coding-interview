class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0 , len(s)-1
        while j>i:
            if s[i].isalnum() == False or s[j].isalnum() == False:
                while i<j and s[i].isalnum() == False:
                    i+=1
                while j>i and s[j].isalnum() == False:
                    j-=1

            else:
                if s[i].lower() != s[j].lower():
                    return False
                i+=1
                j-=1
        return True


assert Solution().isPalindrome(s = "A man, a plan, a canal: Panama") == True 
assert Solution().isPalindrome(s="racee a car") == False 
assert Solution().isPalindrome(s=" ") == True
print("All tests passed successfully!")
