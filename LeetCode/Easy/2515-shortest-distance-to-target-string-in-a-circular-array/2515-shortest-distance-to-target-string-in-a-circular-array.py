class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        n = len(words)
        res = n
        for i in range(n):
            if words[i] == target:
                res = min(res, min(abs(i - startIndex), n - abs(i - startIndex)))
        return res if res < n else -1
