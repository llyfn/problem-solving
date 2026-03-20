package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	var t, n int
	reader := bufio.NewReader(os.Stdin)
	for fmt.Fscan(reader, &t); t > 0; t-- {
		fmt.Fscan(reader, &n)
		pts := make([][2]float64, n)
		for i := 0; i < n; i++ {
			fmt.Fscan(reader, &pts[i][0], &pts[i][1])
		}
		ans := 1e9
		var solve func(idx, cnt int, sx, sy float64)
		solve = func(idx, cnt int, sx, sy float64) {
			if cnt == n/2 {
				for i := idx; i < n; i++ {
					sx, sy = sx-pts[i][0], sy-pts[i][1]
				}
				ans = min(ans, math.Sqrt(sx*sx+sy*sy))
				return
			}
			if idx == n {
				return
			}
			solve(idx+1, cnt+1, sx+pts[idx][0], sy+pts[idx][1])
			solve(idx+1, cnt, sx-pts[idx][0], sy-pts[idx][1])
		}
		solve(0, 0, 0, 0)
		fmt.Printf("%.12f\n", ans)
	}
}
