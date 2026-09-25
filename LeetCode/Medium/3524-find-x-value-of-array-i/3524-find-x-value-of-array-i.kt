class Solution {
    fun resultArray(nums: IntArray, k: Int): LongArray {
        val res = LongArray(k)
        var rem = LongArray(k)
        for (idx in nums.indices) {
            val d = LongArray(k)
            d[nums[idx] % k] += 1
            for (i in 0..<k) d[(i.toLong() * nums[idx] % k).toInt()] += rem[i]
            rem = d
            for (i in 0..<k) res[i] += rem[i]
        }
        return res
    }
}