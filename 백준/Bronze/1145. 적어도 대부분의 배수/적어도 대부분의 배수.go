package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var nums [5]int
	for i := 0; i < 5; i++ {
		fmt.Fscan(reader, &nums[i])
	}
	ans := 1
	for {
		cnt := 0
		for i := 0; i < 5; i++ {
			if ans%nums[i] == 0 {
				cnt++
			}
		}
		if cnt >= 3 {
			fmt.Println(ans)
			break
		}
		ans++
	}
}
