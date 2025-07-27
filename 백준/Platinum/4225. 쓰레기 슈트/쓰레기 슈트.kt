import kotlin.math.*

fun main() = with(System.`in`.bufferedReader()) {
    val out = StringBuilder()
    var tc = 0
    while (true) {
        tc++
        val n = readLine().toInt()
        if (n == 0) break
        root = Point(0.0,  10000.0)
        val ps = List(n) {
            val (x, y) = readLine().split(" ").map { it.toDouble() }
            if (y <= root.y) root = Point(x, y)
            Point(x, y)
        }.sorted()
        val hull = convexHull(ps)
        val min = (hull + hull.first()).windowed(2).minOf { (a, b) ->
            hull.filterNot { it == a || it == b }.maxOf { it.dist(a, b) }
        }
        out.appendLine("Case $tc: ${String.format("%.2f", ceil(min * 100) / 100)}")
    }
    print(out)
}

class Point(val x: Double, val y: Double): Comparable<Point> {
    fun deg() = acos((x - root.x) / dist(root))
    fun dist(p: Point) = hypot(x - p.x, y - p.y)
    fun dist(p1: Point, p2: Point) = abs((x - p1.x) * (p2.y - p1.y) - (y - p1.y) * (p2.x - p1.x)) / p1.dist(p2)
    fun ccw(b: Point, c: Point) = (b.x - x) * (c.y - b.y) - (b.y - y) * (c.x - b.x)
    override fun compareTo(other: Point): Int {
        val c = deg().compareTo(other.deg())
        return c.takeIf { it != 0 } ?: dist(root).compareTo(other.dist(root))
    }
}
var root = Point(0.0, 0.0)

fun convexHull(ps: List<Point>): List<Point> {
    val st = ps.take(2).toMutableList()
    for (i in 2..<ps.size) {
        while (st.size > 1 && st[st.size - 2].ccw(st.last(), ps[i]) < 0) st.removeLast()
        st.add(ps[i])
    }
    return st
}
