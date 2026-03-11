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
	cost := make([]int, n)
	dc := make([][][2]int, n)
	for i := 0; i < n; i++ {
		dc[i] = make([][2]int, n)
	}
	var p, a, d int
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &cost[i])
	}
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &p)
		for j := 0; j < p; j++ {
			fmt.Fscan(reader, &a, &d)
			dc[i] = append(dc[i], [2]int{a-1, d})
		}
	}
	ans := 10000
	vst := make([]bool, n)
	var bt func(int, int)
	bt = func(idx, val int) {
		if val >= ans {
			return
		}
		if idx == n {
			ans = val
			return
		}
		for i := 0; i < n; i++ {
			if vst[i] {
				continue
			}
			vst[i] = true
			for _, v := range dc[i] {
				cost[v[0]] -= v[1]
			}
			bt(idx + 1, val + max(1, cost[i]))
			for _, v := range dc[i] {
				cost[v[0]] += v[1]
			}
			vst[i] = false
		}
	}
	bt(0, 0)
	fmt.Println(ans)
}
