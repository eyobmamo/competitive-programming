class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for x in range(len(nums)):
            for y in range(len(nums)):
                if nums[y]>nums[x]:
                    nums[y],nums[x]=nums[x],nums[y]
