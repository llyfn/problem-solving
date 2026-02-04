class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        sl = SortedList(nums[1 : dist + 2])
        min_s = s = sum(sl[:k - 1])
        for i in range(dist + 2, len(nums)):
            old, new = nums[i - (dist + 1)], nums[i]
            idx = sl.index(old)
            sl.remove(old)
            if idx < k - 1:
                s -= old
                if len(sl) >= k - 1: s += sl[k - 2]
            sl.add(new)
            if sl.index(new) < k - 1:
                s += new
                if len(sl) > k - 1: s -= sl[k - 1]
            min_s = min(min_s, s)
        return nums[0] + min_s