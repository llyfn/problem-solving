class DisjointSet(val n: Int) {
    val parent = IntArray(n) { it }
    val dist = IntArray(n) { 0 }
    fun find(x: Int): Int {
        if (parent[x] != x) {
            val p = find(parent[x])
            dist[x] += dist[parent[x]]
            parent[x] = p
        }
        return parent[x]
    }
    fun union(x: Int, y: Int, d: Int) {
        val px = find(x)
        val py = find(y)
        if (px != py) {
            parent[px] = py
            dist[px] = dist[y] - dist[x] + d
        }
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val out = StringBuilder()
    while (true) {
        val (n, m) = readLine().split(" ").map { it.toInt() }
        if (n == 0 && m == 0) break
        val ds = DisjointSet(n)
        repeat(m) {
            val input = readLine().split(" ")
            if (input[0] == "!") {
                val (x, y, d) = input.drop(1).map { it.toInt() }
                ds.union(x - 1, y - 1, d)
            } else {
                val (x, y) = input.drop(1).map { it.toInt() }
                out.appendLine(if (ds.find(x - 1) == ds.find(y - 1)) ds.dist[x - 1] - ds.dist[y - 1]  else "UNKNOWN")
            }
        }
    }
    print(out)
}