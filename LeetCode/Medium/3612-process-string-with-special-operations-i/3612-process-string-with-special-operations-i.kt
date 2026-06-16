class Solution {
    fun processStr(s: String): String {
      var ans = ""
      for (c in s) {
        when (c) {
          '*' -> ans = ans.dropLast(1)
          '#' -> ans = ans + ans
          '%' -> ans = ans.reversed()
          else -> ans += c
        }
      }
      return ans
    }
}