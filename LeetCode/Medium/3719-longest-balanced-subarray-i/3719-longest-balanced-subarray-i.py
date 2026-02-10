class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        for l in range(len(nums), -1, -1):
            c = [Counter(), Counter()]
            for i in nums[:l]: c[i & 1][i] += 1
            if len(c[0]) == len(c[1]): return l
            for k in range(len(nums) - l):
                o, i = nums[k], nums[l + k]
                c[o & 1][o] -= 1
                if not c[o & 1][o]: del c[o & 1][o]
                c[i & 1][i] += 1
                if len(c[0]) == len(c[1]): return l
        return 0