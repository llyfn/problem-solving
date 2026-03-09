import java.io.StreamTokenizer

fun main() = with(StreamTokenizer(System.`in`.bufferedReader())) {
    val nextInt = { nextToken(); nval.toInt() }
    val n = nextInt()
    val a = IntArray(n) { nextInt() }
    var dp = IntArray(2)
    for (x in a) dp = intArrayOf(dp.max(), dp[0] + x, dp[1] + x)
    println(dp.max())
}
