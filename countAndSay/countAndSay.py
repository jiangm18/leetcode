class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        res = ""
        count = 1
        strc = self.countAndSay(n-1) + '*'
        for i in range(len(strc)-1):
            if strc[i] == strc[i+1]:
                count = count + 1
            else:
                res = res + str(count) + strc[i]
                count = 1
        return res
sol = Solution()
print(sol.countAndSay(4))
