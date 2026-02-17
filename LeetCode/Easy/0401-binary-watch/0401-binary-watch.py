class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        f = lambda r, n: [i for i in range(r) if i.bit_count() == n]
        return [f"{h}:{m:02d}" for H in range(min(turnedOn, 3) + 1) for h in f(12, H) for m in f(60, turnedOn - H)]
