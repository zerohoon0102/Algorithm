class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j = 0, 0
        min_m, max_m = 1, len(matrix)
        min_n, max_n = 0, len(matrix[0])
        ver = [0,1,0,-1]
        hor = [1,0,-1,0]
        direc = 0
        result = [matrix[0][0]]
        
        while 1:
            nxt_i, nxt_j = i+ver[direc], j+hor[direc]
            if (i == nxt_i or min_m <= nxt_i < max_m) and (j == nxt_j or min_n <= nxt_j < max_n):
                i, j = nxt_i, nxt_j
                result.append(matrix[i][j])
            else:
                if hor[direc] > 0:
                    max_n -= 1
                elif hor[direc] < 0:
                    min_n += 1
                elif ver[direc] > 0:
                    max_m -= 1
                elif ver[direc] < 0:
                    min_m += 1
                direc = (direc+1)%4
            if len(result) == len(matrix)*len(matrix[0]):
                return result
