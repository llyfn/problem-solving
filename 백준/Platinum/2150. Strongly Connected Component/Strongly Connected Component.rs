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

struct Tarjan {
    graph: Vec<Vec<usize>>,
    scc: Vec<Vec<usize>>,
    num: Vec<usize>,
    low: Vec<usize>,
    visit: Vec<bool>,
    cnt: usize,
    stack: Vec<usize>,
}

impl Tarjan {
    fn new(v: usize) -> Self {
        Self {
            graph: vec![Vec::new(); v + 1],
            scc: Vec::new(),
            num: vec![0; v + 1],
            low: vec![0; v + 1],
            visit: vec![false; v + 1],
            cnt: 0,
            stack: Vec::new(),
        }
    }

    fn dfs(&mut self, curr: usize) {
        self.visit[curr] = true;
        self.stack.push(curr);
        self.cnt += 1;
        self.num[curr] = self.cnt;
        self.low[curr] = self.cnt;
        for next in self.graph[curr].clone() {
            if self.num[next] == 0 {
                self.dfs(next);
                self.low[curr] = self.low[curr].min(self.low[next]);
            } else if self.visit[next] {
                self.low[curr] = self.low[curr].min(self.num[next]);
            }
        }
        if self.low[curr] == self.num[curr] {
            let mut scc = Vec::new();
            while let Some(top) = self.stack.pop() {
                self.visit[top] = false;
                scc.push(top);
                if top == curr { break; }
            }
            scc.sort();
            self.scc.push(scc);
        }
    }
}

fn main() {
    let mut sc = Scanner::new();
    let mut so = BufWriter::new(stdout().lock());
    let mut v: usize = sc.read();
    let mut e: usize = sc.read();

    let mut tarjan = Tarjan::new(v);
    for _ in 0..e { tarjan.graph[sc.read::<usize>()].push(sc.read::<usize>()); }
    for i in 1..=v { if tarjan.num[i] == 0 { tarjan.dfs(i); } }
    tarjan.scc.sort();

    writeln!(so, "{}", tarjan.scc.len()).ok();
    for scc in &tarjan.scc {
        for &node in scc { write!(so, "{} ", node).ok(); }
        writeln!(so, "{}", -1).ok();
    }
}