fun main() = with(System.`in`.bufferedReader()) {
    val t = readLine().toInt()
    val arr = mutableListOf<Int>().apply{ for (i in 1..t) add(readLine().toInt()) }

    val dp = Array(arr.maxOrNull()!! + 1) {LongArray(3) {0} }
    dp[1][0] = 1; dp[2][1] = 1; dp[3][0] = 1; dp[3][1] = 1; dp[3][2] = 1
    for (i in 4..arr.maxOrNull()!!) {
        dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009
        dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % 1000000009
        dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % 1000000009
    }

    arr.forEach { println(dp[it].sum() % 1000000009) }
    close()
}