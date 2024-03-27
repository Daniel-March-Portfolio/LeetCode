# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root = ListNode(next=head)
        fast_point = head
        for _ in range(n):
            fast_point = fast_point.next

        slow_point = root

        while fast_point is not None:
            fast_point = fast_point.next
            slow_point = slow_point.next
        slow_point.next = slow_point.next.next

        return root.next