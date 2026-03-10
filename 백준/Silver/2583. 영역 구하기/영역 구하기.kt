import java.io.StreamTokenizer
import kotlin.collections.ArrayDeque

fun main() = with(StreamTokenizer(System.`in`.bufferedReader())) {
    val nextInt = { nextToken(); nval.toInt() }
    val m = nextInt()
    val n = nextInt()
    val k = nextInt()
    val d = listOf(0 to 1, 0 to -1, 1 to 0, -1 to 0)
    val map = Array(n) { IntArray(m) }
    repeat(k) {
        val (x1, y1, x2, y2) = listOf(nextInt(), nextInt(), nextInt(), nextInt())
        for (i in x1..<x2) for (j in y1..<y2) map[i][j] = 1
    }
    val ans = mutableListOf<Int>()
    for (i in 0..<n) for (j in 0..<m) if (map[i][j] == 0) {
        var area = 1
        val q = ArrayDeque<Pair<Int, Int>>().apply { add(i to j) }
        map[i][j] = 1
        while (q.isNotEmpty()) {
            val (x, y) = q.removeFirst()
            for ((dx, dy) in d) {
                val (nx, ny) = x + dx to y + dy
                if (nx in 0..<n && ny in 0..<m && map[nx][ny] == 0) {
                    map[nx][ny] = 1
                    area += 1
                    q.add(nx to ny)
                }
            }
        }
        ans += area
    }
    println(ans.size)
    println(ans.sorted().joinToString(" "))
}