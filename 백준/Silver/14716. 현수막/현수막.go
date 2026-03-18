package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var m, n int
	fmt.Fscanln(reader, &m, &n)
	mat := make([][]int, m)
	for i := 0; i < m; i++ {
		mat[i] = make([]int, n)
		for j := 0; j < n; j++ {
			fmt.Fscan(reader, &mat[i][j])
		}
	}
	ans := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if mat[i][j] == 1 {
				ans++
				mat[i][j] = 0
				q := [][2]int{{i, j}}
				for len(q) > 0 {
					r, c := q[0][0], q[0][1]
					q = q[1:]
					for nr := r - 1; nr <= r+1; nr++ {
						for nc := c - 1; nc <= c+1; nc++ {
							if nr >= 0 && nr < m && nc >= 0 && nc < n && mat[nr][nc] == 1 {
								q = append(q, [2]int{nr, nc})
								mat[nr][nc] = 0
							}
						}
					}
				}
			}

		}
	}
	fmt.Println(ans)
}
