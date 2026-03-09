fun main() {
    var ans = 0
    var s = 0
    for (c in readln().replace("()","|")) {
        when (c) {
            '(' -> s += 1
            '|' -> ans += s
            ')' -> { ans += 1; s -= 1}
        }
    }
    println(ans)
}