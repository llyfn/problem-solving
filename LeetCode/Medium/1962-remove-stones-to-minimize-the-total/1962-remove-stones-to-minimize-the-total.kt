class Solution {
    fun minStoneSum(piles: IntArray, k: Int): Int {
        val queue = java.util.PriorityQueue<Int>(compareByDescending { it })
        for (p in piles) queue.add(p)
        repeat(k) { queue.add((queue.poll() + 1) / 2) }
        return queue.sum()
    }
}