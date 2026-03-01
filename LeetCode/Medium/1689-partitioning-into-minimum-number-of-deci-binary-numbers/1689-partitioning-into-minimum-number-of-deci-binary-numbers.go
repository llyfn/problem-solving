func minPartitions(n string) (m int) {
	for _, c := range n {
		if int(c-'0') > m {
			m = int(c - '0')
		}
	}
	return
}