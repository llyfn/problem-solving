class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = map(int, version1.split("."))
        v2 = map(int, version2.split("."))
        for i, j in zip_longest(v1, v2, fillvalue=0):
            if i > j: return 1
            elif i < j: return -1
        return 0
