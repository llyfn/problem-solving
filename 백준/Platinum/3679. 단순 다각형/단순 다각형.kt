fun main() = with(System.`in`.bufferedReader()) {
    repeat(readLine().toInt()) {
        val p = readLine().split(" ").drop(1).map { it.toInt() }.chunked(2) { (x, y) -> Point(x, y) }.withIndex().sortedWith(compareBy({ it.value.x }, { it.value.y })).toMutableList()
        val (_, bp) = p.first()
        p.subList(1, p.size).sortWith { (_, p1), (_, p2) -> (-ccw(bp, p1, p2)).takeIf { it != 0 } ?: (bp.dist(p1) - bp.dist(p2)) }
        var i = p.size - 1
        while (i > 1 && ccw(bp, p[i - 1].value, p[i].value) == 0) i--
        p.subList(i, p.size).reverse()
        println(p.map { it.index }.joinToString(" "))
    }
}
class Point(val x: Int, val y: Int) { fun dist(p: Point) = (x - p.x) * (x - p.x) + (y - p.y) * (y - p.y) }
fun ccw(a: Point, b: Point, c: Point) = (b.x - a.x) * (c.y - b.y) - (b.y - a.y) * (c.x - b.x)