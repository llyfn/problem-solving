import kotlin.math.*

fun main() = with(System.`in`.bufferedReader()) {
    val (x, y, d, t) = readLine().split(" ").map { it.toDouble() }
    val dist = sqrt(x * x + y * y)
    var r = abs(dist - d)
    var ans = minOf(dist, r + t)
    for (i in 2..100000) {
        r -= d
        if (r <= 0) { ans = minOf(ans, t * i); break }
        ans = minOf(ans, r + t * i)
    }
    println(ans)
    close()
}