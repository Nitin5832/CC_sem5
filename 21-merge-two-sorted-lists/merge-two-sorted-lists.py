# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
    
        head=None
        head1=list1
        head2=list2

        if head1.val<=head2.val:
            head=head1
            head1=head1.next
        else:
            head=head2
            head2=head2.next
        
        current = head
        while head1 and head2:
            if head1.val<=head2.val :
                current.next=head1
                head1=head1.next
                current=current.next
                continue
            current.next=head2
            head2=head2.next
            current=current.next

        if head1:
            current.next=head1
        if head2:
            current.next=head2

        return head

            
            

            
            


        
        