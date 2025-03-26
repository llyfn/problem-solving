fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()

    val dp = Array(n + 1) {LongArray(10) {1} }
    dp[1][0] = 0
    for (i in 2..n) {
        dp[i][0] = dp[i-1][1]; dp[i][9] = dp[i-1][8]
        for (j in 1..8) dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000
    }

    println(dp[n].sum() % 1000000000)
    close()
}