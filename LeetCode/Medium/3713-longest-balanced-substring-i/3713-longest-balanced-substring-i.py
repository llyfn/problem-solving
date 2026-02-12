class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        for l in range(n, 0, -1):
            c = Counter(s[:l])
            v = list(c.values())
            if v.count(v[0]) == len(v): return l
            for i in range(n - l):
                i, o = s[l + i], s[i]
                c[o] -= 1
                if c[o] == 0: del c[o]
                c[i] += 1
                v = list(c.values())
                if v.count(v[0]) == len(v): return l
        return 0