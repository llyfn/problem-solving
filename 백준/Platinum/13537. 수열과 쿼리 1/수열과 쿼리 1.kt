class MergeSortTree(private val arr: List<Int>) {
    private val size = arr.size
    private val tree: Array<List<Int>> = Array(4 * size) { emptyList() }

    init { build(1, 0, size - 1) }

    private fun build(n: Int, s: Int, e: Int) {
        if (s == e) tree[n] = listOf(arr[s])
        else {
            val mid = (s + e) / 2
            build(2 * n, s, mid)
            build(2 * n + 1, mid + 1, e)
            tree[n] = merge(tree[2 * n], tree[2 * n + 1])
        }
    }
    private fun merge(l1: List<Int>, l2: List<Int>): List<Int> = buildList {
        var i = 0
        var j = 0
        while (i < l1.size && j < l2.size) if (l1[i] <= l2[j]) add(l1[i++]) else add(l2[j++])
        while (i < l1.size) add(l1[i++])
        while (j < l2.size) add(l2[j++])
    }

    fun query(l: Int, r: Int, k: Int): Int {
        if (l > r || l < 0 || r >= size) return 0
        return query(1, 0, size - 1, l, r, k)
    }
    private fun query(n: Int, s: Int, e: Int, l: Int, r: Int, k: Int): Int {
        if (r < s || e < l) return 0
        if (l <= s && e <= r) return tree[n].size - upperBound(tree[n], k)
        val mid = (s + e) / 2
        return query(2 * n, s, mid, l, r, k) + query(2 * n + 1, mid + 1, e, l, r, k)
    }
    private fun upperBound(list: List<Int>, value: Int): Int {
        var low = 0
        var high = list.size
        while (low < high) {
            val mid = (low + high) / 2
            if (list[mid] <= value) low = mid + 1 else high = mid
        }
        return low
    }
}
fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val out = StringBuilder()
    val mst = MergeSortTree(readLine().split(" ").map { it.toInt() })
    repeat(readLine().toInt()) {
        val (i, j, k) = readLine().split(" ").map { it.toInt() }
        out.appendLine(mst.query(i - 1, j - 1, k))
    }
    print(out)
}