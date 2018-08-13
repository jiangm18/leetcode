class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        INVALID = 0
        SPACE = 1
        SIGN = 2
        DIGIT = 3
        DOT = 4
        EX = 5
        transitionMatrix = [[-1,  0,  3,  1,  2, -1],
                            [-1,  8, -1,  1,  4,  5],
                            [-1, -1, -1,  4, -1, -1],
                            [-1, -1, -1,  1,  2, -1],
                            [-1,  8, -1,  4, -1,  5],
                            [-1, -1,  6,  7, -1, -1],
                            [-1, -1, -1,  7, -1, -1],
                            [-1,  8, -1,  7, -1, -1],
                            [-1,  8, -1, -1, -1, -1]]
        state = 0
        inputType = 0
        for e in s:
            if e == ' ':
                inputType = 1
            elif e == '+' or e == '-':
                inputType = 2
            elif e.isdigit():
                inputType = 3
            elif e == '.':
                inputType = 4
            elif e == 'E' or e == 'e':
                inputType = 5
            else:
                inputType = 0
            state = transitionMatrix[state][inputType]
            if state == -1:
                return False
            
        if state == 1 or state == 4 or state == 7 or state == 8:
            return True
        else:
            return False
sol = Solution()
print sol.isNumber("7j1")
