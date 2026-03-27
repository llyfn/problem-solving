func areSimilar(mat [][]int, k int) bool {
	m, n := len(mat), len(mat[0])
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if mat[i][j] != mat[i][((j + (1 - i % 2 * 2) * k) % n + n) % n] {
				return false
			}
		}
	}
	return true
}