# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int, start=1) -> int:
        if n-start<=1:
            if isBadVersion(start):
                return start
            return n
        mid = (start+n)//2
        if isBadVersion(mid) == False:
            return self.firstBadVersion(n, mid+1)
        return self.firstBadVersion(mid, start)


