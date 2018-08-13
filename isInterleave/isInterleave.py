class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        else:
            dp = []
            len1 = len(s1)
            len2 = len(s2)
            for i in range(len1+1):
                dp.append([])
                for j in range(len2+1):
                    dp[i].append(False)
            dp[0][0] = True
            for i in range(1, len2+1):
                if dp[0][i-1] == True and s3[i-1] == s2[i-1]:
                    dp[0][i] = True
            for i in range(1, len1+1):
                if dp[i-1][0] == True and s3[i-1] == s1[i-1]:
                    dp[i][0] = True
        
            for i in range(1,len1+1):
                for j in range(1,len2+1):
                    if (dp[i-1][j] == True and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] == True and s2[j-1] == s3[i+j-1]):
                        dp[i][j] = True
            print dp
            return dp[len1][len2]
sol = Solution()
sol.isInterleave("db","b","cbb")
[True,False,
 False,False,
 True,True]
