class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        reach = 0
        lastreach = 0
        pos = 0
        steps = 0
        while(pos<=reach and pos < len(nums)):
            print reach,lastreach,pos
            if pos > lastreach:
                steps = steps + 1
                lastreach = reach
            reach = max(reach, pos + nums[pos])
            pos = pos + 1
        return steps
sol = Solution()
print(sol.jump([2,3,1,1,4]))
