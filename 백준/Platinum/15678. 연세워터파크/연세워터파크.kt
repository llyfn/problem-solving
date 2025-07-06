fun main() = with(System.`in`.bufferedReader()) {
    val (n, d) = readLine().split(" ").map { it.toInt() }
    val dp = mutableListOf(0L).apply { addAll(readLine().split(" ").map { it.toLong() }) }
    val q = ArrayDeque<Pair<Int, Long>>()
    for (i in 1..n) {
        while (q.isNotEmpty() && q.first().first < i - d) q.removeFirst()
        if (q.isNotEmpty()) dp[i] += maxOf(0, q.first().second)
        while (q.isNotEmpty() && q.last().second <= dp[i]) q.removeLast()
        q.addLast(i to dp[i])
    }
    println(dp.drop(1).max())
}