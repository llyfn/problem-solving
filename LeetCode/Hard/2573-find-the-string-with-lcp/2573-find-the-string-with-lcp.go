func findTheString(lcp [][]int) string {
	n := len(lcp)
	word := make([]rune, n)
	curr := 'a'
	for i := range word {
		if word[i] == 0 {
			if curr > 'z' {
				return ""
			}
			word[i] = curr
			for j := i + 1; j < n; j++ {
				if lcp[i][j] > 0 {
					word[j] = word[i]
				}
			}
			curr++
		}
	}
	for i := n - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			val := 0
			if word[i] == word[j] {
				val = 1
				if i < n-1 && j < n-1 {
					val += lcp[i+1][j+1]
				}
			}
			if lcp[i][j] != val {
				return ""
			}
		}
	}
	return string(word)
}