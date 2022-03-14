class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        fs, ts = [], []
        for i in s:
            if i == '#' and len(fs) > 0:
                fs.pop()
            elif i!='#':
                fs.append(i)
        for i in t:
            if i == '#' and len(ts) > 0:
                ts.pop()
            elif i != '#':
                ts.append(i)
        return fs == ts

if __name__ == "__main__":
    sol = Solution().backspaceCompare
    assert sol(s = "ab#c", t = "ad#c") == True 
    assert sol(s = "ab##", t = "c#d#") == True
    assert sol(s = "a#c", t = "b") == False
    print("All tests passed successfully!")

