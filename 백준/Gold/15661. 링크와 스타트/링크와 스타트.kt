import kotlin.math.abs
import kotlin.math.min

fun main() = with(System.`in`.bufferedReader()) {
    val size = readLine().toInt()
    val map = Array(size) { IntArray(size) }.apply{
        for (i in 0 until size) this[i] = readLine().split(" ").map{ it.toInt() }.toIntArray()
    }
    val selected = BooleanArray(size)
    var ans = Int.MAX_VALUE

    fun linkAndStart(player: Int = 0, depth: Int = 0) {
        if (depth == size) {
            if (player > 0) {
                var link = 0
                var start = 0
                for (i in 0 until size) for (j in i + 1 until size) {
                    if (selected[i] && selected[j]) link += map[i][j] + map[j][i]
                    else if (!selected[i] && !selected[j]) start += map[i][j] + map[j][i]
                }
                ans = min(ans, abs(link - start))
            }
            return
        }

        if (!selected[depth]) {
            selected[depth] = true
            linkAndStart(player + 1, depth + 1)
            selected[depth] = false
            linkAndStart(player, depth + 1)
        }
    }

    linkAndStart()
    println(ans)

    close()
}
