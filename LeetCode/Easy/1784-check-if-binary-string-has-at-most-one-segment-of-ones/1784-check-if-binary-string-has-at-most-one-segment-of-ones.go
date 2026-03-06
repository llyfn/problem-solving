func checkOnesSegment(s string) bool {
	z := false
	for i := 0; i < len(s); i++ {
		if s[i] == '0' {
			z = true
		} else if z {
			return false
		}
	}
	return true
}