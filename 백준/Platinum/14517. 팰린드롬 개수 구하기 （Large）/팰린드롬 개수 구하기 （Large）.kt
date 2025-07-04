fun main() = with(System.`in`.bufferedReader()) {
    val s = readLine()
    val n = s.length
    val dp = Array(n) { IntArray(n) }
    val mod = 10007
    for (i in 0..<n) dp[i][i] = 1
    for (i in 1..<n) {
        dp[i - 1][i] = 2
        if (s[i] == s[i - 1]) dp[i - 1][i]++
    }
    for (i in 2..<n) for (j in i..<n) {
        if (s[j] == s[j - i]) dp[j - i][j] = (dp[j - i][j - 1] + dp[j - i + 1][j] + 1) % 10007
        else dp[j - i][j] = (mod + dp[j - i][j - 1] + dp[j - i + 1][j] - dp[j - i + 1][j - 1]) % 10007
    }
    println(dp[0][n - 1])
}