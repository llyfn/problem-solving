func numSteps(s string) int {
	n := len(s)
	cnt := 0
	c := 0
	for i := n - 1; i > 0; i-- {
		d := int(s[i]) + c
		if d & 1 == 1 {
			cnt += 2
			c = 1
		} else {
			cnt++
		}
	}
	return cnt + c
}