package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var b string
	ans := 0
	for i := 0; i < 8; i++ {
		fmt.Fscan(reader, &b)
		for j := 0; j < 4; j++ {
			if b[2 * j + i % 2] == 'F' {
				ans++
			}
		}
	}
	fmt.Println(ans)
}
