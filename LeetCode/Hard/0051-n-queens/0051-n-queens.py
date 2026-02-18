class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        col = []
        def is_valid(r, c):
            for i in range(r):
                if col[i] == c or i + col[i] == r + c or i - col[i] == r - c: return False
            return True
        def format_output():
            return ["." * c + "Q" + "." * (n - c - 1) for c in col]
        def dfs(r):
            if r == n - 1:
                ans.append(format_output())
                return
            for c in range(n):
                if is_valid(r + 1, c):
                    col.append(c)
                    dfs(r + 1)
                    col.pop()
        dfs(-1)
        return ans