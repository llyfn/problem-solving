fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val factors = readLine().split(' ').map {
            it.toInt()
        }.let {
        println(it.maxOrNull()!! * it.minOrNull()!!)
    }

    close()
}