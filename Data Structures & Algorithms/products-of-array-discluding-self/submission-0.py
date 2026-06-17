class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        product_nonzero = 1
        count_zero = 0
        result = []
        for num in nums:
            product *= num
            if num == 0:
                count_zero += 1
            if num != 0:
                product_nonzero *= num

        if product == 0:
            if count_zero >= 2:
                return [0] * len(nums)
            else:
                for num in nums:
                    if num != 0:
                        result.append(0)
                    else:
                        result.append(product_nonzero)
                return result


        for num in nums:
            result.append(product // num)
        return result
        