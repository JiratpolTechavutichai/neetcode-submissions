from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_nums = defaultdict(int)
        for num in nums:
            map_nums[num] += 1

        # Sort the dictionary items by the count (x[1]) in descending order
        sorted_items = sorted(map_nums.items(), key=lambda x: x[1], reverse=True)
        
        # Extract the first k keys
        result = [item[0] for item in sorted_items[:k]]
        
        return result