class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 1
        for i in range(len(nums)):
            while(nums[i]>0 and nums[i]<=len(nums) and nums[nums[i]-1]!= nums[i]):
                tmp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[tmp-1] = tmp
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i+1
            
        return len(nums) + 1

sol = Solution()
print(sol.firstMissingPositive([3,4,-1,1]))
