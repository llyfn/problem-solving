import kotlin.math.min

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val map = Array(n) { IntArray(n) }
    for (i in 0 until n) map[i] = readLine().split(" ").map { it.toInt() }.toIntArray()
    val visited = BooleanArray(n)
    var minExpense = Int.MAX_VALUE

    fun travelingSalesman(start: Int, lastVisited: Int = start, expense: Int = 0, depth: Int = 0) {
        if (depth == n - 1) {
            if (map[lastVisited][start] > 0) minExpense = min(minExpense, expense + map[lastVisited][start])
            return
        }

        for (i in 0 until n) {
            if (!visited[i] && map[lastVisited][i] > 0) {
                visited[i] = true
                travelingSalesman(start, i, expense + map[lastVisited][i], depth + 1)
                visited[i] = false
            }
        }
    }

    for (i in 0 until n) {
        visited[i] = true
        travelingSalesman(i)
        visited[i] = false
    }
    println(minExpense)
    close()
}
