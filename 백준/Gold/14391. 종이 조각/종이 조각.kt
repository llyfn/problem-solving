fun main() = with(System.`in`.bufferedReader()) {
    val (n, m) = readLine().split(" ").map { it.toInt() }
    val map = Array(n) { IntArray(m) }
    for (i in 0 until n) map[i] = readLine().map { it.digitToInt() }.toIntArray()

    var ans = 0
    for (i in 0 until (1 shl (n * m))) {
        var sum = 0
        for (j in 0 until n) {
            var num = 0
            for (k in 0 until m) {
                if ((i and (1 shl (j * m + k)) == 0)) num = num * 10 + map[j][k]
                else {
                    sum += num
                    num = 0
                }
            }
            sum += num
        }
        for (k in 0 until m) {
            var num = 0
            for (j in 0 until n) {
                if ((i and (1 shl (j * m + k)) != 0)) num = num * 10 + map[j][k]
                else {
                    sum += num
                    num = 0
                }
            }
            sum += num
        }

        if (ans < sum) ans = sum
    }
    println(ans)
    close()
}
