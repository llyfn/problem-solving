class Solution {
    fun smallestIndex(nums: IntArray): Int {
        nums.forEachIndexed { idx, i ->
            if (idx == i.toString().sumOf { it.code - 48 }) return idx
        }
        return -1
    }
}