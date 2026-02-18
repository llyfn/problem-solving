class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}
        for i in range(len(nums)):
            if target - nums[i] in num_idx: return [num_idx[target - nums[i]], i]
            num_idx[nums[i]] = i
        return []