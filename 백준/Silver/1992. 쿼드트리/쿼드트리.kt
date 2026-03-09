fun main() {
    val n = readln().toInt()
    val arr = Array(n + 1) { IntArray(n + 1) }
    for (i in 1..n) {
        val ln = readln()
        for (j in 1..n) arr[i][j] = ln[j - 1] - '0' + arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]
    }
    fun qt(r: Int, c: Int, s: Int): String =
        when (arr[r + s][c + s] - arr[r + s][c] - arr[r][c + s] + arr[r][c]) {
            0 -> "0"
            s * s -> "1"
            else -> "(" + qt(r, c, s / 2) + qt(r, c + s / 2, s / 2) + qt(r + s / 2, c, s / 2) + qt(r + s / 2, c + s / 2, s / 2) + ")"
        }
    print(qt(0, 0, n))
}
