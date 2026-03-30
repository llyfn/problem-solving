func checkStrings(s1, s2 string) bool {
	odds, evens := make(map[byte]int), make(map[byte]int)
	for i := 0; i < len(s1); i++ {
		if i%2 == 0 {
			evens[s1[i]]++
			evens[s2[i]]--
		} else {
			odds[s1[i]]++
			odds[s2[i]]--
		}
	}
	for c := byte('a'); c <= byte('z'); c++ {
		if odds[c] != 0 || evens[c] != 0 {
			return false
		}
	}
	return true
}