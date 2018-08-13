class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        res = []
        if strs == None or len(strs) == 0:
            return res
        for str in strs:
            sortstr = ''.join(sorted(str))
            if sortstr in dic:
                dic[sortstr].append(str)
            else:
                dic[sortstr] = [str]
        for e in dic:
            res.append(dic[e])
        return res

sol = Solution()
print sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
