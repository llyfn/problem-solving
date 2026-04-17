class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def rev(x):
            return int(str(x)[::-1])

        last = {}
        ans = float('inf')
        for j, v in enumerate(nums):
            if v in last:
                ans = min(ans, j - last[v])
            r = rev(v)
            if r in last:
                if last[r] < j:
                    pass
            last[rev(v)] = j
        return ans if ans != float('inf') else -1