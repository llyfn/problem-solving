fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    var s = 0b0000_0000_0000_0000_0000
    val sb = StringBuilder()

    for (i in 0 until n) {
        val command = readLine().split(" ")
        when (command[0]) {
            "add" -> s = s or (1 shl (command[1].toInt() - 1))
            "remove" -> s = s and (1 shl (command[1].toInt() - 1)).inv()
            "check" -> sb.append("${ s shr (command[1].toInt() - 1) and 1 }\n")
            "toggle" -> s = s xor (1 shl (command[1].toInt() - 1))
            "all" -> s = 0b1111_1111_1111_1111_1111
            "empty" -> s = 0b0000_0000_0000_0000_0000
        }
    }
    print(sb)
    close()
}