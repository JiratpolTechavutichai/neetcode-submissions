class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:

        def factorial(n: int) -> int:
            if n == 0:
                return 1
            if n == 1:
                return 1
            return n * factorial(n - 1)
    
        return int(factorial(m + n - 2) / (factorial(m -1) * factorial(n -1)))
        