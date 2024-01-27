class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n
        result[0]=sum(abs(nums[0]-num) for num in nums[1:])
        for i in range(1,n):
            result[i]=result[i-1]-(n-(i+1))*(nums[i]-nums[i-1])+(i-1)*(nums[i]-nums[i-1])
        return result    
        