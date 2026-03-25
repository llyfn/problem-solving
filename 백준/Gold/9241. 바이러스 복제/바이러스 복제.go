package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var p, c string
	reader := bufio.NewReader(os.Stdin)
	fmt.Fscan(reader, &p, &c)
	n, m := len(p), len(c)
	l, r := 0, 0
	for ; l < min(n, m) && p[l] == c[l]; l++ {}
	for ; r < min(n, m)-l && p[n-r-1] == c[m-r-1]; r++ {}
	fmt.Println(max(0, m-r-l))
}
