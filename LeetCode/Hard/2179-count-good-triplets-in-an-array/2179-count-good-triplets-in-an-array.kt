class Solution {
    class fwt(val size: Int) {
        val tree = IntArray(size + 1)
        fun incr(i: Int) {
            var x = i + 1
            while (x <= size) { tree[x]++; x += x and -x }
        }
        fun sum(i: Int): Long {
            var x = i + 1
            var s = 0L
            while (x > 0) { s += tree[x]; x -= x and -x }
            return s
        }
    }
    fun goodTriplets(nums1: IntArray, nums2: IntArray): Long {
        val n = nums1.size
        val pos = IntArray(n).apply { nums2.forEachIndexed { i, v -> set(v, i) } }
        val tree = fwt(n)
        return nums1.indices.sumOf { i ->
            val mid = pos[nums1[i]]
            val l = tree.sum(mid)
            tree.incr(mid)
            l * (n - mid - i + l - 1)
        }
    }
}