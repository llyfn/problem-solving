class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        sum = 0
        def dfs(node: Optional[TreeNode], path_sum: int):
            if not node: return
            val = 2 * path_sum + node.val
            if node.left or node.right: dfs(node.left, val); dfs(node.right, val)
            else: nonlocal sum; sum += val
        dfs(root, 0)
        return sum