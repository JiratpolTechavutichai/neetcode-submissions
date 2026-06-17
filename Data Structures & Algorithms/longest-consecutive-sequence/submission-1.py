class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        nums.sort()
        temp = 1
        max_temp = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                temp += 1
            elif nums[i + 1] - nums[i] == 0:
                pass
            else:
                max_temp = max(max_temp, temp)
                temp = 1

        max_temp = max(max_temp, temp)

        return max_temp
# 0,1,1,2,3,4,5,6
        