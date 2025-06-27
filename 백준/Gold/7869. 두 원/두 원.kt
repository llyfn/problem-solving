import kotlin.math.*

operator fun <T> List<T>.component6() = this[5]
fun main() = with(System.`in`.bufferedReader()) {
    val (x1, y1, r1, x2, y2, r2) = readLine().split(" ").map { it.toDouble() }
    val dist = hypot(x1 - x2, y1 - y2)
    val result = when {
        dist >= r1 + r2 -> 0.0
        dist <= abs(r1 - r2) -> PI * minOf(r1, r2).pow(2)
        else -> {
            val t1 = acos((r1 * r1 - r2 * r2 + dist * dist) / (2 * r1 * dist))
            val t2 = acos((r2 * r2 - r1 * r1 + dist * dist) / (2 * r2 * dist))
            r1 * r1 * t1 + r2 * r2 * t2 - r1 * r1 * sin(2 * t1) / 2 - r2 * r2 * sin(2 * t2) / 2
        }
    }
    println(String.format("%.3f", result))
    close()
}