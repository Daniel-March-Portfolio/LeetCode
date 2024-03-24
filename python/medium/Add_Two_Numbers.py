# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = ListNode()
        result = result_head

        buffer = 0
        while l1 is not None and l2 is not None:
            val = l1.val + l2.val + buffer
            buffer = val // 10
            val %= 10
            result.next = ListNode(val)
            result = result.next
            l1 = l1.next
            l2 = l2.next

        non_empty = l1
        if l1 is None:
            non_empty = l2

        while non_empty is not None:
            val = non_empty.val + buffer
            buffer = val // 10
            val %= 10
            result.next = ListNode(val)
            result = result.next
            non_empty = non_empty.next

        while buffer != 0:
            result.next = ListNode(buffer % 10)
            buffer //= 10
            result = result.next

        return result_head.next
