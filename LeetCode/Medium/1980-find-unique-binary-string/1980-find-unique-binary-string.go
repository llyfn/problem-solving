func findDifferentBinaryString(nums []string) string {
	n := len(nums[0])
	set := make(map[int]bool)
	for _, i := range nums {
		v, _ := strconv.ParseInt(i, 2, 32)
		set[int(v)] = true
	}
	for i := 1 << (n - 1); i < 1<<n; i++{
		if !set[i] {
			s := strconv.FormatInt(int64(i), 2)
			return strings.Repeat("0", n-len(s)) + s
		}
	}
	if !set[0] {
		return strings.Repeat("0", n)
	}
	return ""
}
