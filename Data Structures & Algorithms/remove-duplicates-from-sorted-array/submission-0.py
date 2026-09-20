class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 1

        for i in range(len(nums)):
            if fast > (len(nums) - 1):
                return len(nums)
            if nums[slow] == nums[fast]:
                nums.pop(fast)
                continue

            slow = fast
            fast = slow + 1
    
