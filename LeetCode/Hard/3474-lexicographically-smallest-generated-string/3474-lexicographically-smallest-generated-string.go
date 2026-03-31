func generateString(str1, str2 string) string {
	n := len(str1)
	m := len(str2)
	totalLen := n + m - 1
	word := make([]byte, totalLen)
	fixed := make([]bool, totalLen)
	for i := 0; i < n; i++ {
		if str1[i] == 'T' {
			for j := 0; j < m; j++ {
				if fixed[i+j] && word[i+j] != str2[j] {
					return ""
				}
				word[i+j] = str2[j]
				fixed[i+j] = true
			}
		}
	}
	for i := 0; i < totalLen; i++ {
		if !fixed[i] {
			word[i] = 'a'
		}
	}
	for i := 0; i < n; i++ {
		if str1[i] == 'F' {
			if string(word[i:i+m]) == str2 {
				changed := false
				for j := m - 1; j >= 0; j-- {
					if !fixed[i+j] {
						if str2[j] == 'a' {
							word[i+j] = 'b'
						} else {
							word[i+j] = 'a'
						}
						changed = true
						break
					}
				}
				if !changed {
					return ""
				}
			}
		}
	}
	for i := 0; i < n; i++ {
		match := string(word[i:i+m]) == str2
		if (str1[i] == 'T' && !match) || (str1[i] == 'F' && match) {
			return ""
		}
	}
	return string(word)
}