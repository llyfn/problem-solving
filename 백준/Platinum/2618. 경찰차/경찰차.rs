use std::io::*;

struct Scanner { it: std::str::SplitAsciiWhitespace<'static>, }
impl Scanner {
    fn new() -> Self {
        let mut s = String::new();
        stdin().read_to_string(&mut s).ok();
        Self { it: s.leak().split_ascii_whitespace() }
    }
    fn read<T: std::str::FromStr>(&mut self) -> T {
        self.it.next().unwrap().parse::<T>().ok().unwrap()
    }
}

struct Dp { n: usize, w: usize, p: Vec<(usize, usize)>, dp: Vec<Vec<isize>>, trace: Vec<Vec<isize>> }

impl Dp {
    fn new(n: usize, w: usize, p: Vec<(usize, usize)>) -> Self {
        let dp = vec![vec![-1; w]; w];
        let trace = vec![vec![-1; w]; w];
        Self { n, w, p, dp, trace }
    }

    fn dist(&mut self, i: usize, j: usize) -> usize {
        self.p[i].0.abs_diff(self.p[j].0) + self.p[i].1.abs_diff(self.p[j].1)
    }

    fn solve(&mut self, i: usize, j: usize) -> isize {
        let next = i.max(j) + 1;
        if next >= self.w { return 0; }

        if self.dp[i][j] != -1 { return self.dp[i][j] }
        let d1 = self.dist(i, next) as isize + self.solve(next, j);
        let d2 = self.dist(j, next) as isize + self.solve(i, next);
        if d1 < d2 {
            self.trace[i][j] = 1;
            self.dp[i][j] = d1;
        } else {
            self.trace[i][j] = 2;
            self.dp[i][j] = d2;
        }
        self.dp[i][j]
    }
}

fn main() {
    let mut sc = Scanner::new();
    let mut so = BufWriter::new(stdout().lock());

    let n: usize = sc.read();
    let w: usize = sc.read();

    let mut p: Vec<(usize, usize)> = vec![(1, 1), (n, n)];
    for _ in 0..w { p.push((sc.read::<usize>(), sc.read::<usize>())); }

    let mut dp = Dp::new(n, w + 2, p);
    writeln!(so, "{}", dp.solve(0, 1)).ok();

    let (mut i, mut j) = (0, 1);
    for k in 2..w + 2 {
        writeln!(so, "{}", dp.trace[i][j]).ok();
        if dp.trace[i][j] == 1 { i = k; } else { j = k; }
    }
}