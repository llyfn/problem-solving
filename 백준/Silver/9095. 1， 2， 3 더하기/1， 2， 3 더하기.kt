fun main() = with(System.`in`.bufferedReader()) {
    val cases = readLine().toInt()

    val nums: MutableList<Int> = mutableListOf()
    for (i in 1..cases) nums.add(readLine().toInt())

    val dp = IntArray(11) { i -> if (i == 2) 2 else 1 }
    for (i in 3..10) dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    nums.forEach { println(dp[it]) }

    close()
}
