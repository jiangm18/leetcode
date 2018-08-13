import copy
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        out = []
        if nums == None or len(nums) == 0:
            return res
        nums.sort()
        self.getSubset(nums, 0, out, res)
        return res
    def getSubset(self, nums, pos, out, res):
        tmp = copy.deepcopy(out)
        res.append(tmp)
        i = pos
        while(i < len(nums)):
            out.append(nums[i])
            self.getSubset(nums, i+1, out, res)
            out.pop()
            while(i<len(nums)-1 and nums[i] == nums[i+1]):
                i = i + 1
            i = i + 1
sol = Solution()
print sol.subsetsWithDup([1,2,2])
