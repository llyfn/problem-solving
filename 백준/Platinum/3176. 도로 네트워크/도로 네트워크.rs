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

struct Network {
    n: usize,
    graph: Vec<Vec<(usize, usize)>>,
    parents: Vec<Vec<usize>>,
    min_dist: Vec<Vec<usize>>,
    max_dist: Vec<Vec<usize>>,
    depths: Vec<usize>,
}

impl Network {
    fn new(n: usize) -> Self {
        let graph = vec![vec![]; n + 1];
        let parents = vec![vec![0; 20]; n + 1];
        let depths = vec![0; n + 1];
        let min_dist = vec![vec![1000001; 20]; n + 1];
        let max_dist = vec![vec![0; 20]; n + 1];
        Self { n, graph, parents, min_dist, max_dist, depths }
    }

    fn add_edge(&mut self, u: usize, v: usize, w: usize) {
        self.graph[u].push((v, w));
        self.graph[v].push((u, w));
    }

    fn find_parent(&mut self, curr: usize, parent: usize, depth: usize, cost: usize) {
        self.parents[curr][0] = parent;
        self.min_dist[curr][0] = cost;
        self.max_dist[curr][0] = cost;
        self.depths[curr] = depth;
        for &(next, d) in &self.graph[curr].clone() {
            if next != parent { self.find_parent(next, curr, depth + 1, d); }
        }
    }

    fn init_dist(&mut self) {
        for i in 1..20 {
            for j in 2..=self.n {
                if self.parents[j][i - 1] != 0 {
                    self.parents[j][i] = self.parents[self.parents[j][i - 1]][i - 1];
                    self.min_dist[j][i] = self.min_dist[j][i - 1].min(self.min_dist[self.parents[j][i - 1]][i - 1]);
                    self.max_dist[j][i] = self.max_dist[j][i - 1].max(self.max_dist[self.parents[j][i - 1]][i - 1]);
                }
            }
        }
    }

    fn find_dist(&mut self, mut u: usize, mut v: usize) -> (usize, usize) {
        if self.depths[u] < self.depths[v] { return self.find_dist(v, u); }
        let (mut min_d, mut max_d) = (1000001, 0);
        let diff = self.depths[u] - self.depths[v];
        for i in 0..20 {
            if (diff & 1 << i) != 0 {
                min_d = min_d.min(self.min_dist[u][i]);
                max_d = max_d.max(self.max_dist[u][i]);
                u = self.parents[u][i];
            }
        }
        if u != v {
            for i in (0..20).rev() {
                if self.parents[u][i] != self.parents[v][i] && self.parents[u][i] != 0 {
                    min_d = min_d.min(self.min_dist[u][i]).min(self.min_dist[v][i]);
                    max_d = max_d.max(self.max_dist[u][i]).max(self.max_dist[v][i]);
                    u = self.parents[u][i];
                    v = self.parents[v][i];
                }
            }
            min_d = min_d.min(self.min_dist[u][0]).min(self.min_dist[v][0]);
            max_d = max_d.max(self.max_dist[u][0]).max(self.max_dist[v][0]);
        }
        (min_d, max_d)
    }
}

fn main() {
    let mut sc = Scanner::new();
    let mut so = BufWriter::new(stdout().lock());

    let n: usize = sc.read();
    let mut nw = Network::new(n);

    for _ in 0..n - 1 { nw.add_edge(sc.read(), sc.read(), sc.read()); }

    nw.find_parent(1, 0, 0, 0);
    nw.init_dist();

    let k: usize = sc.read();

    for _ in 0..k {
        let (min, max) = nw.find_dist(sc.read(), sc.read());
        writeln!(so, "{} {}", min, max).ok();
    }
}