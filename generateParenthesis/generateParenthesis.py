class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        if n == 0:
            return res
        self.generateParenthesisDFS(n, n, "", res)
        return res
    def generateParenthesisDFS(self, left, right, str, res):
        print str
        if left > right:
            return
        if left == 0 and right == 0:
            res.append(str)
        else:
            if (left > 0): 
                self.generateParenthesisDFS(left - 1, right, str + '(', res)
            if (right > 0):
                self.generateParenthesisDFS(left, right - 1, str + ')', res)

sol = Solution()
print(sol.generateParenthesis(3))
