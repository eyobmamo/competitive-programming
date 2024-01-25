class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lng =  len(nums)
        val_c = nums.count(val)
        for left in range(lng - val_c):
            if nums[left] == val:
                right = left
                while nums[right] == val:
                    right += 1   
                nums[left], nums[right] = nums[right], nums[left]
        return lng - val_c
        