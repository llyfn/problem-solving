fun main() = with(System.`in`.bufferedReader()) {
    val (n, m) = readLine().split(' ').map { it.toInt() }
    val jobs = List(n) { readLine().split(' ').drop(1).map { it.toInt() } }
    val asgn = IntArray(m + 1) { -1 }
    val vst = IntArray(m + 1) { 0 }
    var cnt = 1
    fun dfs(x: Int): Boolean {
        for (j in jobs[x]) if (vst[j] != cnt) {
            vst[j] = cnt
            if (asgn[j] < 0 || dfs(asgn[j])) {
                asgn[j] = x
                return true
            }
        }
        return false
    }
    print(jobs.indices.count { cnt++; dfs(it) })
}