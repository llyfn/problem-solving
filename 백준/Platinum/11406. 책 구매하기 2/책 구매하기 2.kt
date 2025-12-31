import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val (n, m) = nextInt() to nextInt()
    val graph = Array(n + m + 2) { mutableListOf<Int>() }
    val cap = Array(n + m + 2) { IntArray(n + m + 2) }
    val flow = Array(n + m + 2) { IntArray(n + m + 2) }
    fun addEdge(u: Int, v: Int, w: Int) { graph[u] += v; graph[v] += u; cap[u][v] = w }
    (1..n).forEach { addEdge(0, it, nextInt()) }
    (n + 1..n + m).forEach { addEdge(it, n + m + 1, nextInt()) }
    for (i in 1..m) for (j in 1..n) addEdge(j, n + i, nextInt())
    var tf = 0
    while (true) {
        val par = IntArray(n + m + 2) { -1 }
        val queue = ArrayDeque<Int>().apply { add(0) }
        while (queue.isNotEmpty()) {
            val u = queue.removeFirst()
            for (v in graph[u]) if (cap[u][v] > flow[u][v] && par[v] == -1) { par[v] = u; queue.add(v) }
        }
        if (par[n + m + 1] == -1) break
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
            u = par[u]
        }
    }
    print(tf)
}