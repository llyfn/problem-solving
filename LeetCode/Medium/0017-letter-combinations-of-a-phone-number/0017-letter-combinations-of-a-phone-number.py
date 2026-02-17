class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        chars = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        ans = [""]
        for i in range(len(digits)): ans = [s + c for s in ans for c in chars[digits[i]]]
        return ans