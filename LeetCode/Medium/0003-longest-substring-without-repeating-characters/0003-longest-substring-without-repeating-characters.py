class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = {}
        ans = l = r = 0
        while r < len(s):
            c = s[r]
            r += 1
            cnt[c] = cnt.get(c, 0) + 1
            while cnt[c] > 1:
                cnt[s[l]] -= 1
                l += 1
            ans = max(ans, r - l)
        return ans