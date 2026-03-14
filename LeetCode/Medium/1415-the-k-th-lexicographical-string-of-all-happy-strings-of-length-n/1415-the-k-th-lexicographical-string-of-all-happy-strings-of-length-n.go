func getHappyString(n int, k int) string {
	var ans string
	var bt func(string)
	bt = func(str string) {
		if len(ans) > 0 || len(str) > n { return }
		if len(str) == n {
			k--
			if k == 0 {
				ans = str
			}
			return
		}
		for _, c := range "abc" {
			sc := string(c)
			if len(str) == 0 || str[len(str)-1:] != sc {
				bt(str + sc)
			}
		}
	}
	bt("")
	return ans
}