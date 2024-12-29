fun main() = with(System.`in`.bufferedReader()) {
    val nk = readLine().split(" ").map { it.toInt() }

    val dp = Array(nk[1] + 1) { LongArray(nk[0] + 1) { 0 } }
    dp[1] = LongArray(nk[0] + 1) { 1 }

    for (k in 2..nk[1]) {
        for (n in 0..nk[0]) {
            for (l in 0..n) dp[k][n] += dp[k - 1][l]
            dp[k][n] = dp[k][n] % 1000000000
        }
    }

    println(dp[nk[1]][nk[0]])
    close()
}