class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if matrix == None or len(matrix) == 0:
            return res
        m = len(matrix)
        n = len(matrix[0])
        layerNum = (min(m, n) + 1)/2
        for layer in range(layerNum):
            lastRow = m - 1 - layer
            lastCol = n - 1 - layer
            if lastCol == layer:
                for j in range(layer, lastRow + 1):
                    res.append(matrix[j][layer])
            else:
                if lastRow == layer:
                    for j in range(layer, lastCol+1):
                        res.append(matrix[layer][j])
                else:
                    for i in range(layer, n-1-layer):
                        res.append(matrix[layer][i])
                    for i in range(layer, m-1-layer):
                        res.append(matrix[i][n-1-layer])
                    for i in range(layer, n-1-layer):
                        res.append(matrix[m-1-layer][n-1-i])
                    for i in range(layer, m-1-layer):
                        res.append(matrix[m-1-i][layer])
        
        return res
sol = Solution()
print sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
