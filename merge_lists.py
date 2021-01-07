# Merge two sorted linked lists and return it as a sorted list. 
# The list should be made by splicing together the nodes of the first two lists.

 # Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def mergeTwoLists(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyNode = ListNode()
        dummyNode.val = -1
        head = dummyNode
        while(l1 != None and l2 != None):
            if(l1.val < l2.val):
                dummyNode.next = l1
                l1 = l1.next
            else:
                dummyNode.next = l2
                l2 = l2.next
            dummyNode = dummyNode.next
        if(l1 != None):
            dummyNode.next = l1
        else:
            dummyNode.next = l2
            
        return head.next
