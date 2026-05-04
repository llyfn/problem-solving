func rotate(m [][]int) {
	n := len(m)
	for i := 0; i < n/2; i++ {
		for j := 0; j < n-2*i-1; j++ {
			m[i][i+j], m[i+j][n-i-1], m[n-i-1][n-i-j-1], m[n-i-j-1][i] = m[n-i-j-1][i], m[i][i+j], m[i+j][n-i-1], m[n-i-1][n-i-j-1]
		}
	}
}