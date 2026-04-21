func minimumHammingDistance(source []int, target []int, allowedSwaps [][]int) int {
	n := len(source)
	parent := make([]int, n)
	for i := range parent {
		parent[i] = i
	}

	var find func(x int) int
	find = func(x int) int {
		if parent[x] != x {
			parent[x] = find(parent[x])
		}
		return parent[x]
	}

	union := func(a, b int) {
		pa, pb := find(a), find(b)
		if pa != pb {
			parent[pa] = pb
		}
	}

	for _, swap := range allowedSwaps {
		union(swap[0], swap[1])
	}

	groups := make(map[int][]int)
	for i := 0; i < n; i++ {
		root := find(i)
		groups[root] = append(groups[root], i)
	}

	hamming := 0
	for _, indices := range groups {
		freq := make(map[int]int)
		for _, idx := range indices {
			freq[source[idx]]++
		}
		for _, idx := range indices {
			if freq[target[idx]] > 0 {
				freq[target[idx]]--
			} else {
				hamming++
			}
		}
	}

	return hamming
}