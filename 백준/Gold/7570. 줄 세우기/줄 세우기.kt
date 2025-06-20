fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val seq = readLine().split(" ").map { it.toInt() }
    var max = 0
    val dp = IntArray(n + 1) { 0 }
    for (i in seq) {
        dp[i] = dp[i - 1] + 1
        max = maxOf(max, dp[i])
    }
    println(n - max)
    close()
}
