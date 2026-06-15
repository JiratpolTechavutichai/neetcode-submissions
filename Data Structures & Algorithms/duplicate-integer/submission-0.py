class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        a = Counter(nums)
        for b in a.keys():
            if a[b] > 1:
                return True
        else:
            return False
        