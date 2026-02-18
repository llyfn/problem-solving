class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        return sum(bisect_left(nums[j + 1:], nums[i] + nums[j]) for i in range(n - 2) for j in range(i + 1, n - 1))
