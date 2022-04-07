import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = list(map(lambda x:-x, stones))        
        heapq.heapify(arr)
        while len(arr)>1:
            x = heapq.heappop(arr)
            y = heapq.heappop(arr)
            if x != y:
                x = x-y
                heapq.heappush(arr, x)
        res = 0
        if len(arr)==1:
            res = -heapq.heappop(arr)
        return res
        
