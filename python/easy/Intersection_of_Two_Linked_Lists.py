# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not self.is_linked_lists_has_common_node(headA, headB):
            return None

        slow = self.get_next_slow(headA, headB)
        fast = self.get_next_fast(headA, headB)

        while slow is not fast:
            slow = self.get_next_slow(headA, slow)
            fast = self.get_next_fast(headA, fast)

        fast = headB
        while slow is not fast:
            slow = self.get_next_slow(headA, slow)
            fast = self.get_next_slow(headA, fast)
        return slow

    def is_linked_lists_has_common_node(self, headA: ListNode, headB: ListNode) -> bool:
        while headA.next is not None:
            headA = headA.next
        while headB.next is not None:
            headB = headB.next
        return headA is headB

    def get_next_fast(self, head: ListNode, node: ListNode) -> ListNode:
        node = node.next
        if node is None:
            node = head
        node = node.next
        if node is None:
            node = head
        return node

    def get_next_slow(self, head: ListNode, node: ListNode) -> ListNode:
        node = node.next
        if node is None:
            node = head
        return node
