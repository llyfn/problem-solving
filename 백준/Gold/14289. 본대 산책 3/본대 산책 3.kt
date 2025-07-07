fun main() = with(System.`in`.bufferedReader()) {
    val (n, m) = readLine().split(" ").map { it.toInt() }
    val mod = 1_000_000_007L
    val start = Array(n) { LongArray(n) }
    start[0][0] = 1L
    val graph = Array(n) { LongArray(n) }
    repeat(m) {
        val (u, v) = readLine().split(" ").map { it.toInt() }
        graph[u - 1][v - 1] = 1
        graph[v - 1][u - 1] = 1
    }
    println(matMul(start, matPow(graph, readLine().toInt(), mod), mod)[0][0])
}
fun matMul(a: Array<LongArray>, b: Array<LongArray>, mod: Long) =
    Array(a.size) { i -> LongArray(b[0].size) { j -> a[0].indices.fold(0L) { acc, k -> (acc + a[i][k] * b[k][j]) % mod } } }
fun matPow(a: Array<LongArray>, e: Int, mod: Long): Array<LongArray> {
    if (e == 1) return a
    val sq = matPow(a, e / 2, mod).let { matMul(it, it, mod) }
    return if (e % 2 == 0) sq else matMul(sq, a, mod)
}