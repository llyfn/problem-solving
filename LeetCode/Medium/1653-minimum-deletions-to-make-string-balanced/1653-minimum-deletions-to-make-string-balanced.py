class Solution:
    def minimumDeletions(self, s: str) -> int:
        a, b = s.count('a'), 0
        r = len(s)
        for c in s:
            if c == 'a': a -= 1
            r = min(r, a + b)
            if c == 'b': b += 1
        return r