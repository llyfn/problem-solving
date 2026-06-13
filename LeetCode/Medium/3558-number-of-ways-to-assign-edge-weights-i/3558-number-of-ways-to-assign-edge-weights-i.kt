class Solution {
    fun assignEdgeWeights(edges: Array<IntArray>): Int {
        var max = 0
        val graph = Array(edges.size + 2) { mutableListOf<Int>() }
        for ((v, w) in edges) {
            graph[v] += w
            graph[w] += v
        }
        val visited = BooleanArray(edges.size + 2)
        fun dfs(v: Int, d: Int) {
            visited[v] = true
            max = maxOf(max, d)
            for (w in graph[v]) if (!visited[w]) dfs(w, d + 1)
        }
        dfs(1, 0)
        return 2.toBigInteger().modPow((max - 1).toBigInteger(), 1000000007.toBigInteger()).toInt()
    }
}