# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, maxx, minn):
            if not node:
                return True

            if node.val >= maxx or node.val <= minn:
                return False

            return isValid(node.left, node.val, minn) and isValid(node.right, maxx, node.val)

        return isValid(root, float('inf'), float('-inf'))