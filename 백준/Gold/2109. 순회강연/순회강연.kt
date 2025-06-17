fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val c = MutableList(10000) { 0 }
    val lec = Array(n) { readLine().split(" ").map { it.toInt() } }
        .sortedWith(compareBy({ -it[0] }, { -it[1] }))
    for (l in lec) for (i in l[1] - 1 downTo 0) if (c[i] == 0) { c[i] = l[0]; break }
    println(c.sum())
    close()
}
