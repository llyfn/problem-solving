const mod = 1_000_000_007

type Fancy struct {
	v []int
	a int
	b int
}

func Constructor() Fancy {
	return Fancy{
		v: []int{},
		a: 1,
		b: 0,
	}
}

func quickMul(x, y int) int {
	ret := 1
	cur := x
	for y > 0 {
		if y&1 != 0 {
			ret = (ret * cur) % mod
		}
		cur = (cur * cur) % mod
		y >>= 1
	}
	return ret
}

func inv(x int) int {
	return quickMul(x, mod-2)
}

func (f *Fancy) Append(val int) {
	f.v = append(f.v, ((val-f.b+mod)%mod)*inv(f.a)%mod)
}

func (f *Fancy) AddAll(inc int) {
	f.b = (f.b + inc) % mod
}

func (f *Fancy) MultAll(m int) {
	f.a = (f.a * m) % mod
	f.b = (f.b * m) % mod
}

func (f *Fancy) GetIndex(idx int) int {
	if idx >= len(f.v) {
		return -1
	}
	return (f.a*f.v[idx]%mod + f.b) % mod
}
