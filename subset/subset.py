import copy
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        out = []
        if nums == None or len(nums) == 0:
            return res
        self.helper(nums, 0, out, res)
        return res
    def helper(self, nums, pos, out, res):
        tmp = copy.deepcopy(out)
        res.append(tmp)
        for i in range(pos, len(nums)):
            out.append(nums[i])
            self.helper(nums, i+1, out, res)
            out.pop()
sol = Solution()
print sol.subsets([1,3,2,4])
