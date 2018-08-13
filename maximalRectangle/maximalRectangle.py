import copy
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res = 0
        if matrix == None or len(matrix) == 0:
            return res
        n = len(matrix[0])
        height = []
        for i in range(n):
            height.append(0)
        for k in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[k][j] == 0:
                    print height
                    height[j] = 0
                else:
                    height[j] = height[j] + 1
            res = max(res, self.largestRectangleArea(height))
        return res

    def largestRectangleArea(self,height):
        res = 0
        stack = []
        tmp = copy.deepcopy(height)
        tmp.append(0)
        n = len(tmp)
        for i in range(n):
            if not stack or tmp[i] >= tmp[stack[-1]]:
                stack.append(i)
            else:
                while(stack and tmp[i] < tmp[stack[-1]]):
                    index = stack[-1]
                    stack.pop()
                    if not stack:
                        width = i
                    else:
                        width = i - 1 - stack[-1]
                    res = max(res, tmp[index]*width)
                stack.append(i)
        return res
sol = Solution()
print sol.maximalRectangle([[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]])
