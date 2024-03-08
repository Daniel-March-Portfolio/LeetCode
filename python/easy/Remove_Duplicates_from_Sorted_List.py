# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        new_head = ListNode(val=head.val)
        new_tail = new_head

        head = head.next
        while head is not None:
            if head.val != new_tail.val:
                new_tail.next = ListNode(val=head.val)
                new_tail = new_tail.next
            head = head.next

        return new_head