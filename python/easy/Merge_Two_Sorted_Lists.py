# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result_list = ListNode(val=None)

        prev_result_node = ListNode(next=result_list)
        current_result_node = result_list

        current_list1_node = list1
        current_list2_node = list2

        while current_list1_node is not None and current_list2_node is not None:
            if current_list1_node.val < current_list2_node.val:
                current_result_node.val = current_list1_node.val
                current_list1_node = current_list1_node.next
            else:
                current_result_node.val = current_list2_node.val
                current_list2_node = current_list2_node.next
            current_result_node.next = ListNode()
            prev_result_node = current_result_node
            current_result_node = current_result_node.next

        not_empty_node = current_list1_node if current_list1_node is not None else current_list2_node
        while not_empty_node is not None:
            current_result_node.val = not_empty_node.val
            current_result_node.next = ListNode()
            prev_result_node = current_result_node
            current_result_node = current_result_node.next
            not_empty_node = not_empty_node.next

        prev_result_node.next = None
        return result_list if result_list.val is not None else None
