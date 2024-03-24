# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_head_head = ListNode()
        new_head = new_head_head
        while head is not None:
            if head.val == val:
                head = head.next
            else:
                new_head.next = ListNode(head.val)
                new_head = new_head.next
                head = head.next

        return new_head_head.next

