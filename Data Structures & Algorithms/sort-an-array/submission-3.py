class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        else:
            mid = len(nums) // 2
            left = self.sortArray(nums[:mid])
            right = self.sortArray(nums[mid:])
            return self.mergeArray(left, right)

    def mergeArray(self, left, right):
        sorted_array = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
        if i < len(left):
            sorted_array.extend(left[i:])
        if j < len(right):
            sorted_array.extend(right[j:])

        return sorted_array