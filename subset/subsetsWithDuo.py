import copy
class Solution(object):
    def subsetsWithDup(self, nums):
        res = [[]]
        if nums == None or len(nums) == 0:
            return res
        i = 0
        start = 0
        length = len(nums)
        while(i<length):
            size = len(res)
            while(start < size):
                tmp = copy.deepcopy(res[start])
                tmp.append(nums[i])
                res.append(tmp)
                start = start + 1
            if i < length-1 and nums[i] == nums[i+1]:
                start = size
            else:
                start = 0
            i = i + 1
        return res
sol = Solution()
print sol.subsetsWithDup([1,2,2])
