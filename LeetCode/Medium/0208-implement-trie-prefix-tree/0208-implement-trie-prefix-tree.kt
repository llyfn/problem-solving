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

    fun startsWith(prefix: String): Boolean {
        var curr = root
        for (i in prefix.indices) {
            curr = curr.map.getOrElse(prefix[i]) { return false }
        }
        return true
    }
}
