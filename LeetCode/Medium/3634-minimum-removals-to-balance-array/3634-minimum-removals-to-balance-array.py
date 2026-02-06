class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min(len(nums) - bisect_right(nums, nums[l] * k) + l for l in range(len(nums)))