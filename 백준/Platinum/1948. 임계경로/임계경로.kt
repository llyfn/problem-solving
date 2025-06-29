import kotlin.math.*

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val m = readLine().toInt()
    val graph = Array(n + 1) { mutableListOf<Pair<Int, Int>>() }
    val degree = Array(n + 1) { 0 }
    val revGraph = Array(n + 1) { mutableListOf<Pair<Int, Int>>() }
    val revDegree = Array(n + 1) { 0 }
    val cost = Array(n + 1) { 0L }
    val revCost = Array(n + 1) { 0L }
    repeat(m) {
        val (u, v, w) = readLine().split(" ").map { it.toInt() }
        graph[u].add(v to w); degree[v]++
        revGraph[v].add(u to w); revDegree[u]++
    }
    fun topoSort(g: Array<MutableList<Pair<Int, Int>>>, deg: Array<Int>, c: Array<Long>, src: Int) {
        val queue = ArrayDeque<Pair<Int, Boolean>>()
        for (i in 1..n) if (deg[i] == 0) queue.add(i to (i == src))
        while (queue.isNotEmpty()) {
            val (curr, isSrc) = queue.removeFirst()
            for ((next, w) in g[curr]) {
                if (isSrc) c[next] = max(c[next], c[curr] + w)
                deg[next]--
                if (deg[next] == 0) queue.add(next to (next == src || isSrc || c[next] > 0))
            }
        }
    }
    val (s, e) = readLine().split(" ").map { it.toInt() }
    topoSort(graph, degree, cost, s)
    println(cost[e])
    topoSort(revGraph, revDegree, revCost, e)
    val nq = ArrayDeque(listOf(s))
    val visited = BooleanArray(n + 1) { false }
    var cnt = 0
    while (nq.isNotEmpty()) {
        val curr = nq.removeFirst()
        for ((next, w) in graph[curr]) {
            if (cost[curr] + w + revCost[next] == cost[e]) cnt++
            if (!visited[next]) {
                visited[next] = true
                nq.add(next)
            }
        }
    }
    println(cnt)
    close()
}