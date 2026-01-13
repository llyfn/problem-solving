fun main() {
    val s = readln()
    val n = s.length.toLong()
    val sa = s.suffixArray()
    val lcp = s.lcpArray(sa)
    var r = n * (n + 1) / 2
    for (i in lcp) r -= i
    println(r)
}

fun String.suffixArray(): List<Int> {
    val n = length
    var sa = (0..<n).toList()
    var ranks = map { it.code }
    var k = 1
    val c = compareBy<Int> { ranks[it] }.thenBy { ranks.getOrNull(it + k) ?: -1 }
    while (k < n) {
        sa = sa.sortedWith(c)
        val newRanks = IntArray(n)
        var rank = 0
        newRanks[sa[0]] = 0
        sa.zipWithNext { i, j -> if (c.compare(i, j) != 0) rank++; newRanks[j] = rank }
        ranks = newRanks.toList()
        if (rank == n - 1) break
        k *= 2
    }
    return sa
}

fun String.lcpArray(sa: List<Int>): List<Int> {
    val n = length
    val lcp = IntArray(n)
    val invSA = IntArray(n).also { sa.forEachIndexed { i, idx -> it[idx] = i } }
    var k = 0
    for (i in 0..<n) {
        if (invSA[i] == 0) k = 0
        else {
            val j = sa[invSA[i] - 1]
            while (getOrNull(i + k)?.equals(getOrNull(j + k)) == true) k++
            lcp[invSA[i]] = k
            k = maxOf(0, k - 1)
        }
    }
    return lcp.toList()
}