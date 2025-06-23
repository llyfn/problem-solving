fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val coins = List(n) { readLine().toCharArray() }
    var ans = n * n
    for (b in 1..<(1 shl n)) {
        var s = 0
        for (i in 0..<n) {
            var c = 0
            for (j in 0..<n) {
                var curr = coins[j][i]
                if (b and (1 shl j) != 0) curr = if (curr == 'H') 'T' else 'H'
                if (curr == 'T') c++
            }
            s += c.coerceAtMost(n - c)
        }
        ans = ans.coerceAtMost(s)
    }
    println(ans)
    close()
}