func maxDistance(colors []int) int {
	n := len(colors)
	for i := 0; i < n; i++ {
		if colors[0] != colors[n - 1 - i] || colors[i] != colors[n - 1] {
			return n - i - 1
		}
	}
	return 0
}