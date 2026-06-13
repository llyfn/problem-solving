class Solution {
    fun wordBreak(s: String, wordDict: List<String>): Boolean {
        val dict = wordDict.toSet()
        val dp = BooleanArray(s.length)
        for (i in s.indices) if (i == 0 || dp[i-1]) {
            for (j in i..s.length) if (dict.contains(s.substring(i, j))) dp[j - 1] = true
        }
        return dp.last()
    }
}