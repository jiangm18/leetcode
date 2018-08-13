class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None or  head.next == None:
            return head
        newNode = ListNode(None)
        newNode.next = head
        tmp = ListNode(None)
        tmphead = tmp
        pre = newNode
        cur = head
        while(cur != None):
            if cur.val < x:
                pre = cur
                cur = cur.next
            else:
                while(cur != None and cur.val >= x):
                    tmp.next = cur
                    tmp = cur
                    cur = cur.next
                tmp.next = None
                pre.next = cur
        pre.next = tmphead.next
        return newNode.next
head = ListNode(1)
head.next = ListNode(1)
sol = Solution()
print sol.partition(head,2)
