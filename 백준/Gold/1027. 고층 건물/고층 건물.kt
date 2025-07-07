fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val l = readLine().split(" ").map { it.toDouble() }
    println(l.indices.maxOf { i ->
        l.indices.count { j ->
            val (i, j) = listOf(i, j).sorted()
            i != j && l.subList(i + 1, j).withIndex().all { (k, v) -> v < l[i] + (l[j] - l[i]) / (j - i) * (k + 1) }
        }
    })
}
