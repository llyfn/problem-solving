func constructProductMatrix(grid [][]int) [][]int {
	const mod = 12345
	n, m, p := len(grid), len(grid[0]), 1
	ans := make([][]int, n)
	for i := range ans {
		ans[i] = make([]int, m)
	}
	for i, row := range grid {
		for j, v := range row {
			ans[i][j] = p
			p = p * v % mod
		}
	}
	p = 1
	for i := n - 1; i >= 0; i-- {
		for j := m - 1; j >= 0; j-- {
			ans[i][j] = ans[i][j] * p % mod
			p = p * grid[i][j] % mod
		}
	}
	return ans
}
