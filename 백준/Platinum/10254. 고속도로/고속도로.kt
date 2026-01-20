import java.io.StreamTokenizer

fun main() = with(StreamTokenizer(System.`in`.bufferedReader())) {
    fun next() = run { nextToken(); nval }
    repeat(next().toInt()) {
        val n = next().toInt()
        val ps = Array(n) { Point(next().toLong(), next().toLong()) }.sorted()
        val h = build(ps).apply { addAll(build(ps.reversed())) }
        var (m, j) = 0L to 1;
        var (p1, p2) = h[0] to h[0]
        for (i in 0..<h.size) {
            val nI = (i + 1) % h.size
            while (true) { val nJ = (j + 1) % h.size;if (h[nI] - h[i] x h[nJ] - h[j] > 0) j = nJ else break }
            if (h[i].distSq(h[j]) > m) { m = h[i].distSq(h[j]); p1 = h[i]; p2 = h[j] }
            if (h[nI].distSq(h[j]) > m) { m = h[nI].distSq(h[j]); p1 = h[nI]; p2 = h[j] }
        }
        println("${p1.x} ${p1.y} ${p2.x} ${p2.y}")
    }
}

class Point(val x: Long, val y: Long) : Comparable<Point> {
    fun distSq(p: Point) = (p.x - x) * (p.x - x) + (p.y - y) * (p.y - y)
    infix fun x(p: Point) = x * p.y - y * p.x
    operator fun minus(p: Point) = Point(x - p.x, y - p.y)
    override fun compareTo(o: Point): Int = if (x != o.x) x.compareTo(o.x) else y.compareTo(o.y)
}

fun build(ps: List<Point>) = mutableListOf<Point>().apply {
    for (p in ps) { while (size > 1 && last() - get(size - 2) x p - last() <= 0L) { removeLast() }; add(p) }
    removeLast()
}