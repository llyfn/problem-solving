import java.io.StreamTokenizer
import kotlin.math.*

fun main() = with(StreamTokenizer(System.`in`.bufferedReader())) {
    fun next() = run { nextToken(); nval.toInt() }
    val n = next()
    val p = next()
    val hSeg = Array(1001) { mutableListOf<Segment>() }
    val vSeg = Array(1001) { mutableListOf<Segment>() }
    var d = 0L
    List(p) { next() to next() }.let { it + it.first() }.zipWithNext { (x1, y1), (x2, y2) ->
        if (y1 == y2) hSeg[y1] += Segment(min(x1, x2)..max(x1, x2), x1, d)
        else vSeg[x1] += Segment(min(y1, y2)..max(y1, y2), y1, d)
        d += abs(x1 - x2) + abs(y1 - y2)
    }
    hSeg.forEach { it.sort() }
    vSeg.forEach { it.sort() }
    fun List<Segment>.dist(c: Int): Long? = takeIf { isNotEmpty() }?.let {
        val r = binarySearch(Segment(c..c, 0, 0)).let { max(it, -it - 2) }
        (r..r + 1).firstNotNullOfOrNull { i -> getOrNull(i)?.takeIf { c in it.r }?.let { it.d + abs(c - it.c) } }
    }
    repeat(n) {
        val (x1, y1, x2, y2) = List(4) { next() }
        val d1 = hSeg[y1].dist(x1) ?: vSeg[x1].dist(y1) ?: 0
        val d2 = hSeg[y2].dist(x2) ?: vSeg[x2].dist(y2) ?: 0
        println(min(abs(d1 - d2), d - abs(d1 - d2)))
    }
}
data class Segment(val r: IntRange, val c: Int, val d: Long) : Comparable<Segment> {
    override fun compareTo(other: Segment) = r.first.compareTo(other.r.first)
}