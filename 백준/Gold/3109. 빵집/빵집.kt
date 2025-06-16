fun main() = with(System.`in`.bufferedReader()) {
    val (r, c) = readLine().split(" ").map { it.toInt() }
    val map = Array(r) { readLine().toCharArray() }
    var count = 0
    fun dfs(x: Int, y: Int): Boolean {
        map[x][y] = 'p'
        if (y == c - 1) {
            count += 1
            return true
        }
        for (dx in -1..1) {
            val nx = x + dx
            val ny = y + 1
            if (nx in 0..<r && ny in 0..<c && map[nx][ny] == '.') {
                if (dfs(nx, ny)) return true
            }
        }
        return false
    }
    for (i in 0..<r) dfs(i, 0)
    println(count)
    close()
}
