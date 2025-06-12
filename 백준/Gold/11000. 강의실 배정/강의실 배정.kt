import java.util.PriorityQueue

fun main() = with(System.`in`.bufferedReader()) {
    val lec = (1..readLine().toInt())
        .map { readLine().split(" ").let { it[0].toInt() to it[1].toInt() } }
        .sortedWith(compareBy({ it.first }, { it.second }))
    val pq = PriorityQueue(listOf(lec[0].second))
    for ((s, e) in lec.drop(1)) {
        if (pq.peek() <= s) pq.poll()
        pq.add(e)
    }
    println(pq.size)

    close()
}