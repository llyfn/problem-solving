val vowel = setOf('a', 'e', 'i', 'o', 'u')

fun main() = with(System.`in`.bufferedReader()) {
    val input = readLine().split(' ').map { it.toInt() }
    val arr = readLine().replace(" ","").toCharArray().sorted()

    val sb = StringBuilder()
    passwordBuilder(arr, input[0], input[1], sb)
    print(sb)
    close()
}

fun passwordBuilder(arr: List<Char>, len: Int, c: Int, sb: StringBuilder,
                    vowels: Int = 0,
                    consonants: Int = 0,
                    sequence: String = "",
                    visited: BooleanArray = BooleanArray(c) { false }
) {
    if (len < 3 || c < 3 || len > 15 || c > 15 || len > c) return
    if (sequence.length > 1 && sequence[sequence.length - 1] < sequence[sequence.length - 2]) return
    if (sequence.length >= len) {
        if (vowels < 1 || consonants < 2) return
        sequence.forEach { sb.append(it) }
        sb.append("\n")
        return
    }

    for (i in 0 until c) {
        if (visited[i]) continue
        else {
            visited[i] = true
            if (arr[i] in vowel) passwordBuilder(arr, len, c, sb, vowels + 1, consonants,sequence + "${ arr[i] }", visited)
            else passwordBuilder(arr, len, c, sb, vowels, consonants + 1,sequence + "${ arr[i] }", visited)
            visited[i] = false
        }
    }
}