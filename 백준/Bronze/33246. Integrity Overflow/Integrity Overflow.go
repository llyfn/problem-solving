package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n)
	var secret string
	fmt.Fscan(reader, &secret)
	secure := true
	for i := 0; i < n; i++ {
		var pw, res string
		fmt.Fscan(reader, &pw)
		fmt.Fscan(reader, &res)
		pass := true
		if len(pw) != len(secret) {
			pass = false
		} else {
			cnt := 0
			for j := 0; j < len(pw); j++ {
				if pw[j] != secret[j] {
					cnt++
				}
				if cnt > 1 {
					pass = false
					break
				}
			}
		}
		if pass != (res == "ALLOWED") {
			secure = false
			break
		}
	}
	if secure {
		fmt.Println("SYSTEM SECURE")
	} else {
		fmt.Println("INTEGRITY OVERFLOW")
	}
	
}
