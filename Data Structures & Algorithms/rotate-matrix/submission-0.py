class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        num_cols = len(matrix[0])
        num_rols = len(matrix)

        # reflect the matrix
        for i in range(num_rols):
            for j in range(i, num_cols):
                temp = matrix[i][j] 
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        # reverse all rows
        for i in range(num_rols): 
            matrix[i].reverse()

        
        

        
