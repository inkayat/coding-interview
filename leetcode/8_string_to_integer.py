class Solution:
    def myAtoi(self, s: str) -> int:
        #ignore leading space
        s = s.strip()
        ss = ""
        for i in range(len(s)):
            if s[i].isdigit() == False and i!=0:
                break
            ss+=s[i]
        try:
            if int(ss)<-(1<<31):
                return -(1<<31)
            elif int(ss)>(1<<31)-1:
                return (1<<31)-1
            return int(ss)
        except:
            return 0


if __name__ == "__main__":
    sol = Solution().myAtoi
    assert sol("91283472332") == 2147483647
    assert sol(".1") == 0
    assert sol("42") == 42 
    assert sol("    -42") == -42
    assert sol("4193 with words") == 4193 

    print("All test passed successfully!")
