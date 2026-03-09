import java.io.StreamTokenizer

fun main() = with(StreamTokenizer(System.`in`.bufferedReader())) {
    val nextInt = { nextToken(); nval.toInt() }
    val n = nextInt()
    val sb = StringBuilder()
    sb.append((1 shl n) - 1).append("\n")
    fun solve(num: Int, from: Int, by: Int, to: Int) {
        if (num == 1) sb.append(from).append(" ").append(to).append("\n")
        else {
            solve(num - 1, from, to, by)
            sb.append(from).append(" ").append(to).append("\n")
            solve(num - 1, by, from, to)
        }
    }
    solve(n, 1, 2, 3)
    print(sb)
}
