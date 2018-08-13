class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a, b = b, a
        res = ""
        a = a[::-1]
        b = b[::-1]
        length = len(b)
        pos = 0
        carry = 0
        while(pos < length):
            tmp = int(a[pos]) + int(b[pos]) + carry
            res = res + str(tmp%2)
            carry = tmp/2
            pos = pos + 1
        while(pos < len(a)):
            tmp = int(a[pos]) + carry
            print tmp
            res = res + str(tmp%2)
            carry = tmp/2
            pos = pos + 1
        if carry == 1:
            res = res + '1'
        return res[::-1]
        
sol = Solution()
print sol.addBinary("1", "111")
