fun main() {
    val n = readln().toInt()
    val a = readln().split(" ").map { it.toInt() % 2 }.toIntArray()
    val ft = FenwickTree(n)
    for (i in 1..n) ft.add(i, a[i - 1])
    repeat(readln().toInt()) {
        val (c, x, y) = readln().split(" ").map { it.toInt() }
        when (c) {
            1 -> { ft.add(x,y % 2 - a[x - 1]); a[x - 1] = y % 2 }
            2 -> println(y - x - ft.sum(y) + ft.sum(x - 1) + 1)
            3 -> println(ft.sum(y) - ft.sum(x - 1))
        }
    }

}
class FenwickTree(val n: Int) {
    private val tree = IntArray(n + 1)
    fun add(i: Int, v: Int) {
        var x = i
        while (x <= n) { tree[x] += v; x += x and -x }
    }
    fun sum(i: Int): Long {
        var x = i
        var r = 0L
        while (x > 0) { r += tree[x]; x -= x and -x }
        return r
    }
}
