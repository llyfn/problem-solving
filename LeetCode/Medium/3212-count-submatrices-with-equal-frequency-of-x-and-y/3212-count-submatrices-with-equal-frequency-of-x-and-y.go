func numberOfSubmatrices(grid [][]byte) int {
	x := make([][]int, len(grid) + 1)
	y := make([][]int, len(grid) + 1)
	for i := range x {
		x[i] = make([]int, len(grid[0]) + 1)
		y[i] = make([]int, len(grid[0]) + 1)
	}
	ans := 0
	for i := range grid {
		for j := range grid[i] {
			x[i+1][j+1] = x[i+1][j] + x[i][j+1] - x[i][j]
			y[i+1][j+1] = y[i+1][j] + y[i][j+1] - y[i][j]
			if grid[i][j] == 'X' {
				x[i+1][j+1]++
			} else if grid[i][j] == 'Y' {
				y[i+1][j+1]++
			}
			if x[i+1][j+1] > 0 && x[i+1][j+1] == y[i+1][j+1] {
				ans++
			}
		}
	}
	return ans
}