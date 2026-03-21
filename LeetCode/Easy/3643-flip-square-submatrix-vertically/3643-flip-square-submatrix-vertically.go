func reverseSubmatrix(grid [][]int, x int, y int, k int) [][]int {
	for i := 0; i < k/2; i++ {
		for j := y; j < y+k; j++ {
			grid[x+i][j], grid[x+k-i-1][j] = grid[x+k-i-1][j], grid[x+i][j]
		}
	}
	return grid
}