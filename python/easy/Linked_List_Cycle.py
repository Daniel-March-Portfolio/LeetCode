# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow_head = head
        fast_head = head.next

        while fast_head is not None and slow_head != fast_head:
            slow_head = slow_head.next
            fast_head = fast_head.next
            if fast_head is not None:
                fast_head = fast_head.next

        return fast_head is not None
