func decodeCiphertext(encodedText string, rows int) string {
	cols := len(encodedText) / rows
	var ans []byte
	for d := 0; d < cols; d++ {
		for i, j := 0, d; i*cols+j < len(encodedText); i, j = i+1, j+1 {
			ans = append(ans, encodedText[i*cols+j])
		}
	}
	return strings.TrimRight(string(ans), " ")
}
