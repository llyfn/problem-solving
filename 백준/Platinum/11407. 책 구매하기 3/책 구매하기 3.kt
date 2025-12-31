import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val (n, m) = nextInt() to nextInt()
    val graph = Array(n + m + 2) { mutableListOf<Int>() }
    val cap = Array(n + m + 2) { IntArray(n + m + 2) }
    val flow = Array(n + m + 2) { IntArray(n + m + 2) }
    val cost = Array(n + m + 2) { IntArray(n + m + 2) }
    fun addEdge(u: Int, v: Int, w: Int) { graph[u] += v; graph[v] += u; cap[u][v] = w }
    fun setCost(u: Int, v: Int, c: Int) { cost[u][v] = c; cost[v][u] = -c }
    (1..n).forEach { addEdge(0, it, nextInt()) }
    (n + 1..n + m).forEach { addEdge(it, n + m + 1, nextInt()) }
    for (i in 1..m) for (j in 1..n) addEdge(j, n + i, nextInt())
    for (i in 1..m) for (j in 1..n) setCost(j, n + i, nextInt())
    var (tf, tc) = 0 to 0
    while (true) {
        val par = IntArray(n + m + 2)
        val dist = IntArray(n + m + 2) { Int.MAX_VALUE }.apply { set(0, 0) }
        val queue = ArrayDeque<Int>().apply { add(0) }
        val inq = BooleanArray(n + m + 2).apply { set(0, true) }
        while (queue.isNotEmpty()) {
            val u = queue.removeFirst().also { inq[it] = false }
            for (v in graph[u]) if (cap[u][v] > flow[u][v] && dist[v] > dist[u] + cost[u][v]) {
                dist[v] = dist[u] + cost[u][v]; par[v] = u
                if (!inq[v]) { inq[v] = true; queue.add(v) }
            }
        }
        if (dist[n + m + 1] == Int.MAX_VALUE) break
        var p = Int.MAX_VALUE
        var u = n + m + 1
        while (u > 0) {
            p = minOf(p, cap[par[u]][u] - flow[par[u]][u])
            u = par[u]
        }
        tf += p
        u = n + m + 1
        while (u > 0) {
            flow[par[u]][u] += p
            flow[u][par[u]] -= p
            tc += p * cost[par[u]][u]
            u = par[u]
        }
    }
    print("$tf\n$tc")
}