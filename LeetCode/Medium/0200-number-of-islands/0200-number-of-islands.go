func numIslands(grid [][]byte) int {
	ans := 0
	dr := []int{-1, 0, 1, 0}
	dc := []int{0, -1, 0, 1}
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == '1' {
				grid[i][j] = '0'
				ans++
				q := [][2]int{{i, j}}
				for len(q) > 0 {
					r, c := q[0][0], q[0][1]
					q = q[1:]
					for k := 0; k < 4; k++ {
						nr, nc := r+dr[k], c+dc[k]
						if nr >= 0 && nr < len(grid) && nc >= 0 && nc < len(grid[0]) && grid[nr][nc] == '1' {
							q = append(q, [2]int{nr, nc})
							grid[nr][nc] = '0'
						}
					}
				}
			}
		}
	}
	return ans
}