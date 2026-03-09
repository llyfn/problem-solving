import java.io.StreamTokenizer

fun main() = with(StreamTokenizer(System.`in`.bufferedReader())) {
    val nextInt = { nextToken(); nval.toInt() }
    val n = nextInt()
    val a = IntArray(n) { nextInt() }
    val op = IntArray(4) { nextInt() }
    var (mx, mn) = Int.MIN_VALUE to Int.MAX_VALUE
    fun backtrack(idx: Int, v: Int) {
        if (idx == n) {
            mx = maxOf(mx, v)
            mn = minOf(mn, v)
            return
        }
        repeat(4) {
            if (op[it] > 0) {
                op[it] -= 1
                when (it) {
                    0 -> backtrack(idx + 1, v + a[idx])
                    1 -> backtrack(idx + 1, v - a[idx])
                    2 -> backtrack(idx + 1, v * a[idx])
                    3 -> backtrack(idx + 1, v / a[idx])
                }
                op[it] += 1
            }
        }
    }
    backtrack(1, a[0])
    print("$mx\n$mn")
}
