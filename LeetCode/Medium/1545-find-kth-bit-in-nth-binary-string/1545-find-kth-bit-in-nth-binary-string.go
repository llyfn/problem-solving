func findKthBit(n, k int) byte {
	if n == 1 {
		return '0'
	}
	mid := 1 << uint(n-1)
	if k < mid {
		return findKthBit(n-1, k)
	} else if k > mid {
		res := findKthBit(n-1, 2 * mid - k)
		if res == '0' {
			return '1'
		}
		return '0'
	}
	return '1'
}