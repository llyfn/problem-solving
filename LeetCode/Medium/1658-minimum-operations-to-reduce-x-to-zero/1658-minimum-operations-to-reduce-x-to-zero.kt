class Solution {
    fun minOperations(nums: IntArray, x: Int): Int {
        var (l, s) = 0 to 0
        var res = -1
        val d = nums.sum() - x
        if (d < 0) return -1
        nums.forEachIndexed { r, i ->
            s += i
            while (s > d) s -= nums[l++]
            if (s == d) res = max(res, r - l + 1)
        }
        return if (res >= 0) nums.size - res else -1
    }
}
