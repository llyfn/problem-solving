fun main() = with(System.`in`.bufferedReader()) {
    readLine()
    val a = readLine().split(' ').map { it.toInt() }.sorted()
    readLine()
    readLine().split(' ').map { it.toInt() }.forEach {
        println(if (a.binarySearch(it) >= 0) 1 else 0)
    }
    close()
}