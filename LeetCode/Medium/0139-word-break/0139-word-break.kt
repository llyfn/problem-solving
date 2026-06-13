class Trie() {
    class Node(var isEnd: Boolean) {
        val map: MutableMap<Char, Node> = mutableMapOf()
    }

    val root = Node(false)

    fun insert(word: String) {
        var curr = root
        for (i in word.indices) {
            curr = curr.map.getOrPut(word[i]) { Node(false) }
            if (i == word.length - 1) curr.isEnd = true
        }
    }

    fun search(word: String): Boolean {
        var curr = root
        for (i in word.indices) {
            curr = curr.map.getOrElse(word[i]) { return false }
            if (i == word.length - 1) return curr.isEnd
        }
        return false
    }
}

class Solution {
    fun wordBreak(s: String, wordDict: List<String>): Boolean {
        val trie = Trie()
        for (w in wordDict) trie.insert(w)
        val dp = BooleanArray(s.length)
        for (i in s.indices) if (i == 0 || dp[i-1]) {
            for (j in i..s.length) if (trie.search(s.substring(i, j))) dp[j - 1] = true
        }
        return dp.last()
    }
}