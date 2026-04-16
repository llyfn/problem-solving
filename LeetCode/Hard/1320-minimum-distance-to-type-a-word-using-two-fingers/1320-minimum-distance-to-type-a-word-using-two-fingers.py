class Solution:
    def minimumDistance(self, word: str) -> int:
        def pos(c):
            i = ord(c) - ord('A')
            return (i // 6, i % 6)
        
        def dist(a, b):
            if a is None:
                return 0
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def dp(i, other):
            if i == len(word):
                return 0
            cur = pos(word[i])
            prev = pos(word[i-1]) if i > 0 else None
            
            move_this = dist(prev, cur) + dp(i + 1, other)
            move_other = dist(other, cur) + dp(i + 1, prev)
            
            return min(move_this, move_other)
        
        return dp(0, None)
