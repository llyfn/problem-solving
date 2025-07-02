class Solution {
    fun minimumIndex(nums: List<Int>): Int {
        val n = nums.size
        val (dom, freq) = nums.groupingBy { it }.eachCount().maxBy { it.value }
        val f = IntArray(n)
        f[0] = if (nums[0] == dom) 1 else 0
        for (i in 1..<n) f[i] = f[i-1] + if (nums[i] == dom) 1 else 0
        for (i in 0..<n) if (f[i] > (i + 1) / 2 && freq - f[i] > (n - i - 1) / 2) return i
        return -1
    }
}