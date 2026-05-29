# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return

        if p.val > q.val:
            p, q = q, p

        curr = root
        while curr:
            if curr.val > q.val:
                curr = curr.left
            elif curr.val < p.val:
                curr = curr.right
            else:
                return curr

        return