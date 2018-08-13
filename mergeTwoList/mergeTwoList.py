class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        if l1 == None and l2 != None:
            return l2
        if l1 != None and l2 == None:
            return l1
        p1 = l1
        temp = p1
        p2 = l2
        while(p1 != None and p2 != None):
            while (p1 != None and p1.val <= p2.val):
                temp = p1
                p1 = p1.next
            if temp != p1:
                temp.next = p2
            temp = p2
            if p1 == None:
                break
            while (p2 != None and p2.val <= p1.val):
                temp = p2
                p2 = p2.next
            if temp != p2:
                temp.next = p1
            if p2 == None:
                break
        if l1.val <= l2.val:
            return l1
        else:
            return l2
