import java.util.StringTokenizer

fun main() = with(System.`in`.bufferedReader()) {
    val readInts = { readLine().split(' ').map { it.toInt() }.toIntArray() }
    val (n, q) = readInts()
    val a = readInts()
    val b = readInts()

    var flag = 0
    val m = 1_000_000_007L
    val p = LongArray(n)
    p[0] = 1
    for (i in 1..<n) p[i] = (p[i - 1] * 31) % m
    var hashA = 0L
    var hashB = 0L
    for (i in 0..<n) {
        hashA = (hashA + a[i] * p[i]) % m
        hashB = (hashB + b[i] * p[i]) % m
    }
    if (hashA == hashB) flag = 1

    fun swap(i: Int, j: Int) {
        hashA = (hashA - a[i] * p[i] - a[j] * p[j] + m) % m
        val tmp = a[i]
        a[i] = a[j]
        a[j] = tmp
        hashA = (hashA + a[i] * p[i] + a[j] * p[j]) % m
        if (hashA == hashB && a contentEquals b) flag = 1
    }

    fun partition(p: Int, r: Int): Int {
        val x = a[r]
        var i = p - 1
        for (j in p..<r) if (a[j] <= x) { i++; swap(i, j) }
        swap(i + 1, r)
        return i + 1
    }

    fun select(p: Int, r: Int, q: Int) {
        if (flag == 1 || p == r) return
        val t = partition(p, r)
        val k = t - p + 1
        if (q < k) select(p, t - 1, q)
        else if (q > k) select(t + 1, r, q - k)
    }

    select(0, n - 1, q)
    print(flag)
}