fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val visited = BooleanArray(n + 1)
    val sb = StringBuilder()

    fun permutation(sequence: String = "", depth: Int = 0) {
        if (depth == n) {
            sb.append(sequence + "\n")
            return
        }
        for (i in 1..n) {
            if (!visited[i]) {
                visited[i] = true
                permutation(sequence + "$i ", depth + 1)
                visited[i] = false
            }
        }
    }

    permutation()
    print(sb)
    close()
}
