class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(heights) - 1
        result = 0

        while right_pointer > left_pointer:
            if (right_pointer - left_pointer) * min(heights[right_pointer], heights[left_pointer]) > result:
                result = (right_pointer - left_pointer) * min(heights[right_pointer], heights[left_pointer])
            
            if heights[left_pointer] > heights[right_pointer]:
                right_pointer -= 1
            else:
                left_pointer += 1

        return result