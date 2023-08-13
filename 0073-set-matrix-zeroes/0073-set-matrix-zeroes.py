class Solution(object):
    def setZeroes(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        zero_positions = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_positions.append((i, j))
        for i, j in zero_positions:
            for a in range(m):
                matrix[a][j] = 0
            for b in range(n):
                matrix[i][b] = 0
        
        return matrix