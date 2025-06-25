fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val tree = mutableMapOf<Int, MutableList<Int>>()
    val nodes = readLine().split(" ").map { it.toInt() }
    for (i in 1..<n) tree.getOrPut(nodes[i]) { mutableListOf() }.add(i)
    fun dfs(node: Int): Int {
        val r = tree[node]?.map { dfs(it) } ?: return 0
        return r.sortedDescending().mapIndexed { idx, i -> i + idx + 1}.max()
    }
    println(dfs(0))
    close()
}