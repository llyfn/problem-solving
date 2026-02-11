class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.min = [0] * (4 * n)
        self.max = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def _push(self, cur, l, r):
        if self.lazy[cur] != 0:
            self.min[cur] += self.lazy[cur]
            self.max[cur] += self.lazy[cur]
            if l != r:
                self.lazy[2 * cur + 1] += self.lazy[cur]
                self.lazy[2 * cur + 2] += self.lazy[cur]
            self.lazy[cur] = 0

    def _query_int(self, cur, l, r):
        self._push(cur, l, r)
        if self.min[cur] > 0 or self.max[cur] < 0:
            return self.n
        if l == r:
            return l
        mid = (l + r) // 2
        res = self._query_int(2 * cur + 1, l, mid)
        if res == self.n:
            res = self._query_int(2 * cur + 2, mid + 1, r)
        return res

    def _range_add_int(self, cur, l, r, ql, qr, val):
        self._push(cur, l, r)
        if r < ql or qr < l:
            return
        if ql <= l and r <= qr:
            self.lazy[cur] += val
            self._push(cur, l, r)
            return
        mid = (l + r) // 2
        self._range_add_int(2 * cur + 1, l, mid, ql, qr, val)
        self._range_add_int(2 * cur + 2, mid + 1, r, ql, qr, val)
        self.max[cur] = max(self.max[2 * cur + 1], self.max[2 * cur + 2])
        self.min[cur] = min(self.min[2 * cur + 1], self.min[2 * cur + 2])

    def query_zero_idx(self):
        return self._query_int(0, 0, self.n - 1)

    def range_add(self, ql, qr, val):
        self._range_add_int(0, 0, self.n - 1, ql, qr, val)

class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        prev = {}
        res = 0
        seg_tree = SegmentTree(n)
        for i, val in enumerate(nums):
            idx = prev.get(val, -1)
            nval = 1 - 2 * (val % 2)
            seg_tree.range_add(idx + 1, i, nval)
            prev[val] = i
            min_zero_ind = seg_tree.query_zero_idx()
            res = max(res, i - min_zero_ind + 1)
        return res