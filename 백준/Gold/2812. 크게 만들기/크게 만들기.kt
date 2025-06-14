import kotlin.collections.ArrayDeque

fun main() = with(System.`in`.bufferedReader()) {
    var (_, k) = readLine().split(" ").map { it.toInt() }
    val num = readLine()
    val deque = ArrayDeque<Char>()
    for (i in num) {
        while (k > 0 && deque.isNotEmpty() && deque.last() < i) {
            deque.removeLast()
            k--
        }
        deque.addLast(i)
    }
    println(deque.joinToString("").substring(0, deque.size - k))

    close()
}
