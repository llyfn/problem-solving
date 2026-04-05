package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

type Edge struct {
	u, v int
	w    float64
}

var parent [101]int

func find(x int) int {
	if parent[x] != x {
		parent[x] = find(parent[x])
	}
	return parent[x]
}

func union(a, b int) bool {
	a, b = find(a), find(b)
	if a == b {
		return false
	}
	parent[a] = b
	return true
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	for {
		var n int
		fmt.Fscan(reader, &n)
		if n == 0 {
			break
		}

		x := make([]float64, n)
		y := make([]float64, n)
		z := make([]float64, n)
		r := make([]float64, n)
		for i := 0; i < n; i++ {
			fmt.Fscan(reader, &x[i], &y[i], &z[i], &r[i])
			parent[i] = i
		}

		var edges []Edge
		for i := 0; i < n; i++ {
			for j := i + 1; j < n; j++ {
				dx := x[i] - x[j]
				dy := y[i] - y[j]
				dz := z[i] - z[j]
				dist := math.Sqrt(dx*dx+dy*dy+dz*dz) - r[i] - r[j]
				if dist < 0 {
					dist = 0
				}
				edges = append(edges, Edge{i, j, dist})
			}
		}

		sort.Slice(edges, func(i, j int) bool {
			return edges[i].w < edges[j].w
		})

		ans := 0.0
		for _, e := range edges {
			if union(e.u, e.v) {
				ans += e.w
			}
		}

		fmt.Fprintf(writer, "%.3f\n", ans)
	}
}
