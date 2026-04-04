func maxWalls(robots []int, distance []int, walls []int) int {
	n := len(robots)
	if n == 0 || len(walls) == 0 {
		return 0
	}
	order := make([]int, n)
	for i := range order {
		order[i] = i
	}
	sort.Slice(order, func(a, b int) bool {
		return robots[order[a]] < robots[order[b]]
	})
	pos := make([]int, n)
	dst := make([]int, n)
	for i, j := range order {
		pos[i] = robots[j]
		dst[i] = distance[j]
	}
	sort.Ints(walls)
	rset := make(map[int]bool)
	for _, p := range pos {
		rset[p] = true
	}
	always := 0
	var ws []int
	for _, w := range walls {
		if rset[w] {
			always++
		} else {
			ws = append(ws, w)
		}
	}
	if len(ws) == 0 {
		return always
	}
	cnt := func(lo, hi int) int {
		if lo > hi {
			return 0
		}
		return sort.SearchInts(ws, hi+1) - sort.SearchInts(ws, lo)
	}
	seg0 := cnt(pos[0]-dst[0], pos[0]-1)
	segN := cnt(pos[n-1]+1, pos[n-1]+dst[n-1])
	dpL, dpR := seg0, 0
	for i := 1; i < n; i++ {
		lo, hi := pos[i-1]+1, pos[i]-1
		var lv, rv, bv int
		if lo <= hi {
			rr := min(pos[i-1]+dst[i-1], hi)
			ll := max(pos[i]-dst[i], lo)
			lv = cnt(lo, rr)
			rv = cnt(ll, hi)
			if rr >= ll {
				bv = cnt(lo, hi)
			} else {
				bv = lv + rv
			}
		}
		dpL, dpR = max(dpR+bv, dpL+rv), max(dpR+lv, dpL)
	}
	return max(dpL, dpR+segN) + always
}
