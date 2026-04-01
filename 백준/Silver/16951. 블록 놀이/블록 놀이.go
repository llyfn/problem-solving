package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n, k int
	fmt.Fscan(reader, &n, &k)
	a := make([]int, n)
	for i := range a {
		fmt.Fscan(reader, &a[i])
	}
	ans := 1001
	for i, p := range a {
		if p - i * k <= 0 {
			continue
		}
		t := 0
		for j, v := range a {
			if v != p + (j - i) * k {
				t++
			}
		}
		ans = min(t, ans)
	}
	fmt.Println(ans)
}
