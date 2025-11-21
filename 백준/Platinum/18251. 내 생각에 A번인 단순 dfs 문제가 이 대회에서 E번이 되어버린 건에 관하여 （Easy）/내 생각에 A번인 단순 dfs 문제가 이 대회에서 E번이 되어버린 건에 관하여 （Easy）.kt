import kotlin.math.max

data class Node(val v: Int, val h: Int)
fun main() {
    val n = readln().toInt()
    val bt = readln().split(" ").map { it.toInt() }
    val nodes = ArrayList<Node>(n)
    fun dfs(i: Int, h: Int) {
        if (i > n) return
        dfs(i * 2, h + 1)
        nodes.add(Node(bt[i - 1], h))
        dfs(i * 2 + 1, h + 1)
    }
    dfs(1, 1)
    val h = nodes.maxOf { it.h }
    var m = Long.MIN_VALUE
    for (i in 1..h) for (j in i..h) {
        var c = 0L
        nodes.asSequence().filter { it.h in i..j }.map { it.v }.forEach {
            c = max(it.toLong(), c + it)
            m = max(m, c)
        }
    }
    println(m)
}