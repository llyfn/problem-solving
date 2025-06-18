import java.util.PriorityQueue

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val ps = Array(n) { readLine().split(" ").map { it.toInt() } }
        .sortedWith(compareBy({ it[0] }, { it[1] }))
    val q = PriorityQueue<Int>()
    for ((d, c) in ps) {
        q.add(c)
        if (d < q.size) q.poll()
    }
    println(q.sum())
    close()
}
