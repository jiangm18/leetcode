class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if list == None or len(lists) == 0:
            return None
        return self.mergeSort(lists, 0, len(lists)-1)
    def mergeSort(self, lists, begin, end):
        if begin >= end:
            return lists[begin]
        mid = (begin + end)/2
        begin1 = begin
        end1 = mid
        begin2 = mid + 1
        end2 = end
        list1 = self.mergeSort(lists, begin1, end1)
        list2 = self.mergeSort(lists, begin2, end2)
        return self.mergeTwoLists(list1, list2)
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
