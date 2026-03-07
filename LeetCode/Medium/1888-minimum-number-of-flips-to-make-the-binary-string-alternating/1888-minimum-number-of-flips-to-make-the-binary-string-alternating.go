func minFlips(s string) int {
	n := len(s)
	e, o := (n+1)/2, n/2
	x := 0
	for i, c := range s {
		if c == '1' {
			if i%2 == 0 {
				x++
			} else {
				x--
			}
		}
	}
	res := min(e-x, o+x)
	if n%2 != 0 {
		for _, c := range s {
			x = 2*(int(c)&1) - x
			res = min(res, min(e-x, o+x))
		}
	}
	return res
}