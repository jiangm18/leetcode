import copy
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        preNode = {}
        HashMap = {}
        for e in wordList:
            HashMap[e] = True
        if endWord not in HashMap:
            return []
        self.BFS(preNode, HashMap, beginWord, endWord)
        res = []
        out = []
        if endWord not in preNode:
            return res
        self.DFS(beginWord, endWord, out, preNode, res)
        return res
    def DFS(self, beginWord, t, out, preNode, res):
        tmp = copy.deepcopy(out)
        if beginWord == t:
            tmp.append(beginWord)
            tmp.reverse()
            res.append(tmp)
            return
        else:
            tmp.append(t)
            for i in range(len(preNode[t])):
                self.DFS(beginWord, preNode[t][i], tmp, preNode, res)
    def BFS(self, preNode, HashMap, beginWord, endWord):
        queue = []
        visited = {beginWord:True}
        queue.append(beginWord)
        while queue:
            length = len(queue)
            tmpVisited = {}
            while(length > 0):
                current = queue[0]
                queue = queue[1:]
                connect = self.isConnected(HashMap, current, endWord, visited)
                for i in range(len(connect)):
                    if connect[i] not in preNode:
                        tmpVisited[connect[i]] = True
                        queue.append(connect[i])
                        preNode[connect[i]] = [current]
                    else:
                        preNode[connect[i]].append(current)
                length = length - 1
            for e in tmpVisited:
                visited[e] = True
            if endWord in visited:
                return
    def isConnected(self, HashMap, current, endWord, visited):
        connect = []
        for i in range(len(current)):
            cur = current
            for j in xrange(26):
                if chr(j+ord('a')) == current[i]:
                    continue
                else:
                    cur = cur[:i] + chr(j+ord('a')) + cur[(i+1):]
                    if (cur == endWord or cur in HashMap) and (cur not in visited):
                        connect.append(cur)
        return connect
sol = Solution()
print sol.findLadders("hit","cog",["hot","dot","dog","lot","log"])
