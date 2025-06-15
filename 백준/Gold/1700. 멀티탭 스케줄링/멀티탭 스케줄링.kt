fun main() = with(System.`in`.bufferedReader()) {
    val (n, k) = readLine().split(" ").map { it.toInt() }
    val e = readLine().split(" ").map { it.toInt() }
    val set = mutableSetOf<Int>()
    var cnt = 0
    e.forEachIndexed { idx, v ->
        set.add(v)
        if (set.size > n) {
            cnt += 1
            var latest = 0
            var max = -1
            for (i in set) {
                var j = e.drop(idx).indexOf(i)
                if (j == -1) j = k
                if (j > max) {
                    latest = i
                    max = j
                }
            }
            set.remove(latest)
        }
    }
    println(cnt)
    close()
}
