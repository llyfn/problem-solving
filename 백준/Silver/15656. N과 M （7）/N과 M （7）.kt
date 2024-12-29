fun main() = with(System.`in`.bufferedReader()) {
    val input = readLine().split(' ').map { it.toInt() }
    val arr = readLine().split(' ').map { it.toInt() }.sorted()
    val n = input[0]
    val m = input[1]
    val sb = StringBuilder()

    dfs7(IntArray(m) { 0 }, arr, n, m, sb)
    print(sb)
}

fun dfs7(sequence: IntArray, arr: List<Int>, n: Int, m: Int, sb: StringBuilder, depth: Int = 0) {
    if (n < 1 || m < 1 || n > 8 || m > 8) return
    if (depth >= m) {
        sequence.forEach { sb.append("$it ") }
        sb.append("\n")
        return
    }

    for (i in 0 until n) {
        sequence[depth] = arr[i]
        dfs7(sequence, arr, n, m, sb, depth + 1)
    }
}