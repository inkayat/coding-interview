class Solution:
    def shortestPalindrome(self, s: str) -> str:
        x, y = 0, len(s)-1
        while y>=0:
            if s[x:y+1]==s[x:y+1][::-1]:
                break
            y-=1
        return s[y+1:][::-1]+s[x:y+1]+s[y+1:]


if __name__ == '__main__':
    sol = Solution().shortestPalindrome
    assert sol(s="aacecaaa") == "aaacecaaa"
    assert sol(s="abcd") == "dcbabcd"
    print("All test passed successfully!")
