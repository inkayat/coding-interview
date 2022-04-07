class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        arr = text.split()
        res = []
        i=0
        while i < len(arr)-2:
            if arr[i]==first and arr[i+1]==second:
                res.append(arr[i+2])
            i+=1
        return res
            
        
