import java.io.StreamTokenizer
import kotlin.collections.ArrayDeque

fun main() = with(StreamTokenizer(System.`in`.bufferedReader())) {
    val nextStr = { nextToken(); sval }
    val nextInt = { nextToken(); nval.toInt() }
    val left = ArrayDeque( nextStr().toCharArray().toList())
    val right = ArrayDeque<Char>()
    repeat(nextInt()) {
        when (nextStr()) {
            "L" -> left.removeLastOrNull()?.let { right.addFirst(it) }
            "D" -> right.removeFirstOrNull()?.let { left.addLast(it) }
            "B" -> left.removeLastOrNull()
            "P" -> left.addLast(nextStr().first())
        }
    }
    println(left.joinToString("") + right.joinToString(""))
}
