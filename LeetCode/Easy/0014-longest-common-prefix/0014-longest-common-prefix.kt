class Solution {
    fun longestCommonPrefix(strs: Array<String>): String {
        var ans = ""
        idx@for (i in 0..<strs.minOf { it.length }) {
            var c = strs[0][i]
            for (s in strs.drop(1)) if (c != s[i]) break@idx
            ans += c
        }
        return ans
    }
}