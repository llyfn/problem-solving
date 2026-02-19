class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = [0] * k
        for i in range(0, len(energy)): dp[i % k] = max(0, dp[i % k]) + energy[i]
        return max(dp[-k:])