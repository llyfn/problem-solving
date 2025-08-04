fun main() = with(System.`in`.bufferedReader()) {
    val ps = readLine().split(" ").map { it.toDouble() }.chunked(2) { (x, y) -> Point(x, y) }
    println(if (ps[0].ccw(ps[1], ps[2]) * ps[0].ccw(ps[1], ps[3]) < 0) 1 else 0)
}

data class Point(val x: Double, val y: Double) {
    fun ccw(b: Point, c: Point) = (b.x - x) * (c.y - b.y) - (b.y - y) * (c.x - b.x)
}
