class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)
        m = v = 0
        for i in range(len(nums)):
            if nums[i] == v: continue
            v = nums[i]
            t = numOperations
            f = 1
            l = r = i
            while t and l > 1 and -k <= v - nums[l - 1] <= k: l -= 1; t -= v != nums[l]; f += 1
            while t and r < n - 1 and -k <= v - nums[r + 1] <= k: r += 1; t -= v != nums[r]; f += 1
            if f > m: m = f
        return m