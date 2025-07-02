import kotlin.math.abs

fun main() = with(System.`in`.bufferedReader()) {
    val (n, m) = readLine().split(" ").map { it.toInt() }
    val min = Array(n + 1) { DoubleArray(n + 1) { Double.MAX_VALUE } }
    val max = Array(n + 1) { DoubleArray(n + 1) { 0.0 } }
    var ans = Double.MAX_VALUE
    repeat(m) {
        val (a, b, c) = readLine().split(" ").map { it.toInt() }
        min[a][b] = minOf(min[a][b], c.toDouble())
        min[b][a] = minOf(min[b][a], c.toDouble())
        max[a][b] = maxOf(max[a][b], c.toDouble())
        max[b][a] = maxOf(max[b][a], c.toDouble())
    }
    for (i in 1..n) for (j in 1..n - 1) for (k in j + 1..n) {
        if (i == j || i == k) continue
        if (min[j][k] > min[j][i] + min[i][k]) {
            min[j][k] = min[j][i] + min[i][k]
            min[k][j] = min[j][i] + min[i][k]
        }
    }
    for (i in 1..n) {
        min[i][i] = 0.0
        var r = 0.0
        for (j in 1..n) for (k in j..n) {
            if (max[j][k] == 0.0) continue
            r = maxOf(r, min[i][j], min[i][k])
            if (abs(min[i][j] - min[i][k]) != max[j][k])
                r = maxOf(r, maxOf(min[i][j], min[i][k]) + (max[j][k] - abs(min[i][j] - min[i][k])) / 2)
        }
        ans = minOf(ans, r)
    }
    println(ans)
    close()
}