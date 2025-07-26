fun main() = with(System.`in`.bufferedReader()) {
    val out = StringBuilder()
    List(readLine().toInt()) { readLine().toInt() }.sortedDescending().forEach { out.appendLine(it) }
    print(out)
}