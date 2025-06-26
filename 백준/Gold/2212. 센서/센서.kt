fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val k = readLine().toInt()
    val points = readLine().split(" ").map { it.toInt() }.sorted()
    val gaps = points.zipWithNext { a, b -> b - a }.sortedDescending()
    println(points.last() - points.first() - gaps.take(k - 1).sum())
    close()
}