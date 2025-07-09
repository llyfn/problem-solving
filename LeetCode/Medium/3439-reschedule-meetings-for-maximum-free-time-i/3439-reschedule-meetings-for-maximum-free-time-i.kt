class Solution {
    fun maxFreeTime(t: Int, k: Int, s: IntArray, e: IntArray): Int {
        val n = s.size
        val gapSum = (0..n-2).runningFold(s[0]) { acc, i -> acc + (s[i + 1] - e[i]) }.toMutableList()
        gapSum.add(0, 0)
        gapSum.add(gapSum.last() + t - e[n - 1])
        print(gapSum)
        return (0..n-k).maxOf { gapSum[it + k + 1] - gapSum[it] }
    }
}