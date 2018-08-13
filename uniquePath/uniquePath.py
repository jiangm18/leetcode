class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [0]
        if m == 1 or n == 1:
            return 1
        self.searchWay(1, 1, m, n, res)
        return res[0]
        
    def searchWay(self, row, col, m, n, res):
        if row == m and col == n:
            res[0] = res[0] + 1
            return
        if row == m and col < n:
            self.searchWay(row, col + 1, m, n, res)
            return
        if row < m and col == n:
            self.searchWay(row+1, col, m, n, res)
            return
        else:
            self.searchWay(row, col + 1, m, n, res)
            self.searchWay(row+1, col, m, n, res)
sol = Solution()
print sol.uniquePaths(2,2)
