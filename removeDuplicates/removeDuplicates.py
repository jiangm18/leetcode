class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:
            return 0
        tmp = []
        for e in nums:
            if e not in tmp:
                tmp.append(e)
        print tmp
        return len(tmp)
        
sol = Solution()
print(sol.removeDuplicates([1,1,2]))
