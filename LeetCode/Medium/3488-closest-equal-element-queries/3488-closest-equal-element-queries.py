class Solution:
    def solveQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        from collections import defaultdict
        n = len(nums)
        idx = defaultdict(list)
        for i, v in enumerate(nums):
            idx[v].append(i)
        
        dist = [-1] * n
        for v, positions in idx.items():
            if len(positions) < 2:
                continue
            k = len(positions)
            for i in range(k):
                p = positions[i]
                prev_p = positions[(i - 1) % k]
                next_p = positions[(i + 1) % k]
                d1 = (p - prev_p) % n
                d2 = (next_p - p) % n
                dist[p] = min(d1, d2)
        
        return [dist[q] for q in queries]

        