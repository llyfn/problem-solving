class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        diff = arr[1] - arr[0]
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == diff: ans.append([arr[i], arr[i + 1]])
            elif arr[i + 1] - arr[i] < diff: ans = [[arr[i], arr[i + 1]]]; diff = arr[i + 1] - arr[i]
        return ans