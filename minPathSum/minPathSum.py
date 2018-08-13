class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            res.append([])
            for j in range(n):
                res[i].append(0)
        print res
        print grid
        res[0][0] = grid[0][0]
        for i in range(1, m):
            res[i][0] = res[i-1][0] + grid[i][0]
        for i in range(1, n):
            res[0][i] = res[0][i-1] + grid[0][i]
        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = min(res[i-1][j], res[i][j-1]) + grid[i][j]
        return res[m-1][n-1]
sol = Solution()
print sol.minPathSum([[0]])
