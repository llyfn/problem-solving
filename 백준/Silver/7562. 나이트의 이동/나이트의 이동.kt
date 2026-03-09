import java.io.StreamTokenizer

fun main() = with(StreamTokenizer(System.`in`.bufferedReader())) {
    val nextInt = { nextToken(); nval.toInt() }
    val d = listOf(1 to 2, 1 to -2, -1 to 2, -1 to -2, 2 to 1, 2 to -1, -2 to 1, -2 to -1)
    repeat(nextInt()) { _ ->
        val n = nextInt()
        val visited = Array(n) { BooleanArray(n) }
        val (xs, ys, xe, ye) = listOf(nextInt(), nextInt(), nextInt(), nextInt())
        val queue = ArrayDeque(listOf(listOf(0, xs, ys)))
        while (queue.isNotEmpty()) {
            val (c, x, y) = queue.removeFirst()
            if (x == xe && y == ye) {
                println(c)
                break
            }
            for ((dx, dy) in d) {
                val (nx, ny) = x + dx to y + dy
                if (nx in 0..<n && ny in 0..<n && !visited[nx][ny]) {
                    visited[nx][ny] = true
                    queue.add(listOf(c + 1, nx, ny))
                }
            }
        }
    }

}
