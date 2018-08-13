class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        newNode = ListNode(None)
        newNode.next = head
        p1 = newNode
        p2 = head
        p3 = head.next
        res = head.next
        while(p3 != None):
            p2.next = p3.next
            p3.next = p2
            p1.next = p3
            p1 = p2
            p2 = p2.next
            if p2 == None:
                p3 = None
            else:
                p3 = p2.next
        return res

Node1 = ListNode(1)
Node2 = ListNode(2)
Node3 = ListNode(3)
Node4 = ListNode(4)
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = None
sol = Solution()
sol.swapPairs(Node1)
