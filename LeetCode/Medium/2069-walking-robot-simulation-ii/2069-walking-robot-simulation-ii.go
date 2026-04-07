type Robot struct {
	moved        bool
	pos, w, h, m int
}

func Constructor(width int, height int) Robot {
	return Robot{false, 0, width, height, 2*(width+height) - 4}
}

func (r *Robot) Step(num int) {
    r.moved = true
	r.pos = (r.pos + num) % r.m
}

func (r *Robot) GetPos() []int {
	if r.pos < r.w {
		return []int{r.pos, 0}
	} else if r.pos < r.w+r.h-1 {
		return []int{r.w - 1, r.pos - r.w + 1}
	} else if r.pos < 2*r.w+r.h-2 {
		return []int{r.m - r.h - r.pos + 1, r.h - 1}
	}
	return []int{0, r.m - r.pos}
}

func (r *Robot) GetDir() string {
	if r.moved && r.pos == 0 {
		return "South"
	} else if r.pos < r.w {
		return "East"
	} else if r.pos < r.w+r.h-1 {
		return "North"
	} else if r.pos < 2*r.w+r.h-2 {
		return "West"
	}
	return "South"
}