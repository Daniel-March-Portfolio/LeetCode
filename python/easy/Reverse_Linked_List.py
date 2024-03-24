# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        new_head = ListNode(head.val)
        head = head.next
        while head is not None:
            new_head = ListNode(head.val, new_head)
            head = head.next

        return new_head