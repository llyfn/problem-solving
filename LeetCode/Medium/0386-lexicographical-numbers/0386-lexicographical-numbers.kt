class Solution {
    fun lexicalOrder(n: Int): List<Int> {
        val ans = mutableListOf<Int>()
        fun dfs(p: Int) {
            ans += p
            for (i in 0..9) if (p * 10 + i <= n) dfs(p * 10 + i)
        }
        for (i in 1..9) if (i <= n) dfs(i)
        return ans
    }
}