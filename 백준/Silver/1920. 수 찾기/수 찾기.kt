fun main() = with(System.`in`.bufferedReader()) {
    readLine()
    val a = readLine().split(' ').sorted()
    readLine()
    readLine().split(' ').forEach { println(if (a.binarySearch(it) >= 0) 1 else 0) }
    close()
}