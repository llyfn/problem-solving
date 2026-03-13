type DSU struct {
	parent []int
}

func NewDSU(n int) *DSU {
	p := make([]int, n)
	for i := range p {
		p[i] = i
	}
	return &DSU{parent: p}
}

func (d *DSU) Find(i int) int {
	if d.parent[i] == i {
		return i
	}
	d.parent[i] = d.Find(d.parent[i])
	return d.parent[i]
}

func (d *DSU) Union(i, j int) bool {
	rootI := d.Find(i)
	rootJ := d.Find(j)
	if rootI != rootJ {
		d.parent[rootI] = rootJ
		return true
	}
	return false
}

func maxStability(n int, edges [][]int, k int) int {
	var required [][]int
	var optional [][]int
	mustMin := -1
	high := 0

	for _, e := range edges {
		v := e[2]
		if e[3] == 0 {
			optional = append(optional, e)
			v *= 2
		} else {
			required = append(required, e)
			if mustMin == -1 || e[2] < mustMin {
				mustMin = e[2]
			}
		}
		if v > high {
			high = v
		}
	}

	if mustMin != -1 && mustMin < high {
		high = mustMin
	}

	dsu1 := NewDSU(n)
	for _, e := range required {
		if !dsu1.Union(e[0], e[1]) {
			return -1
		}
	}

	dsu2 := NewDSU(n)
	comps2 := n
	for _, e := range edges {
		if dsu2.Union(e[0], e[1]) {
			comps2--
		}
	}
	if comps2 > 1 {
		return -1
	}

	ans := -1
	low := 0

	for low <= high {
		mid := low + (high-low)/2
		if check(n, required, optional, mid, k) {
			ans = mid
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	return ans
}

func check(n int, required, optional [][]int, mid, k int) bool {
	dsu := NewDSU(n)
	comps := n

	for _, e := range required {
		if dsu.Union(e[0], e[1]) {
			comps--
		}
	}

	for _, e := range optional {
		if e[2] >= mid {
			if dsu.Union(e[0], e[1]) {
				comps--
			}
		}
	}

	upgrades := 0
	for _, e := range optional {
		if e[2] < mid && e[2]*2 >= mid {
			if dsu.Union(e[0], e[1]) {
				comps--
				upgrades++
			}
		}
	}

	return comps == 1 && upgrades <= k
}