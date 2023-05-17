class Solution:
    def smallerNumbersThanCurrent(self, a: List[int]) -> List[int]:
        countless=[]
        n=len(a)
        
        for x in range(n):
            c=0
            for y in range(n):
                if (a[x]>a[y]): 
                    c+=1
            countless.append(c)   
        return countless
