package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readPhoneNumber(num, f string) string {
	var words = []string{"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
	var multipliers = []string{"", "", "double", "triple", "quadruple", "quintuple", "sextuple", "septuple", "octuple", "nonuple", "decuple"}
	var result []string
	parts := strings.Split(f, "-")
	idx := 0
	for _, f := range parts {
		length, _ := strconv.Atoi(f)
		if idx+length > len(num) {
			break
		}
		chunk := num[idx : idx+length]
		idx += length
		i := 0
		for i < len(chunk) {
			digit := chunk[i]
			count := 1
			for i+count < len(chunk) && chunk[i+count] == digit {
				count++
			}
			word := words[int(digit - '0')]
			if count > 10 {
				for j := 0; j < count; j++ {
					result = append(result, word)
				}
			} else if count == 1 {
				result = append(result, word)
			} else {
				result = append(result, multipliers[count], word)
			}
			i += count
		}
	}
	return strings.Join(result, " ")
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var tc int
	fmt.Fscan(reader, &tc)
	for t := 0; t < tc; t++ {
		var num string
		fmt.Fscan(reader, &num)
		var f string
		fmt.Fscan(reader, &f)
		fmt.Printf("Case #%d: %s\n", t+1, readPhoneNumber(num, f))
	}
}
