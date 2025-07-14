class Solution {
    fun getDecimalValue(head: ListNode?) =
        generateSequence(head) { it.next }.fold(0) { acc, node -> (acc shl 1) or node.`val` }
}