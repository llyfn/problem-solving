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
	dist := make([][]int, n)
	for i := 0; i < n; i++ {
		dist[i] = make([]int, n)
		for j := 0; j < n; j++ {
			fmt.Fscan(reader, &dist[i][j])
		}
	}
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			flag := true
			for k := 0; k < n; k++ {
				if k == i || k == j {
					continue
				}
				if dist[i][j] == dist[i][k]+dist[k][j] {
					flag = false
					break
				}
			}
			if flag {
				fmt.Printf("%d %d\n", i+1, j+1)
			}
		}
	}
}
