class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        fin = [0] * n
        for j in range(m):
            start = fin[0]
            t = 0
            for i in range(n):
                t += skill[i] * mana[j]
                fin[i] = t
                if i < n - 1: start = max(start, fin[i + 1] - t)
            for i in range(n): fin[i] += start
        return fin[-1]