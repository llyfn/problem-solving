class TwoSAT(val n: Int) {
    private val graph = Array(n * 2 + 1) { mutableListOf<Int>() }
    private val par = IntArray(n * 2 + 1)
    private val cnf = IntArray(n * 2 + 1)
    private val visit = BooleanArray(n * 2 + 1)
    private var scc = 0
    private var cnt = 0
    private val stack = mutableListOf<Int>()
    fun addEdge(u: Int, v: Int) { graph[node(-u)].add(node(v)) }
    fun solve(): Boolean {
        for (i in 1..n * 2) if (par[i] == 0) dfs(i)
        for (i in 1..n) if (cnf[i] == cnf[n + i]) return false
        return true
    }
    private fun node(v: Int) = if (0 < v && v <= n) v else n - v
    private fun dfs(v: Int): Int {
        par[v] = ++cnt
        stack.add(v)
        var res = par[v]
        for (u in graph[v]) {
            if (par[u] == 0) res = minOf(res, dfs(u))
            else if (!visit[u]) res = minOf(res, par[u])
        }
        if (res == par[v]) {
            while (stack.isNotEmpty()) {
                val top = stack.removeLast()
                cnf[top] = scc
                visit[top] = true
                if (top == v) break
            }
            scc++
        }
        return res
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    while (true) {
        val (n, m) = readLine()?.split(" ")?.map { it.toInt() } ?: break
        val ts = TwoSAT(n)
        ts.addEdge(1, 1)
        repeat(m) {
            val (u, v) = readLine().split(" ").map { it.toInt() }
            ts.addEdge(u, v)
            ts.addEdge(v, u)
        }
        println(if (ts.solve()) "yes" else "no")
    }

}