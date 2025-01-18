fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val a = readLine().split(" ").map { it.toInt() }.toIntArray()
    val dp = IntArray(n)
    val x = mutableListOf(0)

    for (i in 0..<n) {
        dp[i] = x.binarySearch(a[i]).let { if (it < 0) -it - 1 else it }
        if (x.size <= dp[i]) x.add(a[i])
        if (a[i] < x[dp[i]]) x[dp[i]] = a[i]
    }

    print(dp.max())
    close()
}