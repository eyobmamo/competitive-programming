class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result=[]
        output=[]
        result_min_index=[]
        for x in range(len(points)):
            R=math.sqrt(((points[x][0])**2)+((points[x][1])**2))
            result.append(R)
    
        for x in range(k):
            M=min(result)
            Max=max(result)
            index_max=result.index(Max)
            L=result.index(M)
            result_min_index.append(L)
            result[L]+=result[index_max]
        print(result)  
        for x in range(len(result_min_index)):
            output.append(points[result_min_index[x]])
    
        return output  

        
