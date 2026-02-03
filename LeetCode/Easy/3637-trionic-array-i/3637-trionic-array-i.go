func isTrionic(nums []int) bool {
	p, q := 0, len(nums) - 1
	for p < q && nums[p + 1] > nums[p] { p++ }
	for q > p && nums[q - 1] < nums[q] { q-- }
	if p == 0 || q == len(nums) - 1 { return false }
	for i := p; i < q; i++ { if nums[i] <= nums[i + 1] { return false } }
	return true
}