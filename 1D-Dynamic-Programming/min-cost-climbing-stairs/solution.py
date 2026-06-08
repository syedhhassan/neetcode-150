class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)

        n = len(cost)
        one, two = cost[0], cost[1]
        for i in range(2, n):
            one, two = two, cost[i] + min(one, two)
        
        return min(one, two)