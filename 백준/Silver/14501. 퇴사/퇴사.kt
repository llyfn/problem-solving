fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val t = IntArray(n) { 0 }; val p = IntArray(n) { 0 }; val ans = IntArray(n + 1) { 0 }
    for (i in 0 until n) {
        readLine().split(" ").map{ it.toInt() }.apply {
            t[i] = this[0]
            p[i] = this[1]
        }
    }
    for (i in 0 until n) if (i + t[i] <= n) for (j in i + t[i]..n) if (ans[j] < ans[i] + p[i]) ans[j] = ans[i] + p[i]

    println(ans.maxOrNull())
    close()
}