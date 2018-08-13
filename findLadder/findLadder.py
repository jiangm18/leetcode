import sys
import copy
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        res = []
        HashMap = {}
        for e in wordList:
            HashMap[e] = True
        path = [[beginWord],""]
        del HashMap[beginWord]
        visited ={}
        level = 1
        minlevel = sys.maxint
        while path:
            if level >= minlevel:
                break
            t = path[0]
            path = path[1:]
            if t != "":
                last = t[-1]
                for i in range(len(last)):
                        newlast = last
                        for j in xrange(26):
                            if chr(j+ord('a')) == last[i]:
                                continue
                            else:
                                newlast = newlast[:i] + chr(j+ord('a')) + newlast[(i+1):]
                                if newlast in HashMap and HashMap[newlast] == True:
                                    visited[newlast] = True
                                    nextPath = copy.deepcopy(t)
                                    nextPath.append(newlast)
                                    if newlast == endWord:
                                        res.append(nextPath)
                                        minlevel = min(minlevel,level+1)
                                    else:
                                        path.append(nextPath)
                                        
            else:
                if path:
                    path.append("")
                    level = level + 1
                    for e in visited:
                        HashMap[e] = False
                    visited = {}
        return res
sol = Solution()
print sol.findLadders("red","tax",["ted","tex","red","tax","tad","den","rex","pee"])
