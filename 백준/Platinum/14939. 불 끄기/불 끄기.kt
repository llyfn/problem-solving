fun main() = with(System.`in`.bufferedReader()) {
    val b = IntArray(10) { readLine().replace('#', '0').replace('O', '1').toInt(2) }
    var n = Int.MAX_VALUE
    val d = listOf(0 to 0, 0 to 1, 1 to 0, 0 to -1, -1 to 0)
    fun flip(b: IntArray, x: Int, y: Int) = d.forEach { (dx, dy) ->
        if (x + dx in 0..9 && y + dy in 0..9) b[x + dx] = b[x + dx] xor (1 shl (y + dy))
    }
    fun dfs(b: IntArray, r: Int, cnt: Int) {
        if (r == 10) { if (b.all { it == 0 }) n = minOf(n, cnt) }
        else {
            var cnt = cnt
            for (i in 0..9) if (b[r-1] and (1 shl i) != 0) { flip(b, r, i); cnt++ }
            dfs(b, r + 1, cnt)
        }
    }
    repeat(1 shl 10) { i ->
        val bb = b.clone()
        var cnt = 0
        for (j in 0..9) if (i and (1 shl j) != 0) { flip(bb, 0, j); cnt++ }
        dfs(bb, 1, cnt)
    }
    println(if (n == Int.MAX_VALUE) -1 else n)
}