class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or len(s) == 0 or len(s) == 1:
            return 0
        i = 0
        count = 0
        maxcount = 0
        while(i<len(s)):
            while i <= len(s)-2 and s[i] == '(' and s[i+1] == ')':
                count = count + 2
                i = i + 2
            maxcount = max(maxcount, count)
            count = 0
            i = i + 1
        return maxcount
    def isValid(self, s):
        temp = []
        for e in s:
            if e == '(' or e == '[' or e == '{':
                temp.append(e)
            else:
                if e == ')':
                    if len(temp) == 0 or temp[len(temp)-1] != '(':
                        return False
                    else:
                        temp.pop()
                if e == ']':
                    if len(temp) == 0 or temp[len(temp)-1] != '[':
                        return False
                    else:
                        temp.pop()
                if e == '}':
                    if len(temp) == 0 or temp[len(temp)-1] != '{':
                        return False
                    else:
                        temp.pop()
        if len(temp) == 0:
            return True
        else:
            return False
sol = Solution()
print(sol.longestValidParentheses("()(()"))
