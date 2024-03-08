# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        len_nums = len(nums)
        root = TreeNode(val=nums[len_nums // 2])

        if len_nums > 1:
            return self.convert_to_BST(root, nums[:len_nums // 2], nums[len_nums // 2 + 1:])

        return root

    def convert_to_BST(self, root: TreeNode, left: List[int], right: List[int]) -> TreeNode:
        len_left = len(left)
        len_right = len(right)

        if len_left == 0 and len_right == 0:
            return root

        if len_left > 0:
            root.left = TreeNode(val=left[len_left // 2])
            root.left = self.convert_to_BST(root.left, left[:len_left // 2], left[len_left // 2 + 1:])

        if len_right > 0:
            root.right = TreeNode(val=right[len_right // 2])
            root.right = self.convert_to_BST(root.right, right[:len_right // 2], right[len_right // 2 + 1:])

        return root