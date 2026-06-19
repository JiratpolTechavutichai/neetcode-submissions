class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        mark = [[matrix[r][c] for c in range(num_cols)] for 
        r in range(num_rows)]

        for r in range(num_rows):
            for c in range(num_cols):
                if matrix[r][c] == 0:
                    for i in range(num_cols):
                        mark[r][i] = 0
                    for i in range(num_rows):
                        mark[i][c] = 0

        for r in range(num_rows):
            for c in range(num_cols):
                matrix[r][c] = mark[r][c]

        



        
        