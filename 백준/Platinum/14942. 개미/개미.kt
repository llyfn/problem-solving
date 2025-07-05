fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val a = List(n) { readLine().toInt() }
    val edges = hashMapOf<Int, MutableList<Pair<Int, Int>>>()
    repeat(n - 1) {
        val (u, v, w) = readLine().split(" ").map { it.toInt() }
        edges.getOrPut(u - 1) { mutableListOf() }.add(v - 1 to w)
        edges.getOrPut(v - 1) { mutableListOf() }.add(u - 1 to w)
    }
    val visited = BooleanArray(n) { false }
    val parents = Array(n) { Array(16) { 0 to 0 } }
    val res = IntArray(n) { 0 }
    visited[0] = true

    fun dfs(node: Int) {
        for ((next, weight) in edges[node]!!) {
            if (!visited[next]) {
                visited[next] = true
                parents[next][0] = node to weight
                dfs(next)
            }
        }
    }

    fun search(idx: Int, node: Int, left: Int) {
        if (node == 0) {
            res[idx] = node + 1
            return
        }
        for (d in 15 downTo 0) {
            val (par, w) = parents[node][d]
            if (w <= left) {
                search(idx, par, left - w)
                return
            }
            res[idx] = node + 1
        }
    }

    dfs(0)
    for (d in 1..15) for (i in 0..<n) {
        val (par, w) = parents[i][d - 1]
        val (gp, gw) = parents[par][d - 1]
        parents[i][d] = gp to gw + w
    }
    for (i in 0..<n) search(i, i, a[i])
    res.forEach { println(it) }
}