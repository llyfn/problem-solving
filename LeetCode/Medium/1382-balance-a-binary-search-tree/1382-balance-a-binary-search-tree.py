class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        l = []
        def inorder(n):
            if n: inorder(n.left); l.append(n.val); inorder(n.right)
        def build(s, e):
            if s > e: return None
            m = (s + e) // 2
            return TreeNode(l[m], build(s, m - 1), build(m + 1, e))
        inorder(root)
        return build(0, len(l) - 1)