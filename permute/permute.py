import copy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        out = []
        visited = []
        for i in range(len(nums)):
            visited.append(0)
        if nums == None or len(nums) == 0:
            return res
        self.permuteDFS(nums, visited, 0, out, res)
        return res
        
    def permuteDFS(self, nums, visited, level, out, res):
        if level == len(nums):
            tmp = copy.deepcopy(out)
            res.append(tmp)
        else:
            for i in range(len(nums)):
                if visited[i] == 0:
                    out.append(nums[i])
                    visited[i] = 1
                    self.permuteDFS(nums, visited, level + 1, out, res)
                    out.pop()
                    visited[i] = 0

sol = Solution()
print(sol.permute([1,2,3]))
