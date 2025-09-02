import java.util.StringTokenizer

class FenwickTree(val n: Int) {
    private val tree = LongArray(n + 1)
    fun add(i: Int, d: Long) {
        var x = i
        while (x <= n) { tree[x] += d; x += x and -x }
    }
    fun sum(i: Int): Long {
        var x = i
        var r = 0L
        while (x > 0) { r += tree[x]; x -= x and -x }
        return r
    }
}
fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val tree = FenwickTree(n)
    val seq = readLine().split(" ").map { it.toLong() }.toLongArray()
    for (i in seq.indices) tree.add(i + 1, seq[i])
    val u = mutableListOf<IntArray>()
    val q = mutableListOf<IntArray>()
    repeat(readLine().toInt()) {
        val c = readLine().split(" ").map { it.toInt() }
        if (c[0] == 1) u.add(intArrayOf(c[1], c[2]))
        else q.add(intArrayOf(c[1], c[2], c[3], q.size))
    }
    q.sortBy { it[0] }
    val result = LongArray(q.size)
    var l = 0
    for ((k, i, j, idx) in q) {
        while (l < k) {
            val d = u[l][1] - seq[u[l][0] - 1]
            seq[u[l][0] - 1] += d
            tree.add(u[l][0], d)
            l++
        }
        result[idx] = tree.sum(j) - tree.sum(i - 1)
    }
    println(result.joinToString("\n"))
}