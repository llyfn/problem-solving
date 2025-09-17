import kotlin.math.*
fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val a = readLine().split(" ").map { it.toInt() }
    val dp = Array(n + 1) { IntArray(500001) { -1 } }
    fun dfs(c: Int, d: Int): Int {
        if (dp[c][d] != -1) return dp[c][d]
        if (c == n) return if (d != 0) Int.MIN_VALUE else 0
        dp[c][d] = maxOf(dfs(c + 1, d), dfs(c + 1, d + a[c]) + a[c], dfs(c + 1, abs(d - a[c])) + maxOf(a[c] - d, 0))
        return dp[c][d]
    }
    val ans = dfs(0, 0)
    println(if (ans > 0) ans else -1)
}