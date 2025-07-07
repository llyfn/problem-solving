class Solution {
    fun maxEvents(e: Array<IntArray>): Int = with(java.util.PriorityQueue<Int>()) {
        e.sortBy { it[0] }
        var i = 0
        (1..e.maxOf { it[1] }).count { d ->
            while (i < e.size && e[i][0] == d) add(e[i++][1])
            while (isNotEmpty() && peek() < d) poll()
            poll() != null
        }
    }
}