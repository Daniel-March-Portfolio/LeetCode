# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        buffer = {}
        return self._isBalanced(root, buffer)

    def _isBalanced(self, root: Optional[TreeNode], buffer: dict[TreeNode, int]) -> bool:
        if root is None:
            return True
        if not -1 <= self.calc_depth(root.left, buffer) - self.calc_depth(root.right, buffer) <= 1:
            return False
        return self._isBalanced(root.left, buffer) and self._isBalanced(root.right, buffer)

    def calc_depth(self, node: TreeNode, buffer: dict[TreeNode, int]) -> int:
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        if node not in buffer:
            buffer[node] = 1 + max(self.calc_depth(node.left, buffer), self.calc_depth(node.right, buffer))
        return buffer[node]

