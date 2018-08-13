import copy
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        out = []
        if candidates == None or len(candidates) == 0:
            return res
        self.combinationSumDFS(candidates, target, 0, out, res)
        return res
        
    def combinationSumDFS(self, candidates, target, start, out, res):
        if target < 0:
            return
        else:
            if target == 0:
                tmp = copy.deepcopy(out)
                res.append(tmp)
            else:
                for i in range(start, len(candidates)):
                    out.append(candidates[i])
                    print '1',out,res
                    self.combinationSumDFS(candidates, target - candidates[i], i, out, res)
                    print '2',out,res
                    out.pop()
                    print '3',out,res
sol = Solution()
print(sol.combinationSum([2,3,6,7],7))
