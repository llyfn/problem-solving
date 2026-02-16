class Solution:
    def reverse(self, x: int) -> int:
        pos = x >= 0
        rev = str(x)[::-1] if pos else str(x)[:0:-1]
        r = 2 ** 31 // 10
        if len(rev) == 10 and (int(rev[:9]) > r or int(rev[:9]) == r and int(rev[9]) > 8 - pos): return 0
        else: return int(rev) if pos else -int(rev)