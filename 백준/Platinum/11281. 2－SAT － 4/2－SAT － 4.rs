use std::io::*;
use std::collections::HashMap;

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

struct TwoSAT {
    n: usize,
    graph: Vec<Vec<usize>>,
    num: Vec<usize>,
    scc: Vec<usize>,
    fin: Vec<bool>,
    cnt: usize,
    scc_cnt: usize,
    stack: Vec<usize>,
}

impl TwoSAT {
    fn new(n: usize) -> Self {
        Self {
            n,
            graph: vec![vec![]; 2 * n],
            num: vec![usize::MAX; 2 * n],
            scc: vec![usize::MAX; 2 * n],
            fin: vec![false; 2 * n + 1],
            cnt: 0,
            scc_cnt: 0,
            stack: vec![],
        }
    }

    fn conv(&mut self, x: i32) -> usize {
        if x > 0 { (x - 1) as usize } else { self.n - 1 + (-x as usize) }
    }

    fn neg(&mut self, x: usize) -> usize { (x + self.n) % (2 * self.n) }

    fn add_edge(&mut self, u: i32, v: i32) {
        let (i, j) = (self.conv(u), self.conv(v));
        let (ni, nj) = (self.neg(i), self.neg(j));
        self.graph[ni].push(j);
        self.graph[nj].push(i);
    }

    fn dfs(&mut self, curr: usize) -> usize {
        self.num[curr] = self.cnt;
        self.cnt += 1;
        self.stack.push(curr);

        let mut ret = self.num[curr];
        for &next in &self.graph[curr].clone() {
            if self.fin[next] { continue; }
            if self.num[next] < usize::MAX { ret = ret.min(self.num[next]); }
            else { ret = ret.min(self.dfs(next)); }
        }
        if ret == self.num[curr] {
            while let Some(top) = self.stack.pop() {
                self.scc[top] = self.scc_cnt;
                self.fin[top] = true;
                if top == curr { break; }
            }
            self.scc_cnt += 1;
        }
        ret
    }
}

fn main() {
    let mut sc = Scanner::new();
    let mut so = BufWriter::new(stdout().lock());

    let (n, m): (usize, usize) = (sc.read(), sc.read());
    let mut ts = TwoSAT::new(n);
    for _ in 0..m {
        let (u, v): (i32, i32) = (sc.read(), sc.read());
        ts.add_edge(u, v);
    }
    for i in 0..2 * n {
        if !ts.fin[i] { ts.dfs(i); }
    }
    let mut ans = vec![0; n];
    for i in 0..n {
        let j = ts.neg(i);
        if ts.scc[i] == ts.scc[j] {
            writeln!(so, "0").unwrap();
            return;
        }
        if ts.scc[i] < ts.scc[j] { ans[i] = 1; }
    }
    writeln!(so, "1").unwrap();
    for i in 0..n {
        write!(so, "{} ", ans[i]).unwrap();
    }
}