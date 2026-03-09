import java.io.StreamTokenizer

fun main() = with(StreamTokenizer(System.`in`.bufferedReader())) {
    val nextInt = { nextToken(); nval.toInt() }
    val d = (-1..1).flatMap { r -> (-1..1).map { c -> r to c } }
    while (true) {
        val (w, h) = nextInt() to nextInt()
        if (w == 0) break
        val map = Array(h) { IntArray(w) { nextInt() } }
        var ans = 0
        for (i in 0..<h) for (j in 0..<w) if (map[i][j] == 1) {
            ans += 1
            val queue = ArrayDeque<Pair<Int, Int>>().apply { add(i to j) }
            map[i][j] = 0
            while (queue.isNotEmpty()) {
                val (r, c) = queue.removeFirst()
                for ((dr, dc) in d) {
                    val (nr, nc) = r + dr to c + dc
                    if (nr in 0..<h && nc in 0..<w && map[nr][nc] == 1) {
                        map[nr][nc] = 0
                        queue.add(nr to nc)
                    }
                }
            }
        }
        println(ans)
    }
}
