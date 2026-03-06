package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n)
	cows := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &cows[i])
	}
	var st [][2]int
	ans := 0
	for i := 0; i < n; i++ {
		for len(st) > 0 {
			if st[len(st)-1][1] < cows[i] {
				ans += i - st[len(st)-1][0] + 1
				st = st[:len(st)-1]
			} else {
				break
			}
		}
		st = append(st, [2]int{i, cows[i]})
	}
	st = [][2]int{}
	for i := n - 1; i >= 0; i-- {
		for len(st) > 0 {
			if st[len(st)-1][1] < cows[i] {
				ans += st[len(st)-1][0] - i + 1
				st = st[:len(st)-1]
			} else {
				break
			}
		}
		st = append(st, [2]int{i, cows[i]})
	}
	fmt.Println(ans)
}
