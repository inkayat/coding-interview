class Solution:
    def twoCitySchedCost(self, costs) -> int:
        arr = list(sorted(costs, key=lambda x: abs(x[0]-x[1])))
        a, b, res = 0,0,0
        n = len(costs)//2
        for i, j in arr[::-1]:
            if j<i:
                if b<n:
                    res+=j
                    b+=1
                else:
                    res+=i
                    a+=1
            else:
                if a<n:
                    res+=i
                    a+=1
                else:
                    res+=j
                    b+=1
        return res
                    
