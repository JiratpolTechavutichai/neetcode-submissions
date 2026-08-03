class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            if num not in hash_map.keys():
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        
        for key in hash_map.keys():
            if hash_map[key] > len(nums) // 2:
                return key