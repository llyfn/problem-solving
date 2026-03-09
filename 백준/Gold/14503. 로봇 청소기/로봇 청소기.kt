import java.io.StreamTokenizer

fun main() = with(StreamTokenizer(System.`in`.bufferedReader())) {
    val nextInt = { nextToken(); nval.toInt() }
    val (n, m) = nextInt() to nextInt()
    var (r, c, d) = listOf(nextInt(), nextInt(), nextInt())
    val dr = listOf(-1, 0, 1, 0)
    val dc = listOf(0, 1, 0, -1)
    val map = Array(n) { IntArray(m) { nextInt() } }
    var ans = 0
    while (true) {
        if (map[r][c] == 0) {
            map[r][c] = -1
            ans += 1
        }
        var moved = false
        for (i in 0..3) {
            d = (d + 3) % 4
            val (nr, nc) = r + dr[d] to c + dc[d]
            if (map[nr][nc] == 0) {
                r = nr
                c = nc
                moved = true
                break
            }
        }
        if (!moved) {
            val (nr, nc) = r - dr[d] to c - dc[d]
            if (map[nr][nc] == 1) break else { r = nr; c = nc }
        }
    }
    println(ans)
}
