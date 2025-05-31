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

struct Articulation {
    v: usize,
    e: usize,
    graph: Vec<Vec<usize>>,
    cnt: usize,
    ap: Vec<bool>,
    disc: Vec<usize>,
}

impl Articulation {
    fn new(v: usize, e: usize) -> Self {
        Self { v, e, graph: vec![vec![]; v], cnt: 0, ap: vec![false; v], disc: vec![0; v] }
    }

    fn add_edge(&mut self, u: usize, v: usize) {
        self.graph[u].push(v);
        self.graph[v].push(u);
    }

    fn dfs(&mut self, curr: usize, is_root: bool) -> usize {
        self.cnt += 1;
        self.disc[curr] = self.cnt;
        let mut children = 0;
        let mut ret = self.disc[curr];

        for &next in &self.graph[curr].clone() {
            if self.disc[next] == 0 { // not visited
                children += 1;
                let low = self.dfs(next, false);
                ret = ret.min(low);

                if !is_root && self.disc[curr] <= low { self.ap[curr] = true; }
            } else {
                ret = ret.min(self.disc[next]);
            }
        }
        if is_root && children > 1 { self.ap[curr] = true; }
        ret
    }
}

fn main() {
    let mut sc = Scanner::new();
    let mut so = BufWriter::new(stdout().lock());

    let v: usize = sc.read();
    let e: usize = sc.read();
    let mut a = Articulation::new(v, e);
    for _ in 0..e { a.add_edge(sc.read::<usize>() - 1, sc.read::<usize>() - 1); }
    for i in 0..v { if a.disc[i] == 0 { a.dfs(i, true); } }
    let mut ap_count = 0;
    for i in 0..v { if a.ap[i] { ap_count += 1; } }
    writeln!(so, "{}", ap_count).unwrap();
    for i in 0..v { if a.ap[i] { write!(so, "{} ", i + 1).unwrap(); } }
}
