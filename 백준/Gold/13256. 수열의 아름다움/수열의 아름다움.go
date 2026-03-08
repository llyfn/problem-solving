package main

import (
	"bufio"
	"fmt"
	"os"
)

func f(x, y float64) float64 {
	if x > y {
		x, y = y, x
	}
	return (x + 1) / 6 * (x * (2 * x + 1) + 3 * y * (y - x + 1))
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n)
	ans := 0.0
	var l1, h1, l2, h2 float64
	fmt.Fscan(reader, &l1, &h1)
	for i := 0; i < n - 1; i++ {
		fmt.Fscan(reader, &l2, &h2)
		ans += (f(h1, h2) - f(l1 - 1, h2) - f(h1, l2 - 1) + f(l1 - 1, l2 - 1)) / (h1 - l1 + 1) / (h2 - l2 + 1)
		l1, h1 = l2, h2
	}
	fmt.Println(ans)
}
