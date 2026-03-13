class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        l, r, ans = 1, max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2, 0
        eps = 1e-9
        while l <= r:
            mid = (l + r) // 2
            cnt = 0
            for t in workerTimes: cnt += int((-1 + ((1 + mid // t * 8) ** 0.5)) / 2 + eps)
            if cnt < mountainHeight: l = mid + 1
            else:
                ans = mid
                r = mid - 1
        return ans