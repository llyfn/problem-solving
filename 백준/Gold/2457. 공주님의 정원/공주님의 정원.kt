import java.time.LocalDate

fun main() = with(System.`in`.bufferedReader()) {
    val doy = { m: Int, d: Int -> LocalDate.of(2025, m, d).dayOfYear }
    val n = readLine().toInt()
    val fs = Array(n) { readLine().split(" ").map { it.toInt() }.let { (a, b, c, d) -> doy(a, b) to doy(c, d) } }
        .sortedWith(compareBy({ it.first }, { it.second }))
    val end = doy(12, 1)
    var curr = doy(3, 1)
    var idx = 0
    var cnt = 0
    while (curr < end) {
        var max = -1
        while (idx < n && fs[idx].first <= curr) { max = maxOf(max, fs[idx].second); idx++ }
        if (max <= curr) { println(0); return }
        curr = max; cnt++
    }
    println(if (curr < end) 0 else cnt)
    close()
}
