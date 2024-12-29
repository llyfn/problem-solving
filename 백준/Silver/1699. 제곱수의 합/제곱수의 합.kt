import kotlin.math.min
import kotlin.math.pow
import kotlin.math.sqrt

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()

    val dp = IntArray(n + 1) { n }
    dp[0] = 0
    for (i in 1..n) for (j in 1..sqrt(i.toDouble()).toInt())
        dp[i] = min(dp[i-j.toDouble().pow(2).toInt()] + 1, dp[i])

    println(dp[n])

    close()
}