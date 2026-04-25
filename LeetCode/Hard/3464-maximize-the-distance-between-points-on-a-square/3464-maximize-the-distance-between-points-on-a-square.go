func maxDistance(side int, points [][]int, k int) int {
	n := len(points)
	perim := make([]int, n)
	for i, p := range points {
		x, y := p[0], p[1]
		var d int
		if y == 0 {
			d = x
		} else if x == side {
			d = side + y
		} else if y == side {
			d = 2*side + (side - x)
		} else {
			d = 3*side + (side - y)
		}
		perim[i] = d
	}
	sort.Ints(perim)
	total := 4 * side

	ext := make([]int, 2*n)
	for i := 0; i < n; i++ {
		ext[i] = perim[i]
		ext[i+n] = perim[i] + total
	}

	check := func(mid int) bool {
		for start := 0; start < n; start++ {
			cur := start
			ok := true
			for c := 1; c < k; c++ {
				target := ext[cur] + mid
				lo, hi := cur+1, start+n-1
				if lo > hi {
					ok = false
					break
				}
				best := -1
				for lo <= hi {
					m := (lo + hi) / 2
					if ext[m] >= target {
						best = m
						hi = m - 1
					} else {
						lo = m + 1
					}
				}
				if best == -1 {
					ok = false
					break
				}
				gap := ext[best] - ext[cur]
				if total-gap < mid {
					ok = false
					break
				}
				cur = best
			}
			if ok {
				wrapGap := ext[start+n] - ext[cur]
				m := wrapGap
				if total-wrapGap < m {
					m = total - wrapGap
				}
				if m >= mid {
					return true
				}
			}
		}
		return false
	}

	lo, hi := 0, 2*side
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if check(mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}