fun main() = with(System.`in`.bufferedReader()) {
    val (t, n, d) = readLine().split(" ").map { it.toInt() }
    if (d == 0) { eye(n).print(); return }
    val mod = 1_000_000_007L
    val graphs = List(t) { Array(n) { LongArray(n) } }
    repeat(t) { i ->
        repeat(readLine().toInt()) {
            val (u, v, w) = readLine().split(" ").map { it.toInt() }
            graphs[i][u - 1][v - 1] = w.toLong()
        }
    }
    val rem = graphs.subList(0, d % t).fold(eye(n)) { acc, g -> matMul(acc, g, mod) }
    val res = graphs.subList(d % t, t).fold(rem) { acc, g -> matMul(acc, g, mod) }
    matMul(matPow(res, d / t, mod), rem, mod).print()
}
fun eye(n: Int) = Array(n) { i -> LongArray(n) { j -> if (i == j) 1L else 0L } }
fun matMul(a: Array<LongArray>, b: Array<LongArray>, mod: Long) =
    Array(a.size) { i -> LongArray(b[0].size) { j -> a[0].indices.fold(0L) { acc, k -> (acc + a[i][k] * b[k][j]) % mod } } }
fun matPow(a: Array<LongArray>, e: Int, mod: Long): Array<LongArray> {
    if (e == 0) return eye(a.size)
    if (e == 1) return a
    val sq = matPow(a, e / 2, mod).let { matMul(it, it, mod) }
    return if (e % 2 == 0) sq else matMul(sq, a, mod)
}
fun Array<LongArray>.print() = forEach { println(it.joinToString(" ")) }