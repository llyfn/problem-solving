fun main() = with(System.`in`.bufferedReader()) {
    val s = readLine()
    for (i in 0..<s.length / 2) {
        if (s[i] != s[s.length - 1 - i]) {
            print(s.length)
            return
        }
    }
    print(if (s.toSet().size > 1) s.length - 1 else -1)
}
