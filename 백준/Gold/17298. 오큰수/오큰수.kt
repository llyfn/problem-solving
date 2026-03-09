import java.io.StreamTokenizer
import kotlin.collections.ArrayDeque

fun main() = with(StreamTokenizer(System.`in`.bufferedReader())) {
    val nextInt = { nextToken(); nval.toInt() }
    val n = nextInt()
    val a = IntArray(n) { nextInt() }
    val ans = IntArray(n) { -1 }
    val st = ArrayDeque<Pair<Int, Int>>()
    for ((i, v) in a.withIndex()) {
        while (st.isNotEmpty()) if (st.last().second < v) ans[st.removeLast().first] = v else break
        st.add(i to v)
    }
    println(ans.joinToString(" "))
}