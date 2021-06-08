class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        col_start, col_end = 0, len(matrix[0]) - 1
        row_start, row_end = 0, len(matrix) - 1
        res = []
        
        while row_start <= row_end and col_start <= col_end:
            for j in range(col_start, col_end + 1):
                res.append(matrix[row_start][j])
            
            for i in range(row_start + 1, row_end + 1):
                res.append(matrix[i][col_end])
            
            for j in reversed(range(col_start, col_end)):
                if row_start == row_end:
                    break
                res.append(matrix[row_end][j])
                
            for i in reversed(range(row_start + 1, row_end)):
                if col_start == col_end:
                    break
                res.append(matrix[i][col_start])
                
           
            row_start += 1
            row_end -= 1
            col_start += 1
            col_end -= 1
            
        return res
                
