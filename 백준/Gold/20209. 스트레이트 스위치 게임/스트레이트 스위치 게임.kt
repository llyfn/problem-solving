fun main() = with(System.`in`.bufferedReader()) {
    val (_, k) = readLine().split(' ').map { it.toInt() }
    val a = readLine().split(' ').map { it.toInt() }
    val b = Array(k) { readLine().split(' ').map { it.toInt() - 1 }.drop(1) }
    val q = ArrayDeque<Pair<List<Int>, Int>>()
    val v = mutableSetOf<List<Int>>()
    q.add(a to 0)
    v.add(a)
    while (q.any()) {
        val (c, d) = q.removeFirst()
        if (c.all { it == c[0] }) { println(d); return }
        for (i in 0..<k) {
            val n = c.toMutableList()
            for (j in b[i]) n[j] = (n[j] + i + 1) % 5
            if (v.add(n)) q.add(n to d + 1)
        }
    }
    println(-1)
}