class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # prefix_x[i][j] = count of 'X' in submatrix from (0,0) to (i,j)
        # prefix_y[i][j] = count of 'Y' in submatrix from (0,0) to (i,j)
        prefix_x = [[0] * (n + 1) for _ in range(m + 1)]
        prefix_y = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                x_count = 1 if grid[i][j] == 'X' else 0
                y_count = 1 if grid[i][j] == 'Y' else 0
                
                prefix_x[i + 1][j + 1] = prefix_x[i][j + 1] + prefix_x[i + 1][j] - prefix_x[i][j] + x_count
                prefix_y[i + 1][j + 1] = prefix_y[i][j + 1] + prefix_y[i + 1][j] - prefix_y[i][j] + y_count
        
        count = 0
        for i in range(m):
            for j in range(n):
                # Count submatrices starting at (0,0) and ending at (i,j)
                x = prefix_x[i + 1][j + 1]
                y = prefix_y[i + 1][j + 1]
                if x == y and x > 0:
                    count += 1
        
        return count