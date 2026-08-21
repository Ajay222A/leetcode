class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range (len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i],nums[i+1] = nums[i+1]*2,0
        for i in range (len(nums)-1):
            if nums[i]==0:
                nums.remove(nums[i])
                nums.append(0)
            for j in range(i+1,len(nums),-1):
                if nums[j]==0:
                    nums.remove(nums[j])
                    nums.append(0)
        return nums
        