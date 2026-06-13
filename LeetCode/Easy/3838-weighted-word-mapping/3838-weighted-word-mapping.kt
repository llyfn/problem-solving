class Solution {
    fun mapWordWeights(words: Array<String>, weights: IntArray): String =
        words.map { 'z' - it.sumOf { c -> weights[c - 'a'] } % 26 }.joinToString("")
}