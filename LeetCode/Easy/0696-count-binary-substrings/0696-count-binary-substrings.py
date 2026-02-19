class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = " "
        prev_cnt = cnt = ans = 0
        for c in s:
            if c == prev: cnt += 1
            else: prev, prev_cnt, cnt = c, cnt, 1
            if prev_cnt >= cnt: ans += 1
        return ans