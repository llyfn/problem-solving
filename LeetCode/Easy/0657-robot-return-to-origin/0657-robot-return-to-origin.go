func judgeCircle(moves string) bool {
	return strings.Count(moves, "U") == strings.Count(moves, "D") &&
		strings.Count(moves, "L") == strings.Count(moves, "R")
}