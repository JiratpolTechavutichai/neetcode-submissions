class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result  = [0] * len(nums)
        index = 0
        for num in nums:
            if num != val:
                result[index] += num
                index += 1
        for i in range(index):
            nums[i] = result[i]
        return index
        