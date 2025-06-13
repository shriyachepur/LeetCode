# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        \\\
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        \\\
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        current=slow
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        first=head
        second=prev

        while second and first != second and first.next != second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
    
    

        
        
        