class Solution {
    fun braceExpansionII(expr: String): List<String> {
        val stack = ArrayDeque<Pair<MutableSet<String>, Set<String>>>()
        var union = mutableSetOf<String>()
        var prod = setOf("")
        for (c in expr) when (c) {
            '{' -> {
                stack.addLast(union to prod)
                union = mutableSetOf()
                prod = setOf("")
            }
            ',' -> {
                union.addAll(prod)
                prod = setOf("")
            }
            '}' -> {
                union.addAll(prod)
                val (ou, op) = stack.removeLast()
                prod = op.flatMap { s -> union.map { s + it } }.toSet()
                union = ou
            }
            else -> prod = prod.map { it + c }.toSet()
        }
        return (union + prod).sorted()
    }
}