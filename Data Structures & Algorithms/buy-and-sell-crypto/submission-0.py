class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maximum = 0
        for i in range(len(prices)):
            diff = prices[i] - lowest
            if diff > maximum:
                maximum = diff
            if prices[i] < lowest:
                lowest = prices[i]
        return maximum

            

