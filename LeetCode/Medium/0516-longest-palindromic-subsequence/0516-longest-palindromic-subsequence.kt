class Solution {
    fun longestPalindromeSubseq(s: String): Int {
        val n = s.length
        if (n == 0) return 0
        val dp = Array(n) { IntArray(n) }
        for (i in 0..<n) dp[i][i] = 1
        for (j in 0..<n) for (i in j - 1 downTo 0) {
            if (s[i] == s[j]) dp[i][j] = dp[i + 1][j - 1] + 2
            else dp[i][j] = maxOf(dp[i + 1][j], dp[i][j - 1])
        }
        return dp[0][n - 1]
    }
}