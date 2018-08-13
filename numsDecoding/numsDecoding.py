class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or len(s) == 0 or s[0] == '0':
            return 0
        dp = []
        length = len(s)
        for i in range(length+1):
            dp.append(0)
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        for i in range(2, length+1):
            if s[i-1] == '0':
                if s[i-2] == '1' or s[i-2] == '2':
                    dp[i] = dp[i-2]
                else:
                    dp[i] = 0
            else:
                if (s[i-2] >= '3') or (s[i-2] == '2' and s[i-1] >= '7'):
                    dp[i] = dp[i-1]
                else:
                    if s[i-2] == '0':
                        dp[i] = dp[i-1]
                    else:
                        dp[i] = dp[i-1] + dp[i-2]
        return dp[length]
                
                    
                
sol = Solution()
print sol.numDecodings("2606")


