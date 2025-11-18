class Solution {
    fun isOneBitCharacter(bits: IntArray): Boolean {
        val n = bits.size
        var i = 0
        while (i < n - 1) i += 1 + bits[i]
        return i < n
    }
}
