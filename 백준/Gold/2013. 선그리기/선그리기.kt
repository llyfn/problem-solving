import kotlin.math.round

data class DisjointSet(val n: Int) {
    val parent = IntArray(n) { it }
    fun find(x: Int): Int {
        if (parent[x] != x) parent[x] = find(parent[x])
        return parent[x]
    }
    fun union(x: Int, y: Int) {
        val (px, py) = find(x) to find(y)
        if (px != py) parent[px] = py
    }
}
class Line(a: Point, b: Point) {
    val p = minOf(a, b)
    val q = maxOf(a, b)
    fun overwrap(other: Line): Boolean {
        if (p.ccw(q, other.p) != 0 || p.ccw(q, other.q) != 0) return false
        return (p <= other.q && other.p <= q)
    }
    operator fun plus(other: Line) = Line(minOf(p, other.p), maxOf(q, other.q))
    override fun toString(): String = "($p, $q)"

}
data class Point(val x: Int, val y: Int): Comparable<Point> {
    fun ccw(b: Point, c: Point) = (b.x - x) * (c.y - b.y) - (b.y - y) * (c.x - b.x)
    override fun compareTo(other: Point) = if (x != other.x) x - other.x else y - other.y
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val set = DisjointSet(n)
    val lines = Array(n) {
        val (x1, y1, x2, y2) = readLine().split(' ').map { round(it.toDouble() * 100).toInt() }
        Line(Point(x1, y1), Point(x2, y2))
    }
    for (i in 0..<n) for (j in i + 1..<n) if (lines[i].overwrap(lines[j])) set.union(i, j)
    for (i in 0..<n) set.find(i)
    println(set.parent.toSet().size)
}