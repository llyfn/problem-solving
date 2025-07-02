class Solution {
    fun toHex(num: Int): String {
        val h = "0123456789abcdef"
        return buildString { for (i in 7 downTo 0) append(h[num ushr i * 4 and 15]) }.trimStart('0').ifEmpty { "0" }
    }
}