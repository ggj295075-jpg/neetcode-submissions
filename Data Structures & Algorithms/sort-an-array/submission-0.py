class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        new_nums = []
        for i in range(len(nums)):
            new_nums.append(nums.pop(nums.index(min(nums))))
        return new_nums