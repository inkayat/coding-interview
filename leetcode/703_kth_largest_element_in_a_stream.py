import bisect

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = list(sorted(nums))
        self.k = k

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)
        return self.nums[len(self.nums)-self.k]
