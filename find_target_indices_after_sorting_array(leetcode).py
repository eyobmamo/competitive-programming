class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l=len(nums)
        n=nums.sort()
        
        T=[]

        for x in range(l):
            if nums[x]==target:
                T.append(x)
        return T        
