class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead
        """
        ind=0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp=nums[ind]
                nums[ind]=nums[i]
                nums[i]=temp
                ind+=1