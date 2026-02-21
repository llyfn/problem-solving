class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        return max((next(i for i in range(len(s) + 1) if x + i not in s) for x in s if x - 1 not in s), default = 0)