class Solution:
    def maxScore(self, s: str) -> int:
        cnt_one=s.count("1")
        max1=cnt_one
        max0=0
        res=0
        for c in s[:len(s)-1]:
            if c == "1":
                max1-=1
            else:
                max0+=1
            res=max(res,max0+max1)
        return res        
        