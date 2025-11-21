fun main() {
    val (m, p) = readln().split(" ").map { it.toInt() }
    val n = 2 * m
    val graph = Array(n) { mutableListOf<Int>() }
    val cap = Array(n) { IntArray(n) }
    val flow = Array(n) { IntArray(n) }
    for (i in 0..<m) {
        cap[i * 2][i * 2 + 1] = 1
        graph[i * 2] += i * 2 + 1
        graph[i * 2 + 1] += i * 2
    }
    repeat(p) {
        val (u, v) = readln().split(" ").map { 2 * it.toInt() - 2 }
        cap[u + 1][v] = 1
        cap[v + 1][u] = 1
        graph[u] += v + 1
        graph[v] += u + 1
        graph[u + 1] += v
        graph[v + 1] += u
    }
    generateSequence {
        val par = IntArray(n) { -1 }.apply { set(1, 0) }
        val queue = ArrayDeque<Int>().apply { add(1) }
        while (queue.isNotEmpty()) {
            val u = queue.removeFirst()
            if (u == 2) break
            graph[u].forEach { v ->
                 if (par[v] < 0 && cap[u][v] > flow[u][v]) {
                     par[v] = u
                     queue.add(v)
                 }
            }
        }
        par.takeIf { it[2] != -1 }
    }.forEach { p ->
        var u = 2
        while (u != 0) {
            val v = p[u]
            flow[v][u]++
            flow[u][v]--
            u = v
        }

    }
    print(flow.sumOf { it[2] })
}