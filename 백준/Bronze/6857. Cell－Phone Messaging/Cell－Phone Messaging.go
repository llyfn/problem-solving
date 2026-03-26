package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	m := "2122233132334142435152536162637172737481828391929394"
	for {
		s, _ := reader.ReadString('\n')
		word := strings.TrimSpace(s)
		if word == "halt" || word == "" {
			break
		}
		ans, l := 0, -1
		for _, c := range word {
			k, p := int(m[(c-'a')*2]-'0'), int(m[(c-'a')*2+1]-'0')
			ans += p
			if k == l {
				ans += 2
			}
			l = k
		}
		fmt.Println(ans)
	}
}
