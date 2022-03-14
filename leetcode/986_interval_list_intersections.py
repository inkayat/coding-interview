from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        f, s = 0, 0
        output = []
        while f<len(firstList) and s<len(secondList):
            if firstList[f][0]>secondList[s][-1]:
                s+=1 
            elif secondList[s][0]>firstList[f][-1]:
                f+=1 
            else:
                if firstList[f][0]==secondList[s][0] and secondList[s][-1]==firstList[f][-1]:
                    output.append([firstList[f][0],firstList[f][-1]])
                    f+=1 
                    s+=1 
                elif firstList[f][0]>=secondList[s][0] and firstList[f][-1]<=secondList[s][-1]:
                    output.append([firstList[f][0], firstList[f][-1]])
                    secondList[s][0]=firstList[f][-1]+1
                    f+=1
                elif firstList[f][0]>=secondList[s][0] and firstList[f][-1]>=secondList[s][-1]:
                    output.append([firstList[f][0], secondList[s][-1]])
                    firstList[f][0] = secondList[s][-1]+1 
                    s+=1
                elif firstList[f][0]<=secondList[s][0] and firstList[f][-1]<=secondList[s][-1]:
                    output.append([secondList[s][0], firstList[f][-1]])
                    secondList[s][0]=firstList[f][-1]+1 
                    f+=1
                elif firstList[f][0]<=secondList[s][0] and firstList[f][-1]>=secondList[s][-1]:
                    output.append([secondList[s][0], secondList[s][-1]])
                    firstList[f][0] = secondList[s][-1]+1
                    s+=1
        return output
        

if __name__ == "__main__":
    assert Solution().intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]) == [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    assert Solution().intervalIntersection(firstList = [[1,3],[5,9]], secondList = []) == []
    print("All tests passed successfully!")
