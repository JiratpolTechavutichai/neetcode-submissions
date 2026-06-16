class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #nlogn time complexity
        nums.sort()
        num_map = defaultdict(int)
        result = []
        for num in nums:
            num_map[num] += 1
        for i in range(len(nums)):
            num_map[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, len(nums)):
                num_map[nums[j]] -= 1
                if j >= i+2 and nums[j] == nums[j-1]:
                    continue
                target = -(nums[i] + nums[j])
                if num_map[target] > 0:
                    result.append([nums[i], nums[j], -(nums[i] + nums[j])])
            for j in range(i+1, len(nums)):
                num_map[nums[j]] += 1
        return result


        
       # -4, -1, -1, 0, 1, 2

       # c = -(a+b)