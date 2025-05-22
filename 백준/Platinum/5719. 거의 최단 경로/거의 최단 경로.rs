use std::collections::VecDeque;
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

struct ASP {
    graph: Vec<Vec<(usize, usize)>>,
    dist: Vec<usize>,
    visited: Vec<bool>,
}

impl ASP {
    fn new(n: usize) -> Self {
        Self {
            graph: vec![vec![]; n + 1],
            dist: vec![2 << 24; n + 1],
            visited: vec![false; n + 1],
        }
    }

    fn dijkstra(&mut self, s: usize) -> Vec<Vec<usize>> {
        let mut shortest = vec![vec![]; self.graph.len()];
        let mut queue = VecDeque::new();
        self.dist[s] = 0;
        queue.push_back((s, 0));
        while let Some((v, p)) = queue.pop_front() {
            if p > self.dist[v] { continue; }
            for &(nv, np) in &self.graph[v] {
                if np == 0 { continue; }
                if self.dist[nv] > self.dist[v] + np {
                    self.dist[nv] = self.dist[v] + np;
                    shortest[nv].clear();
                    shortest[nv].push(v);
                    queue.push_back((nv, np));
                } else if self.dist[nv] == self.dist[v] + np {
                    shortest[nv].push(v);
                }
            }
        }
        shortest
    }

    fn bfs(&mut self, s: usize, shortest: &Vec<Vec<usize>>) {
        let mut queue = VecDeque::new();
        queue.push_back(s);
        self.visited[s] = true;
        while let Some(v) = queue.pop_front() {
            for &nv in &shortest[v] {
                if !self.visited[nv] {
                    self.visited[nv] = true;
                    queue.push_back(nv);
                }
                for i in 0..self.graph[nv].len() {
                    if self.graph[nv][i].0 == v { self.graph[nv][i].1 = 0; }
                }
            }
        }
    }
}

fn main() {
    let mut sc = Scanner::new();
    let mut so = BufWriter::new(stdout().lock());

    loop {
        let (n, m): (usize, usize) = (sc.read(), sc.read());
        if n == 0 { break; }
        let (s, d): (usize, usize) = (sc.read(), sc.read());
        let mut asp = ASP::new(n);
        for _ in 0..m {
            let (u, v, p): (usize, usize, usize) = (sc.read(), sc.read(), sc.read());
            asp.graph[u].push((v, p));
        }
        let shortest = asp.dijkstra(s);
        asp.bfs(d, &shortest);
        asp.dist = vec![2 << 24; n + 1];
        asp.dijkstra(s);
        if asp.dist[d] == 2 << 24 { writeln!(so, "-1").ok(); }
        else { writeln!(so, "{}", asp.dist[d]).ok(); }
    }
}