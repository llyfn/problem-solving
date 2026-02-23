class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        dist = -1e9
        while n:
            if n & 1: ans = max(ans, dist); dist = 1
            else: dist += 1
            n >>= 1
        return ans