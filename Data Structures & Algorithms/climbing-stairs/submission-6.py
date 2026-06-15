class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        else:
            old = 2
            new = 3
            for _ in range(n-3):
                old, new = new, old + new
            return new
