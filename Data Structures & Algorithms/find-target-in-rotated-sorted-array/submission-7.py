from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] == target:
                return middle
            
            # Condition 1: Left half is normally sorted
            if nums[left] <= nums[middle]:
                # Check if the target lies within this sorted left half
                if nums[left] <= target < nums[middle]:
                    right = middle - 1  # Search left
                else:
                    left = middle + 1   # Search right
                    
            # Condition 2: Right half must be normally sorted
            else:
                # Check if the target lies within this sorted right half
                if nums[middle] < target <= nums[right]:
                    left = middle + 1   # Search right
                else:
                    right = middle - 1  # Search left
                    
        return -1