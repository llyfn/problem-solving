class Solution {
    fun lexicalOrder(n: Int): List<Int> {
        val ans = mutableListOf<Int>()
        fun dfs(p: String) {
            ans += p.toInt()
            for (i in 0..9) if ((p + i.toString()).toInt() <= n) dfs(p + i.toString())
        }
        for (i in 1..9) if (i <= n) dfs(i.toString())
        return ans
    }
}