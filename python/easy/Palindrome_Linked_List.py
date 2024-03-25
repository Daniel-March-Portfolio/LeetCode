# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_len = self.get_list_len(head)

        stack = []
        n_nodes_till_middle = list_len // 2

        while n_nodes_till_middle > 0:
            stack.append(head)
            head = head.next
            n_nodes_till_middle -= 1

        if list_len % 2 != 0:
            head = head.next

        while head is not None:
            if head.val != stack.pop().val:
                return False
            head = head.next

        return True

    def get_list_len(self, head: Optional[ListNode]) -> int:
        l = 0
        while head is not None:
            head = head.next
            l += 1
        return l