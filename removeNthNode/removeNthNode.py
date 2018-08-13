class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        newNode = ListNode(None)
        newNode.next = head
        pointer = newNode
        while pointer.next != None:
            temp = pointer
            for _ in range(n+1):
                temp = temp.next
            if temp == None:
                temp = pointer.next
                pointer.next = temp.next
                temp.next = None
                break
            pointer = pointer.next
        return newNode.next


sol = Solution()
sol.removeNthFromEnd()
