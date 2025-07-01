fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val a = readLine().split(" ").map { it.toInt() }
    val b = readLine().split(" ").map { it.toInt() }.withIndex().associate { (i, v) -> v to i + 1 }
    val segTree = LongArray(4 * n) { 0L }
    var ans = 0L
    fun sum(s: Int, e: Int, n: Int, l: Int, r: Int): Long {
        if (s > r || e < l) return 0L
        if (s >= l && e <= r) return segTree[n]
        val mid = (s + e) / 2
        return sum(s, mid, n * 2, l, r) + sum(mid + 1, e, n * 2 + 1, l, r)
    }
    fun update(s: Int, e: Int, n: Int, idx: Int, diff: Long) {
        if (s > idx || e < idx) return
        segTree[n] += diff
        if (s == e) return
        val mid = (s + e) / 2
        update(s, mid, n * 2, idx, diff)
        update(mid + 1, e, n * 2 + 1, idx, diff)
    }
    for (i in a) {
        ans += sum(1, n, 1, b[i]!! + 1, n)
        update(1, n, 1, b[i]!!, 1L)
    }
    println(ans)
    close()
}