fun main() {
    var (n, m, k) = readln().split(' ').map { it.toInt() }
    val jobs = List(n) { readln().split(' ').drop(1).map { it.toInt() } }
    val a = IntArray(m + 1) { -1 }
    val v = IntArray(m + 1)
    var c = 1
    fun dfs(x: Int): Boolean {
        for (j in jobs[x]) if (v[j] != c) {
            v[j] = c
            if (a[j] < 0 || dfs(a[j])) { a[j] = x; return true }
        }
        return false
    }
    var ans = (0..<n).count { c++; dfs(it) }
    var i = 0
    while (i < n && k > 0) { c++; if (dfs(i)) { ans++; k-- }; i++ }
    print(ans)
}
