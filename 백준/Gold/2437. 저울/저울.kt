fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val weights = readLine().split(" ").map { it.toInt() }.sorted()
    var ans = 1
    for (w in weights) {
        if (w > ans) break
        else ans += w
    }
    println(ans)
    close()
}
