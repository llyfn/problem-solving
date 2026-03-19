package main

import (
	"bufio"
	"fmt"
	"os"
)

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var t, p, q, n int
	fmt.Fscan(reader, &t)
	for i := 0; i < t; i++ {
		fmt.Fscan(reader, &p, &q, &n)
		g := gcd(p, q)
		if n%g != 0 {
			fmt.Println("R")
			continue
		}
		p, q, n = p/g, q/g, n/g
		if (p < q && n < p && n%(q-p) == 0) || (p > q && (n < p || n%p >= q || (n%p)%(p-q) != 0)) {
			fmt.Println("P")
		} else {
			fmt.Println("E")
		}
	}
	fmt.Println()
}
