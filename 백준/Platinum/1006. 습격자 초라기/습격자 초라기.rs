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

struct Chinchou {
    n: usize,
    w: usize,
    e: Vec<(usize, usize)>,
    a: Vec<usize>,
    b: Vec<usize>,
    c: Vec<usize>,
}

impl Chinchou {
    fn new(n: usize, w: usize) -> Self {
        Self {
            n,
            w,
            e: vec![(0, 0); n],
            a: vec![0; n + 1],
            b: vec![0; n],
            c: vec![0; n],
        }
    }

    fn solve(&mut self, s: usize) {
        for i in s..self.n {
            self.a[i + 1] = self.b[i].min(self.c[i]) + 1;
            if self.e[i].0 + self.e[i].1 <= self.w {
                self.a[i + 1] = self.a[i + 1].min(self.a[i] + 1);
            }
            if i > 0 && self.e[i - 1].0 + self.e[i].0 <= self.w && self.e[i - 1].1 + self.e[i].1 <= self.w {
                self.a[i + 1] = self.a[i + 1].min(self.a[i - 1] + 2);
            }
            if i < self.n - 1 {
                self.b[i + 1] = self.a[i + 1] + 1;
                if self.e[i].0 + self.e[i + 1].0 <= self.w {
                    self.b[i + 1] = self.b[i + 1].min(self.c[i] + 1);
                }
                self.c[i + 1] = self.a[i + 1] + 1;
                if self.e[i].1 + self.e[i + 1].1 <= self.w {
                    self.c[i + 1] = self.c[i + 1].min(self.b[i] + 1);
                }
            }
        }
    }
}

fn main() {
    let mut sc = Scanner::new();
    let mut so = BufWriter::new(stdout().lock());

    let t: usize = sc.read();
    for _ in 0..t {
        let n: usize = sc.read();
        let w: usize = sc.read();
        let mut cc = Chinchou::new(n, w);
        let mut res = 30001;

        for i in 0..n { cc.e[i].0 = sc.read(); }
        for i in 0..n { cc.e[i].1 = sc.read(); }

        cc.b[0] = 1;
        cc.c[0] = 1;
        cc.solve(0);
        res = res.min(cc.a[n]);

        if n > 1 && cc.e[0].0 + cc.e[n-1].0 <= w {
            cc.a[1] = 1;
            cc.b[1] = 2;
            cc.c[1] = if cc.e[0].1 + cc.e[1].1 <= w { 1 } else { 2 };
            cc.solve(1);
            res = res.min(cc.c[n - 1] + 1);
        }
        if n > 1 && cc.e[0].1 + cc.e[n-1].1 <= w {
            cc.a[1] = 1;
            cc.b[1] = if cc.e[0].0 + cc.e[1].0 <= w { 1 } else { 2 };
            cc.c[1] = 2;
            cc.solve(1);
            res = res.min(cc.b[n - 1] + 1);
        }

        if n > 1 && cc.e[0].0 + cc.e[n-1].0 <= w && cc.e[0].1 + cc.e[n-1].1 <= w {
            cc.a[1] = 0;
            cc.b[1] = 1;
            cc.c[1] = 1;
            cc.solve(1);
            res = res.min(cc.a[n - 1] + 2);
        }

        writeln!(so, "{}", res).ok();
    }
}
