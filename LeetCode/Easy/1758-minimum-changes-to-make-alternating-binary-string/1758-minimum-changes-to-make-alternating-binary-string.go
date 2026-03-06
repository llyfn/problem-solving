func minOperations(s string) int {
	o, e := 0, 0
	for i := 0; i < len(s); i++ {
		if (s[i] == '0') == (i % 2 == 0) {
			o += 1
		} 
		if (s[i] == '1') == (i % 2 == 0) {
			e += 1
		}
	}
	return min(o, e)
}
