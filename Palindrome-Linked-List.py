# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        \\\
        :type head: Optional[ListNode]
        :rtype: bool
        \\\
        slow = fast = head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        if fast!=None:
            slow=slow.next
        prev = None
        current=slow
        while current:
            next_node=current.next
            current.next = prev
            prev = current
            current = next_node
        slow = prev
        fast = head
        while slow:
            if fast.val!=slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True




        
