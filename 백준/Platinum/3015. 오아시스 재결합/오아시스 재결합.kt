fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val stack = ArrayDeque<Pair<Long, Long>>()
    var ans = 0L
    repeat(n) {
        val curr = readLine().toLong()
        var cnt = 1L
        while (stack.isNotEmpty() && stack.last().first < curr) ans += stack.removeLast().second
        if (stack.isNotEmpty()) {
            if (stack.last().first == curr) {
                stack.removeLast().let { (_, v) -> ans += v; cnt = v + 1 }
                if (stack.isNotEmpty()) ans++
            } else ans++
        }
        stack.addLast(curr to cnt)
    }
    println(ans)
    close()
}