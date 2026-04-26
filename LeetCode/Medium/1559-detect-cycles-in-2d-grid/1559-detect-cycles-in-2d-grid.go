func containsCycle(grid [][]byte) bool {
	m, n := len(grid), len(grid[0])
	parent := make([]int, m*n)
	rank := make([]int, m*n)
	for i := range parent {
		parent[i] = i
	}
	var find func(int) int
	find = func(x int) int {
		if parent[x] != x {
			parent[x] = find(parent[x])
		}
		return parent[x]
	}
	union := func(x, y int) bool {
		rx, ry := find(x), find(y)
		if rx == ry {
			return false
		}
		if rank[rx] < rank[ry] {
			rx, ry = ry, rx
		}
		parent[ry] = rx
		if rank[rx] == rank[ry] {
			rank[rx]++
		}
		return true
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if i > 0 && j > 0 && grid[i][j] == grid[i-1][j] && grid[i][j] == grid[i][j-1] && grid[i-1][j] == grid[i][j-1] {
				if find((i-1)*n+j) == find(i*n+j-1) {
					return true
				}
			}
			if i > 0 && grid[i][j] == grid[i-1][j] {
				if !union(i*n+j, (i-1)*n+j) {
					return true
				}
			}
			if j > 0 && grid[i][j] == grid[i][j-1] {
				if !union(i*n+j, i*n+j-1) {
					return true
				}
			}
		}
	}
	return false
}