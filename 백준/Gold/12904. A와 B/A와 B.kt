fun main() = with(System.`in`.bufferedReader()) {
    val s = readLine()
    var t = readLine()
    while (s.length < t.length) {
        t = if (t.last() == 'A') t.dropLast(1) else t.dropLast(1).reversed()
    }
    print(if (s == t) 1 else 0)
    close()
}
