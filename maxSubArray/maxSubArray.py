class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0
        local = nums[0]
        globe = nums[0]
        for i in range(1,len(nums)):
            local = max(nums[i], nums[i] + local)
            globe = max(local, globe)
        return globe
sol = Solution()
print sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
