fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val s = readLine().split(" ").map { it.toLong() }
    var l = 0
    var r = 0
    var ans = 1
    while (l <= r && r < n - 1) {
        if (s[r] < s[r + 1]) r++
        else {
            var t = 0
            if (s[r] == s[r + 1]) {
                while (t <= r - l && r + t + 1 < n && s[r + t + 1] == s[r - t]) t++
                t *= 2
            } else {
                while (t < r - l && r + t + 1 < n && s[r + t + 1] == s[r - t - 1]) t++
                t = 2 * t + 1
            }
            ans = maxOf(ans, t)
            l = ++r
        }
    }
    println(ans)
}
