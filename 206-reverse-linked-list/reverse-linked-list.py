class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        
        prev=None
        curr=head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        
        return prev
