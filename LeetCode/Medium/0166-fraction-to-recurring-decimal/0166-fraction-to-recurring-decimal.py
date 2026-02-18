class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = "-" if (numerator < 0) ^ (denominator < 0) else ""
        n, d = abs(numerator), abs(denominator)
        res += str(n // d)
        rem = n % d
        rem_idx = {}
        if rem: res += "."
        while rem:
            rem_idx[rem] = len(res)
            rem *= 10
            res += str(rem // d)
            rem %= d
            if rem in rem_idx: res = f"{res[:rem_idx[rem]]}({res[rem_idx[rem]:]})"; break
        return res