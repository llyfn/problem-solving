class FindSumPairs(val nums1: IntArray, val nums2: IntArray) {
    val cnt = nums2.asIterable().groupingBy { it }.eachCount().toMutableMap()

    fun add(i: Int, v: Int) {
        cnt[nums2[i]] = cnt[nums2[i]]!! - 1
        nums2[i] += v
        cnt[nums2[i]] = cnt.getOrDefault(nums2[i], 0) + 1
    }

    fun count(t: Int): Int = nums1.sumOf { cnt.getOrDefault(t - it, 0) }
}
