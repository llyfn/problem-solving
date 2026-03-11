func bitwiseComplement(n int) int {
	if n == 0 {
		return 1
	}
	return (1 << bits.Len(uint(n)) - 1) ^ n
}
