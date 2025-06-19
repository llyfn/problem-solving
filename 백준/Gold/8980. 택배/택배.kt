fun main() = with(System.`in`.bufferedReader()) {
    val (n, c) = readLine().split(" ").map { it.toInt() }
    val ds = List(readLine().toInt()) { readLine().split(" ").map { it.toInt() } }
    val cap = MutableList(n) { c }
    var cnt = 0
    for ((s, d, c) in ds.sortedBy({ it[1] })) {
        val m = cap.subList(s, d).min().coerceAtMost(c)
        for (i in s..<d) { cap[i] -= m }
        cnt += m
    }
    println(cnt)
    close()
}
