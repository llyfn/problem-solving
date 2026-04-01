type Robot struct {
	id       int
	position int
	health   int
	dir      byte
}

func survivedRobotsHealths(positions, healths []int, directions string) []int {
	n := len(positions)
	robots := make([]Robot, n)
	for i := 0; i < n; i++ {
		robots[i] = Robot{
			id:       i,
			position: positions[i],
			health:   healths[i],
			dir:      directions[i],
		}
	}
	sort.Slice(robots, func(i, j int) bool {
		return robots[i].position < robots[j].position
	})
	var stack []int
	for i := 0; i < n; i++ {
		if robots[i].dir == 'R' {
			stack = append(stack, i)
			continue
		}
		for len(stack) > 0 && robots[i].health > 0 {
			topIdx := stack[len(stack)-1]

			if robots[topIdx].dir == 'R' {
				if robots[topIdx].health > robots[i].health {
					robots[topIdx].health -= 1
					robots[i].health = 0
				} else if robots[topIdx].health < robots[i].health {
					robots[i].health -= 1
					robots[topIdx].health = 0
					stack = stack[:len(stack)-1]
				} else {
					robots[i].health = 0
					robots[topIdx].health = 0
					stack = stack[:len(stack)-1]
				}
			} else {
				break
			}
		}
	}
	sort.Slice(robots, func(i, j int) bool {
		return robots[i].id < robots[j].id
	})
	var result []int
	for _, r := range robots {
		if r.health > 0 {
			result = append(result, r.health)
		}
	}
	return result
}