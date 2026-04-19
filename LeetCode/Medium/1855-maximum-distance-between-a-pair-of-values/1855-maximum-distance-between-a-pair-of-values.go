func maxDistance(nums1, nums2 []int) int {
	var f func(int, int) int
	f = func(i, j int) int {
		if i >= j || i >= len(nums1) || j < 0 {
			return 0
		}
		if nums1[i] <= nums2[j] {
			return j - i
		}
		return max(f(i, j-1), f(i+1, j))
	}
	return f(0, len(nums2)-1)
}