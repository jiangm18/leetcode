class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1.extend(nums2)
        print nums1
        nums1.sort()
        nums1 = nums1[len(nums1)-(m+n):len(nums1)]
        print nums1
        
        
sol = Solution()
nums1 = [0]
m = 0
nums2 = [1]
n = 1
sol.merge(nums1,m,nums2,n)


