package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var N, K int
	fmt.Fscan(reader, &N, &K)
	cost := make([][]int, N)
	for i := 0; i < N; i++ {
		cost[i] = make([]int, N)
		for j := 0; j < N; j++ {
			fmt.Fscan(reader, &cost[i][j])
		}
	}
	for k := 0; k < N; k++ {
		for i := 0; i < N; i++ {
			for j := 0; j < N; j++ {
				cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])
			}
		}
	}
	ans := int(1e9)
	var bt func(idx, v, c int)
	bt = func(idx, v, c int) {
		if v == (1 << N) - 1 {
			ans = min(ans, c)
			return
		}
		for i := 0; i < N; i++ {
			if v & (1 << i) == 0 {
				bt(i, v | (1 << i), c + cost[idx][i])
			}
		}
	}
	bt(K, 1 << K, 0)
	fmt.Println(ans)
}
