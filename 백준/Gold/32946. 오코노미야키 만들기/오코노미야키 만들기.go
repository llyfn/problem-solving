package main

import (
	"bufio"
	"fmt"
	"os"
)

func abs(x int) int {
	if x < 0 { return -x }
	return x
}

func solve(n, p1, p2, m, s int) int {
	if p1 > p2 { p1, p2 = p2, p1 }
	m1, m2 := (p1-m)%2 == 0, (p2-m)%2 == 0
	l, h, ans := min(m, s), max(m, s), -1
	if m1 && m2 { return -1 }
	if !m1 {
		v := max(0, h-p2+1)
		if v == 0 || h < n && (m2 || h != m) { ans = abs(m-p1) + abs(s-m) + v }
	}
	if !m2 {
		v := max(0, p1-l+1)
		if v == 0 || l > 1 && (m1 || l != m) {
			c := abs(m-p2) + abs(s-m) + v
			if ans == -1 || ans > c { ans = c }
		}
	}
	return ans
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n, p1, p2, m, s int
	fmt.Fscan(reader, &n, &p1, &p2, &m, &s)
	fmt.Println(solve(n, p1, p2, m, s))
}
