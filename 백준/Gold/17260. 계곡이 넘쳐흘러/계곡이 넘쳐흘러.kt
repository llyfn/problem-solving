val r = { readln().split(' ').map { it.toInt() } }
fun main() {
    val (n, k) = r()
    val h = r()
    val g = List(n - 1) { r() }.flatMap { listOf(it, it.reversed()) }.groupBy({ it[1] - 1 }, { it[0] - 1 })
    fun d(i: Int, j: Int, k: Int): Boolean = j < 1000001 && g[i]?.any { it != k && (h[it] >= j || d(it, 2 * j - h[it], i)) } ?: false
    print(if (d(k - 1, h[k - 1], -1)) 1 else 0)
}