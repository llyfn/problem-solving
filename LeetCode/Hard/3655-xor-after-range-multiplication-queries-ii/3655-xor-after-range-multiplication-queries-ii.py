class Solution:
    def xorAfterQueries(self, nums, queries):
        import math
        
        MOD = 10**9 + 7
        n = len(nums)
        T = max(1, int(math.isqrt(n)))
        
        groups = [[] for _ in range(T)]
        
        for l, r, k, v in queries:
            if k < T:
                groups[k].append((l, r, v))
            else:
                idx = l
                while idx <= r:
                    nums[idx] = nums[idx] * v % MOD
                    idx += k
        
        dif = [1] * (n + T)
        
        for k in range(1, T):
            if not groups[k]:
                continue
            
            for i in range(n + T):
                dif[i] = 1
            
            for l, r, v in groups[k]:
                dif[l] = dif[l] * v % MOD
                R = ((r - l) // k + 1) * k + l
                dif[R] = dif[R] * pow(v, MOD - 2, MOD) % MOD
            
            for i in range(k, n):
                dif[i] = dif[i] * dif[i - k] % MOD
            
            for i in range(n):
                nums[i] = nums[i] * dif[i] % MOD
        
        result = 0
        for x in nums:
            result ^= x
        return result

