func minDistance(word1, word2 string) int {
	prev := make([]int, len(word2)+1)
	for i := range len(word2) + 1 {
		prev[i] = i
	}
	for i := range len(word1) {
		curr := make([]int, len(word2)+1)
		curr[0] = i + 1
		for j := range len(word2) {
			if word1[i] == word2[j] {
				curr[j+1] = prev[j]
			} else {
				curr[j+1] = min(prev[j]+1, prev[j+1]+1, curr[j]+1)
			}
		}
		prev = curr
	}
	return prev[len(word2)]
}
