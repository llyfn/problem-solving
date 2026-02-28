package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var tc int
	fmt.Fscan(reader, &tc)
	for t := 0; t < tc; t++ {
		var n int
		fmt.Fscan(reader, &n)
		pre := make([]int, n)
		inMap := make(map[int]int)
		for i := 0; i < n; i++ {
			fmt.Fscan(reader, &pre[i])
		}
		for i := 0; i < n; i++ {
			var v int
			fmt.Fscan(reader, &v)
			inMap[v] = i
		}
		preIdx := 0
		var post []int
		var build func(l, r int)
		build = func(l, r int) {
			if l > r {
				return
			}
			rt := pre[preIdx]
			preIdx++
			m := inMap[rt]
			build(l, m - 1)
			build(m + 1, r)
			post = append(post, rt)
		}
		build(0, n-1)
		for i, v := range post {
			fmt.Print(v)
			if i < len(post)-1 {
				fmt.Print(" ")
			}
		}
		fmt.Println()
	}
}
