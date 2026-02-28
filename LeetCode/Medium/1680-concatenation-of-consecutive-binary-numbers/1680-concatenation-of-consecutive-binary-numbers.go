const MOD = int64(1_000_000_007)
func concatenatedBinary(n int) int {
	var ans int64 = 0
	for i := 1; i <= n; i++ {
		ans = ((ans << bits.Len(uint(i))) + int64(i)) % MOD
	}
	return int(ans)
}