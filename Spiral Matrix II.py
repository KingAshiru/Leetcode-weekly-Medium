class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        row_start, row_end = 0, n - 1
        col_start, col_end = 0, n - 1
        num = 0
        res = [[0]*n for _ in range(n)]
        while row_start <= row_end and col_start <= col_end:
            for j in range(col_start, col_end + 1):
                num += 1
                res[row_start][j] = num
            for i in range(row_start + 1, row_end + 1):
                num += 1
                res[i][col_end] = num
            for j in reversed(range(col_start, col_end)):
                num += 1
                res[row_end][j] = num
            for i in reversed(range(row_start + 1, row_end)):
                num += 1
                res[i][col_start] = num
            
            row_start += 1
            row_end -= 1
            col_start += 1
            col_end -= 1
        
        return res
                
