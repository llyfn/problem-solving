package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	var t, x, y int
	reader := bufio.NewReader(os.Stdin)
	for fmt.Fscan(reader, &t); t > 0; t-- {
		fmt.Fscan(reader, &x, &y)
		fmt.Println(int(2*math.Sqrt(float64(y-x)) - 1e-9))
	}
}
