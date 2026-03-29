package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var c1, c2, c3 string
	v := map[string]int{"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
	fmt.Fscan(reader, &c1, &c2, &c3)
	ans := v[c1] * 10 + v[c2]
	for i := 0; i < v[c3]; i++ {
		ans *= 10
	}
	fmt.Println(ans)
}
