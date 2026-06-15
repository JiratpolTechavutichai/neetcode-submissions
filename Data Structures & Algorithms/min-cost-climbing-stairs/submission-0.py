class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        distance_map = {}
        distance_map[len(cost) - 1] = cost[len(cost) - 1]
        distance_map[len(cost) - 2] = cost[len(cost) - 2]

        for i in range(len(cost) - 3, -1, -1):
            distance_map[i] = cost[i] + min(distance_map[i+1], distance_map[i+2])

        return min(distance_map[0], distance_map[1])


