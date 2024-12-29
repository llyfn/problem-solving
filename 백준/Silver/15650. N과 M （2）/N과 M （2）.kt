import java.io.BufferedWriter

fun main() = with(System.`in`.bufferedReader()) {
    val input = readLine().split(' ').map { it.toInt() }
    val bw = System.`out`.bufferedWriter()

    val n = input[0]
    val m = input[1]
    val visited = BooleanArray (n + 1) { false }

    dfs2("", visited, n, m, bw)

    bw.flush()
}

fun dfs2(sequence: String, visited: BooleanArray, n: Int, m: Int, bw: BufferedWriter) {
    if (n < 1 || m < 1 || n > 9 || m > 9) return

    val len = sequence.length
    if (len > 1 && sequence[len-1] < sequence[len-2]) return
    if (len >= m) {
        sequence.forEach { bw.write("$it ") }
        bw.write("\n")
        return
    }

    for (i in 1..n) {
        if (visited[i]) continue
        else {
            visited[i] = true
            dfs2(sequence + "$i", visited, n, m, bw)
            visited[i] = false
        }
    }
}
