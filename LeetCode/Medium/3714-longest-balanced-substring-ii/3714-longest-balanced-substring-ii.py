class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 1

        res = 1
        for i in range(1, n):
            if s[i] == s[i-1]: res += 1; ans = max(ans, res)
            else: res = 1

        for c1, c2, ig in ('a', 'b', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'):
            pos = {0: -1}
            diff = 0
            for i in range(n):
                if s[i] == ig:
                    pos = {0: i}
                    diff = 0
                else:
                    if s[i] == c1: diff += 1
                    else: diff -= 1
                    if diff in pos: ans = max(ans, i - pos[diff])
                    else: pos[diff] = i

        pos = {(0, 0): -1}
        cnt = [0] * 3
        for i in range(n):
            if s[i] == 'a': cnt[0] += 1
            elif s[i] == 'b': cnt[1] += 1
            else: cnt[2] += 1
            diff = (cnt[0] - cnt[1], cnt[1] - cnt[2])
            if diff in pos: ans = max(ans, i - pos[diff])
            else: pos[diff] = i

        return ans