func maxSumTrionic(nums []int) int64 {
	const NINF int64 = -1e15
	s0, s1, s2, ans := NINF, NINF, NINF, NINF
	for i := 1; i < len(nums); i++ {
		p, c := int64(nums[i-1]), int64(nums[i])
		ns0, ns1, ns2 := NINF, NINF, NINF
		if c > p {
			ns0 = max(s0, p) + c
			ns2 = max(s2, s1) + c
		} else if c < p {
			ns1 = max(s1, s0) + c
		}
		s0, s1, s2 = ns0, ns1, ns2
		ans = max(ans, s2)
	}
	return ans
}