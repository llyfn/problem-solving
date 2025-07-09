class FenwickTree(val n: Int) {
    private val tree = IntArray(n + 1)
    fun add(i: Int, d: Int) {
        var x = i
        while (x <= n) { tree[x] += d; x += x and -x }
    }
    fun sum(i: Int): Int {
        var x = i
        var r = 0
        while (x > 0) { r += tree[x]; x -= x and -x }
        return r
    }
}
fun main() = with(System.`in`.bufferedReader()) {
    val out = System.out.bufferedWriter()
    repeat(readLine().toInt()) {
        val (n, m) = readLine().split(" ").map { it.toInt() }
        val q = readLine().split(" ").map { it.toInt() }
        val pos = IntArray(n + 1) { -1 }
        val bit = FenwickTree(n + m)
        for (i in 1..n) {
            pos[i] = m + i
            bit.add(m + i, 1)
        }
        var curr = m
        for (x in q) {
            val s = bit.sum(pos[x] - 1)
            out.write("$s ")
            bit.add(pos[x], -1)
            bit.add(curr, 1)
            pos[x] = curr--
        }
        out.newLine()
    }
    out.flush()
}