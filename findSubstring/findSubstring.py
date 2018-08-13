class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        if s == None or len(s) == 0 or words == None or len(words) == 0:
            return res
        dic = self.iniMap(words)
        print dic
        count = len(words)
        countChanged = False
        wordsLen = len(words[0])
        for i in range(len(s)-wordsLen*len(words)+1):
            subStr = s[i:i+wordsLen]
            j = i
            while (subStr in dic and dic[subStr] > 0 and j + wordsLen <= len(s)):
                dic[subStr] = dic[subStr] - 1
                count = count - 1
                countChanged = True
                j = j + wordsLen
                subStr = s[j: j+wordsLen]
                if subStr not in dic:
                    break
            if count == 0:
                res.append(i)
            if countChanged:
                dic = self.iniMap(words)
                count = len(words)
                countChanged = False
        return res
    def iniMap(self,words):
        dic = {}
        for i in range(len(words)):
            if words[i] in dic:
                dic[words[i]] = dic[words[i]] + 1
            else:
                dic[words[i]] = 1
        return dic
sol = Solution()
print(sol.findSubstring("barfoothefoobarman",["foo","bar"]))
