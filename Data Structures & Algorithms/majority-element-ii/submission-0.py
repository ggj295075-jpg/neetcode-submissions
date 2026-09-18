from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter()
        counts = Counter(nums)
        res = []

        for i in counts:
            if counts[i] > (len(nums)//3):
                res.append(i)
        return res