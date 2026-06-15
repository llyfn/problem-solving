class Solution {
    fun deleteMiddle(head: ListNode?): ListNode? {
        if (head?.next == null) return null
        var s = head
        var h = head.next
        while (h?.next?.next != null) {
            s = s?.next
            h = h.next?.next
        }
        s?.next = s.next?.next
        return head
    }
}