import java.util.PriorityQueue

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val gas = List(n) { readLine().split(" ").map { it.toInt() } }.sortedWith(compareBy({ it[0] }, { -it[1] }))
    var (l, p) = readLine().split(" ").map { it.toInt() }
    val q = PriorityQueue<Int>(compareByDescending { it })
    var cnt = 0
    for ((a, b) in gas + listOf(listOf(l, 0))) {
        if (p >= l) break
        while (p < a && q.isNotEmpty()) { p += q.poll(); cnt++ }
        if (p < a) break
        q.add(b)
    }
    println(if (p >= l) cnt else -1)
    close()
}
