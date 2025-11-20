fun main() {
    val (n, p) = readln().split(" ").map { it.toInt() }
    val graph = Array(n) { mutableListOf<Int>() }
    val cap = Array(n) { IntArray(n) }
    val flow = Array(n) { IntArray(n) }
    repeat(p) {
        val (u, v) = readln().split(" ").map { it.toInt() - 1 }
        cap[u][v] = 1
        graph[u] += v
        graph[v] += u
    }
    generateSequence {
        val par = IntArray(n) { -1 }.apply { set(0, 0) }
        val queue = ArrayDeque<Int>().apply { add(0) }
        while (queue.isNotEmpty()) {
            val u = queue.removeFirst()
            if (u == 1) break
            graph[u].forEach { v ->
                 if (par[v] < 0 && cap[u][v] > flow[u][v]) {
                     par[v] = u
                     queue.add(v)
                 }
            }
        }
        par.takeIf { it[1] != -1 }
    }.forEach { p ->
        var u = 1
        while (u != 0) {
            val v = p[u]
            flow[v][u]++
            flow[u][v]--
            u = v
        }

    }
    print(flow.sumOf { it[1] })
}