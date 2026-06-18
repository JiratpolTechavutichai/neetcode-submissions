class Solution:
    def findMin(self, nums: List[int]) -> int:
        minval = nums[0]
        for num in nums:
            if num < minval:
                minval = num
        return minval
        