class Solution {
    fun maximumLength(nums: IntArray): Int {
        val p = listOf(listOf(0, 0), listOf(0, 1), listOf(1, 0), listOf(1, 1))
        val cnt = MutableList(4) { 0 }
        for (i in nums) for (j in p.indices) if (i % 2 == p[j][cnt[j] % 2]) cnt[j]++
        return cnt.max()
    }
}