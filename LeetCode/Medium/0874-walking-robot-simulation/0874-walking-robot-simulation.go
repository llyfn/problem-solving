func robotSim(commands []int, obstacles [][]int) int {
	var dir, x, y, ans, nx, ny int
	obs := make(map[[2]int]bool)
	for _, o := range obstacles {
		obs[[2]int{o[0], o[1]}] = true
	}
	for _, c := range commands {
		if c == -2 {
			dir = ((dir-1)%4 + 4) % 4
		} else if c == -1 {
			dir = (dir + 1) % 4
		} else {
			for i := 0; i < c; i++ {
				switch dir {
				case 0:
					nx, ny = x, y+1
				case 1:
					nx, ny = x+1, y
				case 2:
					nx, ny = x, y-1
				case 3:
					nx, ny = x-1, y
				}
				if obs[[2]int{nx, ny}] { 
					break
				}
				x, y = nx, ny
				ans = max(ans, x*x+y*y)
			}
		}
	}
	return ans
}