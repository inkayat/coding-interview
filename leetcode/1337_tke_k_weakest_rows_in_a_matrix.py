from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = sorted(list(enumerate(mat)), key=lambda x:sum(x[1]))
        return [arr[i][0] for i in range(k)]
