class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        if not (1 in nums):
            return 1
        for i in range(1, len(nums)):
            if nums[i-1] < 1:
                continue
            if (nums[i] - nums[i-1]) > 1:
                return nums[i-1]+1
        return nums[-1] + 1