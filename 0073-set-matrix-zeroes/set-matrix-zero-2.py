class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        def setzero(a, b, matrix):
            for i in range(m):
                matrix[i][b] = 0
            for j in range(n):
                matrix[a][j] = 0

        zero_positions = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_positions.append((i, j))
        for i, j in zero_positions:
            setzero(i, j, matrix)

        return matrix
