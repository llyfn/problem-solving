func numSpecial(mat [][]int) int {
	m, n := len(mat), len(mat[0])
	row := make([]int, m)
	col := make([]int, n)
	var ones [][2]int
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if mat[i][j] == 1 {
				row[i]++
				col[j]++
				ones = append(ones, [2]int{i, j})
			}
		}
	}
	ans := 0
	for _, one := range ones {
		if row[one[0]] == 1 && col[one[1]] == 1 {
			ans++
		}
	}
	return ans
}
