class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for layer in range(n/2):
            for i in range(layer, n-layer-1):
                tmp = matrix[layer][i]
                matrix[layer][i] = matrix[n-1-i][layer]
                matrix[n-1-i][layer] = matrix[n-1-layer][n-1-i]
                matrix[n-1-layer][n-1-i] = matrix[i][n-1-layer]
                matrix[i][n-1-layer] = tmp
        return matrix
sol = Solution()
print sol.rotate([[1,2,3],[4,5,6],[7,8,9]])
