class Solution {
    fun maxSubArray(nums: IntArray): Int {
        var ans = nums.first()
        var mx = nums.first()
        for (n in nums.drop(1)) {
          mx = maxOf(mx + n, n)
          ans = maxOf(ans, mx)
        }
        return ans
    }
}