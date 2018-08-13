class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or len(s) == 0:
            return 0
        if s[-1] == ' ':
            wordList = s.split(' ')
            return len(wordList[-2])
        else:
            wordList = s.split(' ')
            return len(wordList[-1])
sol = Solution()
print sol.lengthOfLastWord("a ")
