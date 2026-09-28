# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):

        if not head or not head.next:
            return True
        
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        while slow:
            nxt=slow.next
            slow.next=prev
            prev=slow
            slow=nxt
        
        slow=head
        while prev:
            if slow.val!=prev.val:
                return False
            slow=slow.next
            prev=prev.next
        
        return True
            

        