class Solution:
    def totalMoney(self, n: int) -> int:
        q = n // 7
        r = n % 7
        return q * 28 + q * (q - 1) * 7 // 2 + q * r + r * (r + 1) // 2