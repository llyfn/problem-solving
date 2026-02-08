# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(n):
            if not n: return 0
            l, r = dfs(n.left), dfs(n.right)
            if l == -1 or r == -1 or abs(l - r) > 1: return -1
            return 1 + max(l, r)
        return dfs(root) != -1