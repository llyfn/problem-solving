fun main() = with(System.`in`.bufferedReader()) {
    val input = readLine().split(' ').map { it.toInt() }
    val sb = StringBuilder()

    val n = input[0]
    val m = input[1]


    dfs4("", n, m, sb)
    print(sb)
}

fun dfs4(sequence: String, n: Int, m: Int, sb: StringBuilder) {
    if (n < 1 || m < 1 || n > 9 || m > 9) return

    val len = sequence.length
    if (len > 1 && sequence[len-1] < sequence[len-2]) return
    if (len >= m) {
        sequence.forEach { sb.append("$it ") }
        sb.append("\n")
        return
    }

    for (i in 1..n) dfs4(sequence + "$i", n, m, sb)
}
