class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

if __name__ == "__main__":
    sol = Solution().strStr 
    assert sol(haystack="hello", needle="ll") == 2
    assert sol(haystack="aaaaa", needle="bba") == -1
    assert sol(haystack="", needle="") == 0
    print("All tests passed successfully!")

