class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r = [0] * n
        for i in range(n): r[i] = nums[(i + nums[i]) % n]
        return r