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
    graph: Vec<Vec<usize>>,
    num: Vec<usize>,
    sn: Vec<usize>,
    visit: Vec<bool>,
    scc: usize,
    cnt: usize,
    stack: Vec<usize>,
}

impl TwoSAT {
    fn new(n: usize) -> Self {
        Self {
            graph: vec![vec![]; 2 * n + 1],
            num: vec![0; 2 * n + 1],
            sn: vec![0; 2 * n + 1],
            visit: vec![false; 2 * n + 1],
            scc: 0,
            cnt: 0,
            stack: vec![],
        }
    }

    fn add_edge(&mut self, u: i32, v: i32) {
        let i = if u > 0 { u as usize * 2 - 1 } else { -u as usize * 2 };
        let j = if v > 0 { v as usize * 2 - 1 } else { -v as usize * 2 };
        self.graph[if i % 2 == 0 { i - 1 } else { i + 1 }].push(j);
        self.graph[if j % 2 == 0 { j - 1 } else { j + 1 }].push(i);
    }

    fn dfs(&mut self, curr: usize) -> usize {
        self.cnt += 1;
        self.num[curr] = self.cnt;
        self.stack.push(curr);

        let mut ret = self.num[curr];
        for &next in &self.graph[curr].clone() {
            if self.num[next] == 0 { ret = ret.min(self.dfs(next)); }
            else if !self.visit[next] { ret = ret.min(self.num[next]); }
        }
        if ret == self.num[curr] {
            while let Some(top) = self.stack.pop() {
                self.sn[top] = self.scc;
                self.visit[top] = true;
                if top == curr { break; }
            }
            self.scc += 1;
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
    for i in 1..=2 * n {
        if ts.num[i] == 0 { ts.dfs(i); }
    }
    for i in 1..=n {
        if ts.sn[i * 2 - 1] == ts.sn[i * 2] {
            writeln!(so, "0").unwrap();
            return;
        }
    }
    writeln!(so, "1").unwrap();
}