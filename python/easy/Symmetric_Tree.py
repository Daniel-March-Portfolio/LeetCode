# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left_part = [root.left]
        right_part = [root.right]

        while len(left_part) > 0 and len(right_part) > 0:
            left = left_part.pop(0)
            right = right_part.pop(0)

            if left is None or right is None:
                if left is None and right is None:
                    continue
                return False
            elif left.val != right.val:
                return False

            left_part.extend([left.left, left.right])
            right_part.extend([right.right, right.left])

        return True