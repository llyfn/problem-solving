func hasValidPath(grid [][]int) bool {
	m, n := len(grid), len(grid[0])
	dirs := map[int][][2]int{
		1: {{0, -1}, {0, 1}},
		2: {{-1, 0}, {1, 0}},
		3: {{0, -1}, {1, 0}},
		4: {{0, 1}, {1, 0}},
		5: {{0, -1}, {-1, 0}},
		6: {{0, 1}, {-1, 0}},
	}
	visited := make([][]bool, m)
	for i := range visited {
		visited[i] = make([]bool, n)
	}
	queue := [][2]int{{0, 0}}
	visited[0][0] = true
	for len(queue) > 0 {
		cell := queue[0]
		queue = queue[1:]
		r, c := cell[0], cell[1]
		if r == m-1 && c == n-1 {
			return true
		}
		for _, d := range dirs[grid[r][c]] {
			nr, nc := r+d[0], c+d[1]
			if nr < 0 || nr >= m || nc < 0 || nc >= n || visited[nr][nc] {
				continue
			}
			connected := false
			for _, nd := range dirs[grid[nr][nc]] {
				if nr+nd[0] == r && nc+nd[1] == c {
					connected = true
					break
				}
			}
			if connected {
				visited[nr][nc] = true
				queue = append(queue, [2]int{nr, nc})
			}
		}
	}
	return false
}