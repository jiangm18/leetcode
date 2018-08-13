def largestRectangleArea(height):
    res = 0
    stack = []
    height.append(0)
    n = len(height)
    for i in range(n):
        if not stack or height[i] >= height[stack[-1]]:
            stack.append(i)
        else:
            while(stack and height[i] < height[stack[-1]]):
                index = stack[-1]
                stack.pop()
                if not stack:
                    width = i
                else:
                    width = i - 1 - stack[-1]
                res = max(res, height[index]*width)
            stack.append(i)
    return res

print largestRectangleArea([1,2,3,4,5,6,7])
                
