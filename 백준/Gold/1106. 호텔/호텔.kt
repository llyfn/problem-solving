fun main() = with(System.`in`.bufferedReader()) {
    val (c, n) = readLine().split(" ").map { it.toInt() }
    val costs = List(n) { readLine().split(" ").map { it.toInt() } }
    val maxC = 100
    val dp = Array(c + maxC) { 100_000_000 }
    dp[0] = 0
    for ((p, q) in costs) for (i in 1..<c + maxC) if (i >= q) dp[i] = minOf(dp[i], dp[i - q] + p)
    println(dp.takeLast(maxC).min())
}