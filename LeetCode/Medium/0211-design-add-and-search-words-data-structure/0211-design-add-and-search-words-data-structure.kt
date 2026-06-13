class WordDictionary() {
    class Node(var isEnd: Boolean) {
        val map: MutableMap<Char, Node> = mutableMapOf()
    }

    val root = Node(false)

    fun addWord(word: String) {
        var curr = root
        for (i in word.indices) {
            curr = curr.map.getOrPut(word[i]) { Node(false) }
            if (i == word.length - 1) curr.isEnd = true
        }
    }

    fun search(word: String, node: Node = root): Boolean {
        var curr = node
        for (i in word.indices) {
            if (word[i] == '.') {
                return if (i == word.length - 1) curr.map.any { (_, v) -> v.isEnd }
                else curr.map.any { (_, v) -> search(word.substring(i + 1), v) }
            }
            curr = curr.map.getOrElse(word[i]) { return false }
            if (i == word.length - 1) return curr.isEnd
        }
        return false
    }
}
