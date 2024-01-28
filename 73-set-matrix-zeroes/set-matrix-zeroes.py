class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])

        zero_row = set()
        zero_col = set()

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)
        
        for i in zero_row:
            matrix[i] = [0] * col

        for j in zero_col:
            for i in range(row):
                matrix[i][j] = 0

        return matrix 
 