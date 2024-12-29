fun main() = with(System.`in`.bufferedReader()) {
    val input = readLine().split(" ").map{ it.toInt() }
    val n = input[0]; val s = input[1]
    val arr = readLine().split(" ").map{ it.toInt() }
    var ans = 0

    fun partialSet(sum: Int = 0, depth: Int = 0, isValid: Boolean = false) {
        if (depth == n) {
            if (isValid && sum == s) ans++
            return
        }

        partialSet(sum + arr[depth], depth + 1, true)
        partialSet(sum, depth + 1, isValid)
    }

    partialSet()
    print(ans)
    close()
}