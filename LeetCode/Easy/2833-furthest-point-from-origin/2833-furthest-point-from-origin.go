func furthestDistanceFromOrigin(moves string) int {
	pos, x := 0, 0
	for _, m := range moves {
		switch m {
		case 'L':
			pos--
		case 'R':
			pos++
		default:
			x++
		}
	}
	return max(x-pos, x+pos)
}