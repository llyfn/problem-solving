fun main() {
    val (n, m) = readln().split(' ').map { it.toInt() }
    val edges = Array(n + 1) { ArrayList<Pair<Int, Long>>() }
    repeat(m) {
        val (a, b, c) = readln().split(' ').map { it.toInt() }
        edges[a] += b to c.toLong()
    }
    val dist = LongArray(n + 1) { Long.MAX_VALUE }.apply { set(1, 0) }
    val inq = BooleanArray(n + 1).apply { set(1, true) }
    val cnt = IntArray(n + 1).apply { set(1, 1) }
    val queue = ArrayDeque<Int>().apply { add(1) }
    while (queue.isNotEmpty()) {
        val u = queue.removeFirst().also { inq[it] = false}
        for ((v, c) in edges[u]) {
            if (dist[v] > dist[u] + c) {
                dist[v] = dist[u] + c
                if (!inq[v]) {
                    if (++cnt[v] >= n) return println(-1)
                    inq[v] = true
                    queue.add(v)
                }
            }
        }
    }
    dist.drop(2).forEach { println(if (it < Long.MAX_VALUE) it else -1) }
}