func findRotation(mat [][]int, target [][]int) bool {
	n := len(mat)
	for c := 0; c < 4; c++ {
		if reflect.DeepEqual(mat, target) {
			return true
		}
		for i := 0; i < n/2; i++ {
			for j := i; j < n-i-1; j++ {
				mat[i][j], mat[j][n-1-i], mat[n-1-i][n-1-j], mat[n-1-j][i] = mat[n-1-j][i], mat[i][j], mat[j][n-1-i], mat[n-1-i][n-1-j]
			}
		}
	}
	return false
}