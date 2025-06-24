fun main() = with(System.`in`.bufferedReader()) {
    val mins = listOf<Long>(0, 0, 1, 7, 4, 2, 0, 8)
    val dp = (listOf<Long>(9, 9, 1, 7, 4, 2, 6, 8) + List(100) { Long.MAX_VALUE }).toMutableList()
    for (i in 8..100) for (j in 2..7) dp[i] = minOf(dp[i], 10 * dp[i - j] + mins[j])
    val ns = List(readLine().toInt()) { readLine().toInt() }
    for (n in ns) {
        val max = if (n % 2 == 0) "1".repeat(n / 2) else "7" + "1".repeat((n - 3) / 2)
        println("${dp[n]} $max")
    }
    close()
}