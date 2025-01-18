fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val a = readLine().split(" ").map { it.toInt() }.toIntArray()
    val dp = IntArray(n)
    val x = mutableListOf(0)
    val y = IntArray(n)

    for (i in 0..<n) {
        dp[i] = x.binarySearch(a[i]).let { if (it < 0) -it - 1 else it }
        if (x.size <= dp[i]) x.add(a[i])
        if (a[i] < x[dp[i]]) x[dp[i]] = a[i]
        y[i] = dp[i]
    }
    println(dp.max())
    val s = buildList {
        var idx = x.size - 1
        for (i in n - 1 downTo 0) {
            if (y[i] == idx) { add(a[i]); idx-- }
        }
    }
    println(s.reversed().joinToString(" "))
    close()
}